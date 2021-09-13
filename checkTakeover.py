#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:55 上午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : checkTakeover.py

import json,requests,sys
import queue
from threading import Thread


all_que = queue.Queue()

def checkvuln():
    while True:
        try:
            site = all_que.get(timeout=0.1)
        except:
            break
        # print(site)
        try:
            url_response_text = (url_get(site))
            json_dicts = providers_read()
            for json_dict in json_dicts:
                fingerprint_lists = json_dict['response'][0]  # 存储指纹信息
                # 过滤默认404页面导致误报
                if fingerprint_lists in url_response_text[1] and '<h1>404 Not Found</h1><' not in  url_response_text[1]:
                    print("[Takerover vuln][{}]:{},特征:{}".format(url_response_text[0], site, fingerprint_lists))
                # fingercname_lists = json_dict['cname']  # 存储cname信息
        except:
            pass

# 发起请求
def url_get(url):
    try:
        r = requests.get(url=url, timeout=5)
        status_code = r.status_code
        response_text = r.content.decode('utf-8')
        return status_code,response_text
    except:
        # print('[*]网络连接超时，请稍后重试')
        pass

# 指纹读取 存储到json_dicts中
def providers_read():
    try:
        with open('providers.json','r') as f:
            str_json = f.read()
            json_dicts = json.loads(str_json)
            return json_dicts
    except:
        print('[*]加载指纹文件失败，请检查是否存在providers.json文件')

def scan(files):
    for x in open(files):
        x = x.strip()
        if x.find('http') >= 0:
            pass
        else:
            x = 'http://' + x + '/'
        all_que.put(x)

    urlth = []
    for x in range(15):
        p = Thread(target=checkvuln)
        urlth.append(p)
        p.start()
    for paa in urlth:
        paa.join()

if __name__ == '__main__':
    filename = sys.argv[1]
    scan(filename)
