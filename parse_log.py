# -*- coding: utf-8 -*-
import re


def parse_single_line(stream):
    items = re.match('(.*?) - - \[(.*?) \+0800\] "(.*?)" .*? "-" "(.*?)"', stream).groups()
    ip, time, api, user_agent = items[0], items[1], items[2], items[3] 
    # 过滤掉一些js,css和图片请求
    if re.search('(\.(css|js|bmp|gif|png|jpeg))|image', api):
        return None
    # 通过user_agent获得请求使用的终端类型
    wide_type = 'unknown'
    small_type = 'unknown'
    categorys = [
        {'wide':'mobile', 'small':'Android'},
        {'wide':'mobile', 'small':'iPhone'},
        {'wide':'mobile', 'small':'Windows Phone OS'},
        {'wide':'pc', 'small':'Mac OS X'},
        {'wide':'pc', 'small':'Windows NT'},
    ]
    for category in categorys:
        if category['small'] in user_agent:
            small_type = category['small']
            wide_type = category['wide']
            break
    return [ip, time, api, small_type, wide_type]


def main():
    with open('web.log', 'r') as f:
        for line in f:
           print parse_single_line(line)


if __name__ == "__main__":
    main()
