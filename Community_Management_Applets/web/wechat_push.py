import lxml.html
import requests
import re
# 广场热门活动页面中通过推送链接展示推送


# 获取推送的标题和展示图
def getArticleHead(url):
    html = requests.get(url).content
    html = html.decode('utf-8')
    # 标题
    msg_title = re.findall(r'var msg_title = \"(.*?)\"',html)[0]
    # 推文首页图
    msg_cdn_url = re.findall(r'var msg_cdn_url = \"(.*?)\"',html)[0]
    print("title:"+msg_title)
    print("msg_url:"+msg_cdn_url)


# 获取文章内容
def getArticle(url):
    html = requests.get(url).content
    html = html.decode('utf-8')
    return html


if __name__ == '__main__':
    getArticleHead("http://mp.weixin.qq.com/s/yxKf-ce509DJs6MyZ5Uvug")