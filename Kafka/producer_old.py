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
from kafka import KafkaProducer

KAFKA_BROKERLIST = "localhost:9092"
TOPIC = 'gam'


def run(brokers, car_count):
    """
    Run the test
    """
    producer = KafkaProducer(bootstrap_servers=[brokers])
    speed = [60 for _ in range(car_count)]
    distance = [0 for _ in range(car_count)]
    for i in range(0, 500):
        car_id = random.randint(1, 1)

        all_speeds = [i for i in range(-5, 6, 5)]
        speed[car_id-1] += random.choice(all_speeds)
        temp_speed = speed[car_id-1] if speed[car_id-1] > 0 else 0

        distance[car_id-1] += speed[car_id-1] / 3.6;

        producer.send(TOPIC, ','.join([str(car_id), str(temp_speed), str(distance[car_id-1]), '1234']))
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
