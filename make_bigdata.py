# -*- coding: utf-8 -*-
""" 模拟生成nginx日志
代码主要用于生成nginx日志，使用方法主要有以下两种，
1. 调用generate_logs_file函数，生成日志，并将日志保存到本地；
2. generate_logs函数作为模块引用到其他项目中，产生实时的日志流。
"""
import time
import json
import random
from datetime import datetime


def generate_logs_file(users, responses, path, count, buffer_size):
    for index in xrange(0, count, buffer_size):
        log_stream = ''
        selected_users = random.sample(users, buffer_size)
        for user in selected_users:
            response = random.choice(responses)
            log_stream += generate_log(user, response)
        write_to_file(log_stream, path)


def get_material(ips_path, user_agent_path, responses_path):
    ips = load_json(ips_path)
    user_agents = load_json(user_agent_path)
    users = generate_users(ips, user_agents)
    responses = load_json(responses_path)
    return users, responses


def generate_logs(users, responses, count):
    log_stream = ''
    for index in xrange(count):
        user = random.choice(users)
        response = random.choice(responses)
        log_stream += generate_log(user, response)
    return log_stream


def generate_log(user, response):
    current_time = datetime.now()
    stream = '{ip} - - [{current_time} +0800] "{api}" {status} {size} "-" "{user_agent}"\n'.format(
        ip=user['ip'],
        current_time=current_time,
        api=response['api'],
        status=response['status'],
        size=response['size'],
        user_agent=user['user_agent'].strip()
    )
    return stream


def write_to_file(stream, path):
    with open(path, 'a') as f:
        f.write(stream)


def generate_users(ips, user_agents):
    users = []
    for ip in ips:
        for user_agent in user_agents:
            user = {'ip': ip, 'user_agent': user_agent}
            users.append(user)
    return users


def load_json(path):
    with open(path, 'r') as f:
        stream = f.read()
        return json.loads(stream)


def main():
    ips_path = 'ips.json'
    user_agent_path = 'user_agent.json'
    ips = load_json(ips_path)
    user_agents = load_json(user_agent_path)
    users = generate_users(ips, user_agents)

    responses_path = 'responses.json'
    responses = load_json(responses_path)

    start_time = time.time()
    log_path = 'web.log'
    count = 1000000
    buffer_size = 1000
    generate_logs_file(users=users, responses=responses, path=log_path, count=count, buffer_size=buffer_size)
    print 'insert {count} rows into web.log. spend time: {spend_time} s'.format(count=1000000, spend_time=time.time()-start_time)


if __name__ == '__main__':
    main()
