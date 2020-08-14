from urllib import request

import re

Name = r'<h3 class="event-title"><a href=".*">(.*)</a></h3>'  # 匹配名称的正则

Location = r'<span class="event-location">(.*)</span>'  # 匹配地点的正则

Time = r'<time datetime=".*">(.*)<span class="say-no-more">'  # 匹配时间的正则

Year = r'<span class="say-no-more">(.*)</span></time>'  # 匹配年份


def main():
    URL = 'https://www.python.org/events/python-events/'

    data = delInf(URL)


# 处理html内的信息并输出正则到的内容

def delInf(URL):
    datalist = []

    strInf = request.urlopen(URL).read().decode('utf-8')  # 整个网页的信息采用utf-8的编码格式来

    name = re.findall(Name, strInf)  # 正则匹配内容，返回所有匹配到的项，返回的是一个列表形式

    location = re.findall(Location, strInf)

    time = re.findall(Time, strInf)

    year = re.findall(Year, strInf)

    for index in range(0, len(name)):
        print('会议名称:' + name[index])

        print('会议地点:' + location[index])

        print('会议时间:' + time[index].replace('&ndash;', '-'))  # 由于特殊字符的存在，这里要替换一下

        print('会议年份:' + year[index] + '\n')


if __name__ == '__main__':
    main()
