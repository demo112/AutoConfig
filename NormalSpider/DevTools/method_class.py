import time

import requests
import write


class Devtools:
    def __init__(self):
        self.base_url = "http://localhost:9000/"
        pass

    def make_url(self, father_url="", child_url=""):
        """
        通过输入URL片段延长url
        :param base_url:
        :return:
        """
        url = father_url + child_url
        return url

    def get_page(self, url, type):
        p = requests.get(url)
        # 1、校验请求结果
        status = p.status_code
        if status == 200:
            print("%s请求成功，下载网页中" % url)
            # 2、获取请求内容
            data = self.parse_page(p, type)
        elif status == 400 or 404 or 403:
            print("可能无权限访问该链接，请核实")
            data = None
        else:
            print("未知情况，请修改脚本处理异常")
            data = None
        return data

    def parse_page(self, data, type):
        if type == 'json':
            js = data.json(encoding="utf-8")
            data = js
        elif type == "html":
            data = data
        return data

    def save_it(self, url, date):
        filename = url.split("/")[-1] + '.html'
        date =date.text
        with open(filename, "w", encoding="utf-8") as f:
            f.write(date)

class MakeRandom:
    def __init__(self):
        pass

    def way_1_time(self):
        t = str(time.time()).split(".")
        ts = t[0] + t[1][0:3]
        return ts





if __name__ == '__main__':
    dev = Devtools()
    url = dev.make_url()
    page = dev.get_page()
    target = dev.parse_page()
