"""
Name:       producer.py
Purpose:    Generates test data for kafka-spark-opentsdb example app
            the various component services such as HDFS, HBase etc
Author:     PNDA team
Created:    14/03/2016
"""
import io
import os
import sys
import getopt
import random
import time
from time import gmtime, strftime

import avro.schema
import avro.io
from kafka import KafkaProducer

KAFKA_BROKERLIST = "localhost:9092"

# Path to user.avsc avro schema
HERE = os.path.abspath(os.path.dirname(__file__))
SCHEMA_PATH = HERE + "/dataplatform-raw.avsc"

# Kafka topic
# TOPIC = "avro.flink.streaming"
TOPIC = 'gam'
CURRENT_TIME_MILLIS = lambda: int(round(time.time() * 1000))


def run(brokers, car_count):
    """
    Run the test
    """
    schema = avro.schema.parse(open(SCHEMA_PATH).read())
    producer = KafkaProducer(bootstrap_servers=[brokers])
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    extra_bytes = bytes('')

    speed = [60 for _ in range(car_count)]
    distance = [0 for _ in range(car_count)]
    for i in range(0, 5):
        gen_data = {}

        car_id = random.randint(1, 1)
        gen_data['car_id'] = car_id

        all_speeds = [i for i in range(-5, 6, 5)]
        speed[car_id-1] += random.choice(all_speeds)
        temp_speed = speed[car_id-1]
        gen_data['speed'] = temp_speed if temp_speed > 0 else 0

        distance[car_id-1] += speed[car_id-1] / 3.6;
        gen_data['distance'] = distance[car_id-1]

        gen_data = "+"*100
        writer.write({"timestamp": CURRENT_TIME_MILLIS(),
                      "rawdata": str(gen_data)}, encoder)
        raw_bytes = bytes_writer.getvalue()

        # reset buffer to start index
        bytes_writer.seek(0)
        print(extra_bytes + raw_bytes)
        producer.send(TOPIC, extra_bytes + raw_bytes)
        time.sleep(1)


if __name__ == '__main__':

    broker_list = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:", ["brokerlist="])
    except getopt.GetoptError:
        print 'producer.py [-b localhost:9092] '
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'producer.py [--brokerlist broker:port [,broker:port]]'
            sys.exit()
        elif opt in ("-b", "--brokerlist"):
            print "brokerlist: %s" % arg
            broker_list = arg

    run(broker_list if broker_list is not None else KAFKA_BROKERLIST, 1)
