# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 10:25
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    :

from MultiSpider import *
from MySQLService import Saver


def main(username):
    Saver.create_table(username)
    ZHIHUSpider.start_spider(username)
    Saver.save_user_info(username)


if __name__ == '__main__':
    start = time.time()
    main('neng-liang-a-wei-er')
    end = time.time()
    print("一共耗时：", end - start)
