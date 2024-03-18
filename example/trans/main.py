import json
import base64
import sys
sys.path.append("../..")
import client

APPId = "4CC5779A"
APIKey = "94a179ef19bd9f8c5c5a3ac1060016f7"
APISecret = "HY7xfGGKO3ilByAE9MHDGS9ByvsNg0gO"

txt = base64.b64encode('你好!'.encode()).decode()
	
body =  {
    "header": {
        "app_id": APPId,
        "status": 3
    },
    "parameter": {
        "its": {
            "from": "cn",
            "to": "en",
            "result": {}
        }
    },
    "payload": {
        "input_data": {
            "encoding": "utf8",
            "status": 3,
            "text": txt
        }
    }
}


headers = {'content-type': "application/json", 'host':'itrans.xf-yun.com', 'app_id':APPId}

cli = client.Client(APPId, APIKey, APISecret, "https://itrans.xf-yun.com", "/v1/its")
resp = cli.once(body=json.dumps(body), headers=headers)

obj = json.loads(resp.content)
text = base64.b64decode(obj['payload']['result']['text'].encode()).decode()
print(text)