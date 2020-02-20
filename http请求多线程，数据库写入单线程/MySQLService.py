# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 0030 下午 1:55
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 连接数据库 执行sql语句
import datetime

from Config import Setting
import pymysql


class MySQLService:
    host = Setting.host
    user = Setting.user
    password = Setting.password

    def __init__(self, db):
        self.__conn = pymysql.Connect(host=self.host, user=self.user,
                                      password=self.password, database=db, charset='utf8')
        self.__cursor = self.__conn.cursor()

    def execute(self, sql, args=None):
        """

        :param sql: 要执行的sql语句
        :param args: tuple, list or dict
        :return:
        """
        self.__cursor.execute(sql, args=args)

    def execute_idu(self, sql, args=None):
        """
        执行增删改操作
        :param sql:
        :param args:
        :return: None
        """
        try:
            self.execute(sql, args)
            self.__conn.commit()
        except Exception as e:
            self.__conn.rollback()
            raise e

    def select(self, sql, args=None):
        """
        执行查询操作
        :param sql:
        :param args:
        :return:  元组类型 元素为查询到的每一个记录
        """
        self.execute(sql, args)
        return self.__cursor.fetchall()

    def close(self):
        self.__cursor.close()
        self.__conn.close()


class Saver:
    def __init__(self, data, username):
        """

        :param data:
        :param username: 这里指用户名url中的名字
        """
        self.data = data
        self.username = username

    def save(self):
        """
        保存数据 粉丝数据表格若存在先删除再创建
        :return: null
        """
        mysql = MySQLService(Setting.db)
        followers_table_name = self.username.replace('-', '_')
        mysql.execute(Setting.drop_sql.format(followers_table_name))
        mysql.execute(Setting.create_sql.format(followers_table_name))

        fake_count = 0
        sql1 = "INSERT INTO user_info(username, page_url, total_count, fake_count, recording_time) " \
               "VALUES('{}', '{}', {}, {}, '{}');"
        page_url = Setting.page_url_pattern.format(self.username)
        recording_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_count = self.data.qsize()

        sql2 = "INSERT INTO {}_followers_info(name, page_url, headline, gender, " \
               "follower_count, answer_count, articles_count, badge_count, is_fake) " \
               "VALUES('{}', '{}', '{}', {}, {}, {}, {}, {}, {})"

        done_count = 0
        while not self.data.empty():
            one_data = self.data.get()
            if one_data['is_fake'] == 1:
                fake_count += 1
            mysql.execute_idu(sql2.format(followers_table_name, *one_data.values()))
            done_count += 1
            print(done_count)
        mysql.execute_idu(sql1.format(self.username, page_url, total_count, fake_count, recording_time))

        mysql.close()
