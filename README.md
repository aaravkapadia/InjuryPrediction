Work:
1. train model on csv data
2. backend flow: user posts workout, oura api data ingest into postgres(by scheduled ingest) -> user gets injury risk(run model on postgres history data on each get- feature engineered to join oura data + workout data). User can updata workout/history via put or delete via delete
3. weekly retraining on accumulated data(eventually want online learning)