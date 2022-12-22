import serial
import time
from datetime import date
import json

ser = serial.Serial("COM7", 9600)

storage = {}

with open('data.json') as json_file:
    storage = json.load(json_file)

while True:

    rfid = str(ser.readline())
    rfid = str(rfid[2:-5])
    print(rfid)
    
    if str(rfid) not in storage.keys():
        storage[rfid] = {"name":str(input("New member! Enter your name: ")), "totaltimespent":0, "entrytime":int(time.time()), "entrydate":str(date.today())}
        print(storage[rfid]["name"], " in")
        print("time : ", time.strftime('%H:%M:%S'))
        print()
    else:
        if storage[rfid]["entrytime"] == 0:
            storage[rfid]["entrytime"] = int(time.time())
            storage[rfid]["entrydate"] = str(date.today())
            print(storage[rfid]["name"], " in")
            print("time : ", time.strftime('%H:%M:%S'))
            print()
        else:
            storage[rfid]["totaltimespent"] += ((int(time.time()) - int(storage[rfid]["entrytime"]))//60)
            storage[rfid]["entrytime"] = 0
            print(storage[rfid]["name"], " out")
            print("time : ", time.strftime('%H:%M:%S'))
            print()

    with open('data.json', 'w') as json_file:
        json.dump(storage, json_file)
