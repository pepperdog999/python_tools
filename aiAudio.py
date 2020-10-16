# encoding:utf-8
import json
from urllib import request,parse

def get_token():
    API_Key = "DF2wS4DQ53TlS8ATxasy0ZXv"            # 官网获取的API_Key
    Secret_Key = "GvADiMXnwATEhaiKuOXg3t37KnKClGWr" # 为官网获取的Secret_Key
    #拼接得到Url
    Url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+API_Key+"&client_secret="+Secret_Key
    try:
        resp = request.urlopen(Url)
        result = json.loads(resp.read().decode('utf-8'))
        # 打印access_token
        print("access_token:",result['access_token'])
        return result['access_token']
    except request.URLError as err:
        print('token http response http code : ' + str(err.code))

def main():
    # 1、获取 access_token
    token = get_token()
    # 2、将需要合成的文字做2次urlencode编码
    TEXT = "陛下，我叫达拉崩吧斑得贝迪卜多比鲁翁！"
    tex = parse.quote_plus(TEXT)  # 两次urlencode
    # 3、设置文本以及其他参数
    params = {'tok': token,     # 开放平台获取到的开发者access_token
              'tex': tex,       # 合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字
              'per': 4,         # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
              'spd': 4,         # 语速，取值0-15，默认为5中语速
              'pit': 5,         # 音调，取值0-15，默认为5中语调
              'vol': 5,         # 音量，取值0-15，默认为5中音量
              'aue': 3,         # 下载的文件格式, 3为mp3格式(默认); 4为pcm-16k; 5为pcm-8k; 6为wav（内容同pcm-16k）
              'cuid': "7749py", # 用户唯一标识
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
    # 4、将参数编码，然后放入body，生成Request对象
    data = parse.urlencode(params)
    req = request.Request("http://tsn.baidu.com/text2audio", data.encode('utf-8'))
    # 5、发送post请求
    f = request.urlopen(req)
    result_str = f.read()
    # 6、将返回的header信息取出并生成一个字典
    headers = dict((name.lower(), value) for name, value in f.headers.items())
    # 7、如果返回的header里有”Content-Type: audio/wav“信息，则合成成功
    if "audio/mp3" in headers['content-type'] :
        print("tts success")
        # 合成成功即将数据存入文件
        with open("result.mp3", 'wb') as of:
            of.write(result_str)

if __name__ == '__main__':
    main()