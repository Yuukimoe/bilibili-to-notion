import requests, json


def createPage(databaseId, token, name, page, duration):
    createUrl = 'https://api.notion.com/v1/pages'

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Page": {
                "rich_text": [
                    {
                        "text": {
                            "content": page
                        }
                    }
                ]
            }
            ,
            "Duration": {
                "rich_text": [
                    {
                        "text": {
                            "content": duration
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)
    status_code = res.status_code
    resp_text = res.text
    return status_code, resp_text

def allin(databaseId, token, name, page, duration):
    createUrl = 'https://api.notion.com/v1/pages'

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": f'{page}. {name}, {duration}'
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)
    status_code = res.status_code
    resp_text = res.text
    return status_code, resp_text
