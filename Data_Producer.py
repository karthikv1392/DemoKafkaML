_Author_ = "Karthik Vaidhyanathan"

import subprocess

import csv
import sys
import time
from kafka import KafkaConsumer, KafkaProducer
from Initializer import Initialize
from datetime import datetime,timedelta

init_object = Initialize()

class kafka_producer():
    def publish_message(self,producer_instance, topic_name, key, value):
        try:
            key_bytes = bytearray(key,'utf8')
            value_bytes = bytearray(value,'utf8')
            print (topic_name, key, value)
            producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
            producer_instance.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def connect_kafka_producer(self):
        _producer = None
        try:
            _producer = KafkaProducer(bootstrap_servers=[init_object.kafka_host], api_version=(0, 10))
            #_producer = KafkaProducer(bootstrap_servers=['192.168.1.41:9092'], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
        finally:
            return _producer


producer_object = kafka_producer()


class Data_Streamer():

    def __init__(self):
        self.start_time = datetime.now()

    def stream_data(self):
        producer_instance = producer_object.connect_kafka_producer()
        with open (init_object.data_path + init_object.stream_file, 'r') as stream_file:
            for line in stream_file.readlines():
                x_val =  float(line.strip('\n'))
                print (x_val)
                producer_object.publish_message(producer_instance, "pizza", "data", str(x_val))
                time.sleep(2)



if __name__ == '__main__':
    data_producer_object = Data_Streamer()
    data_producer_object.stream_data()