from fastapi import FastAPI

app = FastAPI()

workouts = []

@app.post("/workout")
def log_workout(workout: dict):
    workouts.append(workout)
    return {"message": "logged", "total": len(workouts)}

@app.get("/workouts")
def get_workouts():
    return workouts

@app.get("/health")
def health():
    return {"status": "ok"}

