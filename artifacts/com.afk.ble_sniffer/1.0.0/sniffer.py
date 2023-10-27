import sys
import time
import json
import datetime


import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    PublishToTopicRequest,
    PublishMessage,
    BinaryMessage
)

SENDING_INTERVAL = int(sys.argv[1])
TIMEOUT = 10
TOPIC = "iotc/rpt/d2gg/sub"
MAC_LIST_PATH = '/tmp/ble_macs'


ipc_client = awsiot.greengrasscoreipc.connect()



def publish_to_iotconnect(data_dict: dict):
    
    message = [{'time': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), 'data' : data_dict}]

    request = PublishToTopicRequest()
    request.topic = TOPIC
    publish_message = PublishMessage()
    publish_message.binary_message = BinaryMessage()
    publish_message.binary_message.message = bytes(json.dumps(message).encode('utf-8'))
    request.publish_message = publish_message
    operation = ipc_client.new_publish_to_topic()
    operation.activate(request)
    future = operation.get_response()
    future.result(TIMEOUT)


while True:

    # this code is supposed to be run externally
    # like in a systemd service
    import bl_scanner
    bl_scanner.get_bl_devices()
    #

    macs = ""
    with open(MAC_LIST_PATH, "r", encoding="UTF-8") as file:
        macs = file.read()

    to_send = { "macs": macs }
    print(f"Publish sending message {to_send}")
    publish_to_iotconnect(to_send)

    time.sleep(SENDING_INTERVAL)
