import os
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from motor.motor_tornado import MotorClient
from bson import json_util
from pymongo import MongoClient
import time


MONGODB = os.getenv("MONGODB")


class ChangesHandler(tornado.websocket.WebSocketHandler):

    connected_clients = set()

    def check_origin(self, origin):
        return True

    def open(self):
        ChangesHandler.connected_clients.add(self)

    def on_close(self):
        ChangesHandler.connected_clients.remove(self)

    @classmethod
    def send_updates(cls, message):
        for connected_client in cls.connected_clients:
            connected_client.write_message(message)

    @classmethod
    def on_change(cls, change):
        print(change)
        message = {
            'operation': change['operationType'],
            'data': change['fullDocument'],
            'taskID': change['documentKey']['_id']

        }

        # message = f"{change['operationType']}: {change['fullDocument']}"
        # message = f"{change['operationType']}"

        ChangesHandler.send_updates(message)


change_stream = None


async def watch(collection):
    global change_stream

    async with collection.watch(full_document='updateLookup') as change_stream:
        async for change in change_stream:
            ChangesHandler.on_change(change)


def main():
    client = MotorClient(MONGODB)
    collection = client["taskdb"]["ta"]

    app = tornado.web.Application(
        [(r"/tasks", ChangesHandler)]
    )

    app.listen(3333)

    loop = tornado.ioloop.IOLoop.current()
    loop.add_callback(watch, collection)
    try:
        loop.start()
    except KeyboardInterrupt:
        pass
    finally:
        if change_stream is not None:
            change_stream.close()


if __name__ == "__main__":
    print("started mongo watcher.")
    mongo_isLive = False

    while not mongo_isLive:
        try:
            client = MongoClient(MONGODB)
            tasks = client["taskdb"]
            col = tasks["ta"]
            mongo_isLive = True


        except Exception as e:
            print('error ', e)
            time.sleep(5)
        

    print('MongoDB connected to Websocket!')

    main()
