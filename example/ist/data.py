APPId = "4CC5779A"
APIKey = "94a179ef19bd9f8c5c5a3ac1060016f7"
APISecret = "HY7xfGGKO3ilByAE9MHDGS9ByvsNg0gO"

class Request:
    def __init__(self, header, parameter, payload):
        self.header = header
        self.parameter = parameter
        self.payload = payload

# 请求数据
request_data = {
	"header":{
		"app_id":"4CC5779A",
		"uid":"39769795890",
		"did":"SR082321940000200",
		"imei":"8664020318693660",
		"imsi":"4600264952729100",
		"mac":"6c:92:bf:65:c6:14",
		"net_type":"wifi",
		"net_isp":"CMCC",
		"status":0,
		"res_id":""
	},
	"parameter":{
		"iat":{
			"language":"en_us",
			"result":{
				"encoding":"utf8",
				"compress":"raw",
				"format":"json"
			}
		}
	},
	"payload":{
		"audio":{
			"encoding":"raw",
			"sample_rate":16000,
			"channels":1,
			"bit_depth":16,
			"status":0,
			"seq":0,
			"audio":"./resource/input/test.en.txt.pcm",
			"frame_size":0
		}
	}
}