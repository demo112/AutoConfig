from NormalSpider.DevTools.method_class import *

def open_dev_tools():
    base_url = "http://localhost:9000"

    mr = MakeRandom()
    time_random = mr.way_1_time()


    dev = Devtools()
    random_term = "/json/list?t="
    target_url = dev.make_url(base_url, random_term)
    url = dev.make_url(target_url, time_random)
    data = dev.get_page(url, "json")

    EZAccess_url = base_url + data[0]['devtoolsFrontendUrl']
    page = dev.get_page(EZAccess_url, "html")
    dev.save_it(EZAccess_url, page)
    print(page.text)

if __name__ == '__main__':
    open_dev_tools()