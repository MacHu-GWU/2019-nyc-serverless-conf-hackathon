import requests
import json
from datetime import datetime

device_id = "de042ca7-3bd0-4d66-8690-d88312d18cef"
create_at = str(datetime.utcnow())
# lat, lng = 40.702962, -74.011626 # 10006
lat, lng = 40.713672, -74.006806 # 10007

data = dict(
    device_id=device_id,
    create_at=create_at,
    lat=lat,
    lng=lng,
)

url = "https://69kusj68ik.execute-api.us-east-1.amazonaws.com/dev/rpc/gps-tracker"
res = requests.post(url, headers=dict(auth="allow"), data=json.dumps(data))
print(res.text)
