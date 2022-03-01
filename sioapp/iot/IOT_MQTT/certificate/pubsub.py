# >>> import ssl
# >>> ssl.OPENSSL_VERSION
# 'OpenSSL 1.1.1l  24 Aug 2021'

# import json
# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("iotconsole-1643319534105-1")

# For TLS mutual authentication
myMQTTClient.configureEndpoint("abye2kp5ues9g-ats.iot.us-west-2.amazonaws.com", 8883)

path = "C:\\Users\\schristian\\Desktop\\schristian\\SIO_SERVER\\iot\\IOT_MQTT\\certificate\\"
rootca = "C:\\Users\\schristian\\Desktop\\schristian\\SIO_SERVER\\iot\\IOT_MQTT\\certificate\\AmazonRootCA1.crt"
privatek = "C:\\Users\\schristian\\Desktop\\schristian\\SIO_SERVER\\iot\\IOT_MQTT\\certificate\\9b675e4114c5d2db1f8e9cda32a8cc7b68a761052abd49e5289b286d6b85321b_private.key"
certificate = "C:\\Users\\schristian\\Desktop\\schristian\\SIO_SERVER\\iot\\IOT_MQTT\\certificate\\9b675e4114c5d2db1f8e9cda32a8cc7b68a761052abd49e5289b286d6b85321b_certificate.pem"
myMQTTClient.configureCredentials(rootca, privatek, certificate)


# myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
# myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
# myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
# myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


myMQTTClient.connect()
# myMQTTClient.publish("info", "connected", 1)

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }


# i = 0
# while True:
#     x['age'] = i
#     myMQTTClient.publish("info", json.dumps(x), 1)
#     i+=1


# myMQTTClient.connect()
# myMQTTClient.publish("myTopic", "myPayload", 0)
# myMQTTClient.subscribe("myTopic", 1, "customCallback")
# myMQTTClient.unsubscribe("myTopic")
# myMQTTClient.disconnect()
