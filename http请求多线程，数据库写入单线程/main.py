# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 10:25
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    :

from MultiSpider import *
from MySQLService import Saver


def main(username):
    queue = ZHIHUSpider.get_all_follower_data(username)
    saver = Saver(queue, username)
    saver.save()


if __name__ == '__main__':
    main('mu-yi-81-66')
