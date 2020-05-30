from VirtualAsistant import VirtualAsistant
import time
import json

with open("config.json") as conf:
    config = json.load(conf)

VA = VirtualAsistant(config["ownerName"], config["VirtualAsistantName"], config["Language"], config["databaseName"])

time.sleep(1)
while(1):
    VA.stt()
