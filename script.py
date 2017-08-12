#!./env/bin/python

import paho.mqtt.client as mqtt
import yaml

config = yaml.load(open('config.yml', 'r'))
print(config)

def on_connect(client, userdata, flags, rc):
  print ("Connected with result code {}".format(rc))
  client.subscribe("gordon/smarthouse/buttons")

def on_message(cleint, userdata, msg):
  try:
    button = int(msg.payload.decode('utf-8'))
  except:
    return
  print ("button {} pushed".format(button))
  for message in config[button]:
    client.publish(message['topic'], message['payload'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.bluesmoke.network", 1883, 60)

client.loop_forever()
