# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 5:36
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    :

from Config import Setting
from MySQLService import MySQLService
from URLDealer import URLDealer
from DataMaker import DataParser
from multiprocessing import Queue
from MultiSpider import *


def test(function):
    def decorated_test(*args, **kwargs):
        print('测试开始: ' + function.__name__)
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print('发生异常: ' + str(e))
            raise e
        else:
            print('测试返回值为：' + str(result))
            return result
        finally:
            print('测试结束: ' + function.__name__)

    return decorated_test


@test
def test_get_response():

    test_url = Setting.url.format('mu-yi-81-66', 100, 20)
    url_dealer = URLDealer(test_url, Setting.headers, Setting.timeout)
    response = url_dealer.get_response()
    return type(response.text)


@test
def test_parse_follower_data():
    test_url = Setting.url.format('mu-yi-81-66', 20, 20)
    url_dealer = URLDealer(test_url, Setting.headers, Setting.timeout)
    data = url_dealer.get_response().text
    dm = DataParser(data, Queue(100))
    dm.parse_follower_data()
    queue = dm.followers_queue
    while not queue.empty():
        print(queue.get())


@test
def test_follower_count():
    sp = SpiderPrepare('mu-yi-81-66')
    return sp.follower_count()


@test
def test_get_url_queue():
    sp = SpiderPrepare('mu-yi-81-66')
    url_queue = sp.get_url_queue()
    while not url_queue.empty():
        print(url_queue.get())


@test
def test_select():
    mysql = MySQLService(Setting.db)
    followers_table_name = 'mu_yi_81_66_followers_info'
    select_sql = "SELECT COUNT(*), SUM(is_fake) FROM {}".format(followers_table_name)
    return mysql.select(select_sql)


if __name__ == '__main__':
    result = test_select()
    print(type(int(result[0][1])))

