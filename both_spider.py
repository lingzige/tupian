# coding=utf-8


from selenium import webdriver
from lxml import etree
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import csv


class Boss(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.zhipin.com'
        self.url = 'https://www.zhipin.com/c101030100/h_101030100/?query=python&page=1&ka=page-prev'
        self.position_links = []
        self.position_content = []
        self.File = open('./bossSpider.csv', 'a')
        self.writer = csv.writer(self.File)
        self.writer.writerow(('position_name', 'salary', 'city', 'experience', 'education', 'position_type'))

    def run(self):
        """程序入口"""
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="next"]'))
            )
            self.parse_list_url(source)
            next_btn = self.driver.find_element_by_xpath('//a[@class="next"]')
            if "next disabled" in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()
            time.sleep(1)

    def parse_list_url(self, source):
        """获取列表页每个职位的url"""
        html = etree.HTML(source)
        links = html.xpath('//h3[@class="name"]/a/@href')
        # print(links)
        for link in links:
            # links中的链接包含公司的链接，所以需要将公司的链接筛选掉，用startswith方法过滤出只有职位的链接
            if link.startswith('/job_detail'):
                # 职位链接是不完全的，要拼接基础链接
                url = self.base_url + link
                self.parse_detail_page(url)
                time.sleep(1)

    def parse_detail_page(self, url):
        """进入详情页，获得详情页的源码"""
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="name"]/h1'))
        )
        source = self.driver.page_source
        self.parse_detail_info(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_info(self, source):
        """获取详情页需要的信息"""
        html = etree.HTML(source)
        position_name = html.xpath('//div[@class="name"]/h1/text()')[0]
        salary = html.xpath('//span[@class="badge"]/text()')[0].strip()
        city = html.xpath('//div[@class="info-primary"]/p/text()')[0]
        experience = re.findall(r'<em class="vline">.*?>(.*?)<', source, re.S)[0]
        education = re.findall(r'<em class="vline"></em?.*?<em.*?></em>(.*?)</p>', source, re.S)[0]
        position_desc = re.findall(r'<div class="text">(.*?)</div>', source, re.S)[0].strip()
        position_desc = re.sub(r'<br>', '', position_desc)
        positions = {
            'position_name': position_name,
            'salary': salary,
            'city': city,
            'experience': experience,
            'education': education,
            'position_desc': position_desc
        }
        self.position_content.append(positions)
        # print(self.position_content)
        position = json.dumps(positions, ensure_ascii=False)
        self.writer.writerow((positions['position_name'].encode('utf-8'), positions['salary'].encode('utf-8'), positions['city'].encode('utf-8'), positions['experience'].encode('utf-8'), positions['education'].encode('utf-8'), positions['position_desc'].encode('utf-8')))
        time.sleep(1)
        print(position.encode('utf-8'))
        print('='*50)


if __name__ == '__main__':
    boss = Boss()
    boss.run()