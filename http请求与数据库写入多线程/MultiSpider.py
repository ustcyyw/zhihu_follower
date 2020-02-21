# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 8:30
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 多进程爬取数据

import json
import time
from threading import Thread
from DataMaker import DataParser
from URLDealer import URLDealer
from Config import Setting
import queue as Queue
from MySQLService import Saver


class SpiderThread(Thread):
    """
    爬虫线程类
    """

    def __init__(self, url_queue, username):
        super(SpiderThread, self).__init__()
        self.username = username
        self.url_queue = url_queue

    # override
    def run(self):
        """
        不断爬取队列中url 每次爬取间隔指定时间
        :return:
        """
        while not self.url_queue.empty():
            self.spider()
            time.sleep(Setting.sleep_time)

    def spider(self):
        try:
            url = self.url_queue.get()
            url_dealer = URLDealer(url, Setting.headers, Setting.timeout)
            data = url_dealer.get_response().text
            data_parser = DataParser(data)
            followers_list = data_parser.parse_follower_data()
            saver = Saver(followers_list, self.username)
            saver.save_followers_info()
        except Exception as e:
            print(str(e))


class SpiderPrepare:
    def __init__(self, name):
        """
        :param name: 知乎用户名 需要从流量器url中截取
        """
        self.name = name

    def follower_count(self):
        """
        得到总的粉丝数
        :return:
        """
        url = Setting.url.format(self.name, 20, 20)
        data_str = URLDealer(url, Setting.headers, Setting.timeout).get_response().text
        data = json.loads(data_str)
        return data['paging']['totals']

    def get_url_queue(self):
        """
        得到所有json数据的url
        :return:
        """
        followers_count = self.follower_count()
        page_count = int(followers_count / 20) + 1
        queue = Queue.Queue(page_count)
        for i in range(0, page_count):
            url = Setting.url.format(self.name, i * 20, 20)
            queue.put(url)
        return queue


class ZHIHUSpider:
    """多线程爬虫 得到某用户所有粉丝数据"""
    thread_count = Setting.thread_count

    @classmethod
    def start_spider(cls, username):
        spider_prepare = SpiderPrepare(username)
        url_queue = spider_prepare.get_url_queue()

        threads = []
        for i in range(cls.thread_count):
            st = SpiderThread(url_queue, username)
            st.start()
            time.sleep(0.29)
            threads.append(st)

        for thread in threads:
            thread.join()
