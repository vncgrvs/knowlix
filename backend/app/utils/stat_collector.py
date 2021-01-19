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
        print("send login data to InfluxDB")
        point = influxdb_client.Point("user_login").tag(
            "user", user).field("login", 1.0)
        api.write(bucket=bucket, org=ORG, record=point)

    except Exception as err:
        print(err)
        pass


def log_sections(user: str, sections: list, bucket: str, api=write_api):
    try:
        print(client.health())
        
        for section in sections:
            point = influxdb_client.Point("downloads").tag(
                "user", user).tag("section", section).field("section", 1.0)
            print(f"send {section} data to InfluxDB")
            api.write(bucket=bucket, org=ORG, record=point)

    except Exception as err:
        print(err)
        pass
