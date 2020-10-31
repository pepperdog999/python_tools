# -- coding: utf-8 --
import upyun
from sys import argv
import os
import json

kwargs = { 'allow-file-type': 'jpg,jpeg,png,py' }
def upload():
    base_url = 'http://ideas-img.test.upcdn.net/'
    bucket = 'ideas-img'
    username = 'pepperdog'
    password = 'LaLgJL011a2ef6l3AuceoEU8SdrjxbdK'
    # #构建鉴权对象
    up = upyun.UpYun(bucket, username, password)
    file = './uploader_youpai_sdk.py'
    path = 'img/'
    urls = list()

    key = path + file.split("/")[-1]
    with open(file, 'rb') as f:
        ret = up.put(key, f, checksum=True, form=True, **kwargs)
        print ret
        print base_url+ret['url']

    # #要上传文件列表
    # for f in argv[1:]:
    #     if not (os.path.exists(f)):
    #         print ('文件不存在！')
    #         exit(-2)
    #     #上传后保存的文件名
    #     key = path + f.split("/")[-1]
    #     with open(path, 'rb') as f:
    #         res = up.put(key, f, checksum=True, headers=headers)
    #         print res
    #     # if (ret == None):
    #     #     print ("上传失败！")
    #     #     exit(-1)
    #     # else:
    #     #     urls.append(base_url + ret['key'])
    #
    # print('Upload Success:')
    # for url in urls: print(url)

if __name__ == "__main__":
    upload()
    # if len(argv) < 2:
    #     print("参数错误！")
    # else:
    #     upload()