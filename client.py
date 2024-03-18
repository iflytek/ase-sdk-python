from datetime import datetime
from urllib import parse
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time
from time import mktime
from hashlib import sha256
import hmac
import base64
import websocket
import requests

media_type_list = ["text", "audio", "image", "video"]

# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


class Client:
    def __init__(self, appid, apikey, api_secret, endpoint, uri):
        self.appid = appid
        self.apikey = apikey
        self.api_secret = api_secret
        self.endpoint = endpoint
        self.uri = uri

    def once(self, body, headers):
        return requests.post(url=self.build_signed_url(self.endpoint, self.uri), data=body, headers=headers)
    
    def stream(self, on_open, on_message, on_error=on_error):
            url = self.build_signed_url(self.endpoint, self.uri, 'GET')
            self.ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error)
            self.ws.run_forever()
    
    def build_signed_url(self, endpoint, uri, method='POST'):
        url_result = parse.urlparse(endpoint+uri)
        date = format_date_time(mktime(datetime.now().timetuple()))
        signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(url_result.hostname, date, method, url_result.path)
        signature_sha = hmac.new(self.api_secret.encode('utf-8'), signature_origin.encode('utf-8'),digestmod= sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        self.apikey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        values = {
            "host": url_result.hostname,
            "date": date,
            "authorization": authorization
        }
        return endpoint + uri + "?" + urlencode(values)