# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import sys
import os
import os.path
import time
import json
import datetime
import random

import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    PublishToTopicRequest,
    PublishMessage,
    BinaryMessage
    #JsonMessage
)
from dummy_sensor import DummySensor

frequency = int(sys.argv[1])
print(frequency)
TIMEOUT = 30
publish_rate = 1.0

ipc_client = awsiot.greengrasscoreipc.connect()

sensor = DummySensor()

topic = "iotc/rpt/d2gg/sub"

while True:
    data = {"macs" : sensor.read_value()}
    message = [{
            "uniqueId": "npp",
            "time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "data": data
    }]
    print("Publish sending message {}".format(message))
    msgstring = json.dumps(message)
    request = PublishToTopicRequest()
    request.topic = topic
    publish_message = PublishMessage()
    publish_message.binary_message = BinaryMessage()
    publish_message.binary_message.message = bytes(msgstring, "utf-8")
    request.publish_message = publish_message
    operation = ipc_client.new_publish_to_topic()
    operation.activate(request)
    try:
        future_response = operation.get_response()
        print("Future value : :  ", future_response)

        future_response.result(TIMEOUT)
    except Exception as error:
        print("Error in future()", str(error))  

    print(frequency)
    time.sleep(frequency)
    pass
