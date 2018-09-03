# coding=utf-8

import json
import urllib
import urllib2
import os


class ShouHuiJianZhu(object):
    def __init__(self):
        pass

    def gain_response(self, base_url, headers):
        # url = 'http://image.so.com/j?q=%E6%89%8B%E7%BB%98%E5%BB%BA%E7%AD%91&src=srp' \
        #       '&correct=%E6%89%8B%E7%BB%98%E5%BB%BA%E7%AD%91&pn=60&ch=&sn=96&cn=0&gn=0&kn=36'
        page = 0
        for i in range(10):
            page += 60
            params = {
                'q': '手绘建筑',
                'src': 'srp',
                'correct': '手绘建筑',
                'pn': page,
                'ch': '',
                'cn': '0',
                'gn': '0',
                'kn': '36'
            }
            data = urllib.urlencode(params)
            url = base_url + data
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request).read()
            json_data = json.loads(response)
            # print(json_data)
            list = json_data.get('list')
            for image in list:
                image_url = image.get('thumb')
                self.download_image(image_url)

    def download_image(self, image_url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        request = urllib2.Request(image_url, headers=headers)
        response = urllib2.urlopen(request).read()
        filename = image_url[-10:]
        # os.makedirs('images')
        # folder = '/images'
        # if not os.path.exists(folder):
        #     os.makedirs(folder)
        with open(filename, 'wb')as f:
            f.write(response)

    def main(self):
        base_url = 'http://image.so.com/j?'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        self.gain_response(base_url, headers)


if __name__ == '__main__':
    jz = ShouHuiJianZhu()
    jz.main()