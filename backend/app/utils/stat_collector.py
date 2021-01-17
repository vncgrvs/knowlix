import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
from .config import TOKEN_INFLUXDB, ORG, URL

client = influxdb_client.InfluxDBClient(
    url=URL,
    token=TOKEN_INFLUXDB,
    org=ORG
)
write_api = client.write_api(write_options=SYNCHRONOUS)


def log_user_login(user: str, bucket: str, api=write_api):
    try:
        point = influxdb_client.Point("user_login").tag("user",user).field("login", 1)
        api.write(point)
    except Exception as err:
        print(err)
