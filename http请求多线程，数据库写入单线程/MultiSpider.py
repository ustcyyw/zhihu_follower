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


class SpiderThread(Thread):
    """
    爬虫进程类
    """

    def __init__(self, name, url_queue, follower_queue):
        super(SpiderThread, self).__init__()
        self.name = name
        self.url_queue = url_queue
        self.follower_queue = follower_queue

    # override
    def run(self):
        """
        不断爬取队列中url 每次爬取间隔指定时间
        :return:
        """
        print("Process " + self.name + " start!")
        while not self.url_queue.empty():
            self.spider()
            time.sleep(Setting.sleep_time)
        print("Process " + self.name + " end!")

    def spider(self):
        url = self.url_queue.get()
        url_dealer = URLDealer(url, Setting.headers, Setting.timeout)
        data = url_dealer.get_response().text
        data_parser = DataParser(data, self.follower_queue)
        data_parser.parse_follower_data()


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
    def get_all_follower_data(cls, username):
        spider_prepare = SpiderPrepare(username)
        url_queue = spider_prepare.get_url_queue()
        follower_count = spider_prepare.follower_count()

        follower_queue = Queue.Queue(follower_count)
        threads = []
        for i in range(cls.thread_count):
            st = SpiderThread(str(i), url_queue, follower_queue)
            st.start()
            time.sleep(0.15)
            threads.append(st)

        for thread in threads:
            thread.join()

        return follower_queue
