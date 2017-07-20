# -*- coding: utf-8 -*-
import time
import random
# from kafka import KafkaProducer
from make_bigdata import generate_logs, get_material


PAGE_NUM = 100
MAX_MSG_NUM = 3
MAX_CLICK_TIME = 5
MAX_STAY_TIME = 10
IPS_PATH = 'ips.json'
USER_AGENTS_PATH = 'user_agent.json'
RESPONSES_PATH = 'responses.json'


# class ConnectKafka(object):
#     kafka_host = None  # host
#     kafka_port = None  # port
#     kafka_topic = None
#     producer = None

#     def __init__(self, kafka_host, kafka_port, kafka_topic):
#         self.kafka_host = kafka_host
#         self.kafka_port = kafka_port
#         self.kafka_topic = kafka_topic

#     def create_connect(self):
#         self.producer = KafkaProducer(bootstrap_servers=['{kafka_host}:{kafka_port}'.format(
#             kafka_host=self.kafka_host,
#             kafka_port=self.kafka_port
#         )])

#     @staticmethod
#     def produce_msg():
#         logs_size = random.randrange(1, 10000)
#         msg = generate_logs(IPS_PATH, USER_AGENTS_PATH, RESPONSES_PATH, logs_size)
#         time.sleep(0.1)
#         print msg
#         return msg

#     def send_msg(self):
#         while True:
#             msg = self.produce_msg()
#             response = self.producer.send(self.kafka_topic, msg.encode('utf-8'))
#             time.sleep(0.1)

#     def run(self):
#         self.create_connect()
#         #msg = self.produce_msg()
#         self.send_msg()

# if __name__ == '__main__':
#     ck = ConnectKafka('10.1.4.17', 6667, 'my_test')
#     ck.run()


if __name__ == '__main__':
    users, responses = get_material(IPS_PATH, USER_AGENTS_PATH, RESPONSES_PATH)
    while True:
        logs_size = random.randint(1, 10000)
        import ipdb
        # ipdb.set_trace()
        msg = generate_logs(users, responses, logs_size)
        print msg
        time.sleep(0.1)
