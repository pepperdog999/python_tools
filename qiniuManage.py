# -- coding: utf-8 --
from qiniu import Auth
from qiniu import BucketManager

access_key = 'YvcreQyhOcIxMKl4zTTCPzQemJli1KQ62DMQLG0F'
secret_key = 'kOU3HABHe-KJmca35LtR2jd6VsS_aisA7PHeczAy'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
# bucket_name = 'sagacity'
bucket_name = 'sctse-base'

# 前缀
prefix = None
# 列举条目
limit = 1000
# 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
delimiter = None
# 标记
marker = ''
ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)

# for i in ret['items']:
#     print i

#按文件类型删除
# for i in ret['items']:
#     key = i['key']
#     print i['fsize']
#     if key.split('.')[1] == 'mp4':
#         print(key)
#         ret, info = bucket.delete(bucket_name, i['key'])

#按文件大小删除
for i in ret['items']:
    key = i['key']
    if i['fsize'] > 1024*64: #KB
        print(key)
        ret, info = bucket.delete(bucket_name, i['key'])