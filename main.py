# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
import requests
import xlwt
import pymysql
from bs4 import BeautifulSoup
from lxml import etree

def get_html(url):
    headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",}
    data_pre = {
            "cityId": "2",
            "platform": "online",
            "pageID": "102001",
            "head": {
                "Version": "",
                "userRegion": "CN",
                "Locale": "zh-CN",
                "LocaleController": "zh-CN",
                "TimeZone": "8",
                "Currency": "CNY",
                "PageId": "102001"}
    }


    response = requests.post(url, data=json.dumps(data_pre)).text
    response = json.loads(response)
    print(response)
    return response

def xpath_data(html):
    hotel_list = html["ResponseStatus"]["Response"]["hotels"]
    print(hotel_list)
    return hotel_list
def save_data():
    pass
def main():
    url="https://m.ctrip.com/restapi/soa2/21881/getRecommendHotels"
    first_html=get_html(url)
    div_list=xpath_data(first_html)




# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

