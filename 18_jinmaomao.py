#python3 win7
#utf-8

'this is voting program for Jinmaomao'

__author__ = 'zhangdansan'

import urllib.request
import urllib.parse
import time
import random
import string

#x = input('input something voting for jinmaomao:')

def random_sleep_time(digits_length):
    digits_char = string.digits
    need_sleep_time = ''
    for i in range(digits_length):
        need_sleep_time += random.choice(digits_char)
    return int(need_sleep_time)


while True:

    url = 'http://youchongyuan.voxverbi.com/youchongyuan/zan.php'

    open_id = {
        'zt': 'bDW3c2q8I0ponBhPE%20eEktmUIKgZZmZ0pSNusPk7Rfcut8qtR%20c7PUp6OO77uRmOW7lmUEhxdJxiByUtg2pO0TVzYV9PV1ABjJbCkBAn3w61TWTwI%20GnUot8xb%20Mdw%20B', \
        'ly': '/I1tHQT352Mynuvy97X9I8IA7OFtBGHSfsPmYZToAd62DGJUUjkf1mrCsXvRl4NxmxCwD7hPHbDviM6/Dz%201yUVBbFx7BStztLrdrck9NB%200Wg8TQPiPHDutSLxPfWg8', \
        
    }

    for run_open_id_keys in open_id.keys():
        print(run_open_id_keys)

        wechat_data = {'openid': open_id[run_open_id_keys], 'id': '672'}
        data = urllib.parse.urlencode(wechat_data).encode(encoding='UTF8')

        headers = {'Accept': 'application/json, text/javascript, */*; q=0.01', \
                   'Accept-Encoding': 'gzip, deflate', \
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4', \
                   'Content-Length': '162', \
                   'Content-Type': 'application/x-www-form-urlencoded', \
                   'Cookie': 'Hm_lvt_aa91084402006a7e6156f0d875606920=2178657970; Hm_lpvt_aa91084402006a7e6156f0d875606920=2178657970', \
                   'Host': 'youchongyuan.voxverbi.com', \
                   'Origin': 'http://youchongyuan.voxverbi.com', \
                   'Proxy-Connection': 'keep-alive', \
                   'Referer': 'http://youchongyuan.voxverbi.com/youchongyuan/home.html?\
                               openid='+open_id[run_open_id_keys]+'&state=1', \
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
                               54.0.2840.87 Safari/537.36', \
                   'X-Requested-With': 'XMLHttpRequest'}

        request = urllib.request.Request(url=url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        data = response.read().decode('UTF-8')
        print(data)
        print(time.ctime())
        next_people_time = random_sleep_time(2)
        print('等待', next_people_time, '秒刷下一人\n')
        time.sleep(next_people_time)

    print(time.ctime())
    next_turn_time = random_sleep_time(3)
    print('\n\n\n此轮结束，等待', next_turn_time, '秒刷下一波')
    
    time.sleep(next_turn_time)
