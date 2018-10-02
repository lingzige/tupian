# coding=utf-8

from selenium import webdriver
import time
from lxml import etree
import re
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class LaGou(object):
    position_name_input = raw_input('请输入你要查询的职位的名称:')

    def __init__(self):
        """定义driver和初始页面的url"""
        self.drive = webdriver.Firefox()
        self.url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput=' % LaGou.position_name_input
        self.positions = []
        self.File = open('lagouPosition.csv', 'a')
        self.writer = csv.writer(self.File)
        self.writer.writerow(('position_name', 'salary', 'city', 'experience', 'education', 'job_type', 'desc'))

    def run(self):
        """爬虫的入口函数"""
        self.drive.get(self.url)
        # 使用无限循环来进行点击下一页，当if条件满足时，结束循环
        while True:
            source = self.drive.page_source
            # 显示等待
            WebDriverWait(driver=self.drive, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="pager_next "]'))
            )
            self.parse_page(source)
            # 获取下一页的点击框，并判断当到最后一页时，跳出该循环
            next_btn = self.drive.find_element_by_xpath('//span[@class="pager_next "]')
            # 判断点击到最后一页时，结束点击
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
                # 没有就一直点击，每隔2秒点击一次
            else:
                next_btn.click()
            time.sleep(1)

    def parse_page(self, source):
        """获取每个职位的url，以便进入职位的详情页"""
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            # print(link)
            self.parse_detail_source(link)
            time.sleep(2)

    def parse_detail_source(self, url):
        """获取详情页面的源码"""
        # 这个是在同一个窗口打开页面，但是爬取过程中要打开两个窗口，所以需要重新打开一个窗口
        # self.drive.get(url)
        # 重新打开一个页面，打开之后，需要把driver切换到这个页面上
        # 重新打开一个页面的原因是因为点击下一页这个操作只能在列表页进行，如果不切换窗口的话就会造成在详情页无法点击下一页
        self.drive.execute_script("window.open('%s')" % url)
        self.drive.switch_to.window(self.drive.window_handles[1])
        # 放在这个地方是因为等待这个窗口的打开，判断打开的条件就是出现了工作要求这项
        WebDriverWait(self.drive, timeout=10).until(
            # 为什么两处的显示等待中的xpath路劲不一样?这个地方是等待的条件，写这个就说明等待这个职位名称出现就停止等待，也可以是别的。
            # EC.presence_of_element_located((By.XPATH, '//div[@class="job-name"]/span[@class="name"]'))
            EC.presence_of_element_located((By.XPATH, '//dd[@class="job_request"]//span[1]'))
        )
        source = self.drive.page_source
        self.parse_detail_page(source)
        time.sleep(1)
        self.drive.close()
        # 关闭详情页之后，需要把driver重新切换到列表页
        self.drive.switch_to.window(self.drive.window_handles[0])

    def parse_detail_page(self, source):
        """解析详情页，获取信息"""
        html = etree.HTML(source)
        position_name = html.xpath('//span[@class="name"]/text()')[0]
        salary = html.xpath('//dd[@class="job_request"]//span[1]/text()')[0].strip()
        city = html.xpath('//dd[@class="job_request"]//span[2]/text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        experience = html.xpath('//dd[@class="job_request"]//span[3]/text()')[0].strip()
        experience = re.sub(r'[\s/]', '', experience)
        education = html.xpath('//dd[@class="job_request"]//span[4]/text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)
        job_type = html.xpath('//dd[@class="job_request"]//span[5]/text()')[0].strip()
        job_type = re.sub(r'[\s/]', '', job_type)
        desc = ''.join(html.xpath('//dd[@class="job_bt"]//p/text()')).strip()
        position = {
            'position_name': position_name,
            'salary': salary,
            'city': city,
            'experience': experience,
            'education': education,
            'job_type': job_type,
            'desc': desc
        }
        self.positions.append(position)
        # text = json.dumps(self.positions, ensure_ascii=False)
        json_position = json.dumps(position, ensure_ascii=False)
        self.writer.writerow((position['position_name'].encode('utf-8'), position['salary'].encode('utf-8'), position['city'].encode('utf-8'), position['experience'].encode('utf-8'), position['education'].encode('utf-8'), position['job_type'].encode('utf-8'), position['desc'].encode('utf-8')))
        print(json_position.encode('utf-8'))
        # print(text.encode('utf-8'))
        print('='*40)


if __name__ == '__main__':
    spider = LaGou()
    spider.run()
