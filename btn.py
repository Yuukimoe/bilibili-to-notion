from lib.bilibili_spider import biliSpider
from lib.save_to_notion import createPage
from lib.save_to_notion import allin
from lib.utils import convert_seconds_to_time, read_ini_config
import sys

def subsection_save(notion_database_id, notion_api_key, btv_paylist, debug=0):
    for i in range(0, len(btv_paylist)):
        page = "P" + str(btv_paylist[i]["page"])
        name = btv_paylist[i]["part"]
        time = convert_seconds_to_time(btv_paylist[i]["duration"])
        resp = createPage(databaseId=notion_database_id, token=notion_api_key, name=name, page=page, duration=time)
        if debug == 0:
            print(f'[{resp[0]}] {page}, {name}, {time}')
        else:
            print(f'[{resp[0]}] {page}, {name}, {time}, {resp[1]}')

def allin_save(notion_database_id, notion_api_key, btv_paylist, debug=0):
    for i in range(0, len(btv_paylist)):
        page = "P" + str(btv_paylist[i]["page"])
        name = btv_paylist[i]["part"]
        time = convert_seconds_to_time(btv_paylist[i]["duration"])
        resp = allin(databaseId=notion_database_id, token=notion_api_key, name=name, page=page, duration=time)
        if debug == 0:
            print(f'[{resp[0]}] {page}, {name}, {time}')
        else:
            print(f'[{resp[0]}] {page}, {name}, {time}, {resp[1]}')

if __name__ == '__main__':
    file_path = "config.ini"
    config = read_ini_config(file_path)

    notion_api_key = config['Notion']['notion_api_key']
    notion_database_id = config['Notion']['notion_database_id']

    if len(sys.argv) == 3 and sys.argv[2] == 'debug':
        debug = 1
    else:
        debug = 0

    if len(sys.argv) > 1:
        url = sys.argv[1]
        print("[INFO] URL: ", url)
        btv_paylist = biliSpider(url)
        if len(sys.argv) == 3 and sys.argv[2] == 'allin':
            allin_save(notion_database_id, notion_api_key, btv_paylist, debug)
        else:
            subsection_save(notion_database_id, notion_api_key, btv_paylist, debug)
    else:
        print("Example:\n"
              "> python3 btn https://bilibili.com/xxx\n"
              "> python3 btn https://bilibili.com/xxx allin")