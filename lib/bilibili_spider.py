import requests
from bs4 import BeautifulSoup
import json

def get_json_from_url(url):
    """
    :param url: 传入包含视频合集的 URL
    :return: 返回获取的视频 JSON 列表
    """
    # 发送HTTP请求获取页面内容
    response = requests.get(url)
    html = response.text

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 找到<script>标签
    script_tags = soup.find_all('script')

    # 遍历所有<script>标签
    for script_tag in script_tags:
        # 找到包含window.__INITIAL_STATE__变量的<script>标签
        if 'window.__INITIAL_STATE__' in script_tag.text:
            # 提取JSON数据
            json_start = script_tag.text.find('{')
            json_end = script_tag.text.rfind('}') + 1
            json_data = script_tag.text[json_start:json_end]

            # 去除末尾的多余字符
            json_data = json_data.replace(";(function(){var s;(s=document.currentScript||document.scripts[document.scripts.length-1]).parentNode.removeChild(s);}", "")

            # 返回JSON数据
            return json_data

    # 如果未找到目标数据，返回None或者抛出异常，根据你的需求来决定
    return None

def get_pages_from_json(json_data):
    """
    :param json_data: 传入获取到的 JSON 列表
    :return: 原始的 pages 信息
    """
    # 解析JSON数据
    data = json.loads(json_data)

    # 获取videoData中的pages内容
    video_data = data['videoData']
    pages = video_data['pages']

    return pages

def biliSpider(url):
    json_data = get_json_from_url(url)

    if json_data is not None:
        # 在这里对json_data进行处理，如解析JSON、提取所需信息等
        # 这里只是简单打印JSON数据
        # print(json_data)
        pages = get_pages_from_json(json_data)
        return pages
    else:
        return None
