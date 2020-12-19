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
        

        message = {
            'operation':change['operationType'],
            'data':change['fullDocument'],
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
    # mongo_db_found = False
    client = MongoClient(MONGODB)
    tasks=client["taskdb"]
    col = tasks["ta"]
    print('created tasksdb and ta collection')

    # while not mongo_db_found:
    #     names = client.list_database_names()

    #     if 'taskdb' in names:
    #         collections=client["taskdb"].list_collection_names()

    #         if 'ta' in collections:
    #             col = client["taskdb"]["ta"]
    #             count_docs = int(col.count_documents({}))

    #             if count_docs > 0:
    #                  mongo_db_found = True
    #                  print("DB availaible now!")


    #     time.sleep(5)
    #     if not mongo_db_found:
    #         print("DB not there yet...")
    
    main()