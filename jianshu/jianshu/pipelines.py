# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 950503,
            'database': 'jianshu',
            'charset': 'utf8'
        }
        # 密码必须用引号
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='950503', database='jianshu', charset='utf8')
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['avatar'], item['author'], item['pub_time'], item['content'], item['artical_id'], item['original_url']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into artical(id, title, avatar, author, pub_time, content, artical_id, original_url)
                values(null, %s, %s, %s, %s, %s, %s, %s)
            """
            return self._sql
        return self._sql


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '950503',
            'database': 'jianshu2',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                   insert into artical2(id, title, avatar, author, pub_time, content, artical_id, original_url)
                   values(null, %s, %s, %s, %s, %s, %s, %s)
               """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, item, cursor):
        cursor.execute(self.sql, (item['title'], item['avatar'], item['author'], item['pub_time'], item['content'], item['artical_id'], item['original_url']))

    def handle_error(self, error, item, spider):
        print('='*10)
        print(error)
        print('='*10)
