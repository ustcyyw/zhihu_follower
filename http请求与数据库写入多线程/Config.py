# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 5:20
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 配置文件


class Setting:
    """http请求headers配置 需要修改cookie"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' \
                      '537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'cookie': '_zap=de06290c-0228-49fa-b623-51e8d682fc50; d_c0="AKCuHJNWig2PTmM2kcnB6MbGJiU2BK_St_k=|1525402017"; _xsrf=4auI7fdpCTBKT06MEr7FTYz8IRU0qsO3; __utma=51854390.229267630.1530896375.1530896375.1530896375.1; __utmv=51854390.100-1|2=registration_date=20160302=1^3=entry_date=20160302=1; __gads=ID=1afd0bf97012fb9d:T=1557398108:S=ALNI_MZ5Yh6XfnOBFlbYqmj6MntjOxbrjA; tst=r; capsion_ticket="2|1:0|10:1580287830|14:capsion_ticket|44:NjE4MWRiNTgzYzZjNGEwMGE1MTk0NjEwZmQzNGRhZDQ=|98b1d7c449a898b09e923e5a49eaf629c0e1eb714d81dec8e4d6984b058a9c5f"; z_c0="2|1:0|10:1580287871|4:z_c0|92:Mi4xMFE2ekFnQUFBQUFBb0s0Y2sxYUtEU1lBQUFCZ0FsVk5mNVVlWHdDdmpOYTR0TThEc0s0ZjFUdVNRNE15cWstNzdR|2c2a0fe385b6b50701a49e170fb41660002131f4be8ccea9ec26cdeb49af864d"; q_c1=44a46e11f9a24928a272927f8eff6278|1580394957000|1519116400000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1580361287,1580371433,1580465480,1580641947; BAIDU_SSP_lcr=https://www.baidu.com/link?url=Mu-II2lbFaGpQf-QbLISiXydudRindF4RsfBTwzVi1_&wd=&eqid=baab9d0b001cb694000000065e36ae7a; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1580641952; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1580641925|1580641917'
    }

    """请求url的限定时间"""
    timeout = 10

    "得到关注者数据的url"
    url = "https://www.zhihu.com/api/v4/members/{}/followers?" \
          "include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&" \
          "offset={}&limit={}"

    """知乎主页url模式"""
    page_url_pattern = 'https://www.zhihu.com/people/{}'

    """请求url发生异常时再次请求的等待时间"""
    exception_wait = 1

    """多线程爬取时，爬取每个url后的等待时间"""
    sleep_time = 0.85

    """线程数"""
    thread_count = 8

    """数据库相关配置：host user 及密码"""
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'zhihu_followers'

    """表格构造相关sql"""
    drop_sql = "DROP TABLE IF EXISTS {}_followers_info;"
    create_sql = "CREATE TABLE {}_followers_info  (" \
                 "id int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键'," \
                 "name varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'follower名字'," \
                 "page_url varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'follower主页url'," \
                 "headline varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '个人简介'," \
                 "gender int(1) NOT NULL COMMENT '性别'," \
                 "follower_count int(11) NOT NULL COMMENT '粉丝数'," \
                 "answer_count int(11) NOT NULL COMMENT '回答数'," \
                 "articles_count int(11) NOT NULL COMMENT '文章数'," \
                 "badge_count int(11) NOT NULL COMMENT '徽章数'," \
                 "is_fake int(1) NOT NULL COMMENT '是否为假粉 1为假粉'," \
                 "PRIMARY KEY (id) USING BTREE" \
                 ");"
