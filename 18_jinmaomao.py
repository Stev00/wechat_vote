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
        'lt': 'wFqDDE1%203hbItdw0ZZjupkBg75kxLXez1cXqa8BL2bPiM6TIsKqSMT9JcN9ujlU15jUgc2IJvVzum%20Y5W6iRpaXUIjShP6wSSaSzb2dHg5TMNpKiwcCmGNTeoW4XviET', \
        'cwb':'C1NEbxF4bTPp%208kVDarwKdQGhwqw1FhTAtzfejFEzJr2eDVfQzq8liOIBs9ct6RsZrwkGPVMZZzjhP4tsPZvOEdlOA6vEsRWmw4n13J6xopPplXJ6X6rqg9VhtG8/MPn',\
        'cg': 'VtBAuJvv0SwnbDQuDR5L03STbHTSiVUis9qm9RdFP520rZI6jfFa7NXLGrxmNtwFeLpnydp96515oSTyxE%20E79TFF1SbrYLIyLzBfUkzRnN1baKKOKy45mh75SM7oZdE',\
        'lj': 'lfAd75LZq3/08ZqsIWgtbIDYJHYg47I5GwDiIiaytqXdPKTsmXDCx3TFCUUWxdsYVcNC5kg2clhC/GCZtjcn2KWI4c9h%206efwZSRQnD/%20EUNmraJNYJoTOk3UJY6J5cA',\
        'phy':'QwGabM0M6HWKJNzjHOqOCch/dUzrxZWDKrYlfDH9wtW5iJvwZqWoc54M%20gK0NS3WzKQ0Y66g9XGhyvngOqiB3MoWx22leRwIqRGNTO7pQogtBCOmAcd0uPYFrWj5mVi2',\
        'lhw':'klfG9nv3s0yKJ3k/Lpd513jj1RoirzJDga9it8oVcJrYwoZPb1pwUZgS9RvbuLmE7HDluKV1%20cz4kAvmvsc%20jFEgAFIInMGLNgTCkEtd3FnPQQVR6A2JNZ2kvqwDTM3x',\
        'zwj':'M0UmhmZ135BfZmaH1Wsr1P7KY7BWUJ7q01v3ba8Hwqyn1q/o%20vphTMkerVeOSJz7PuHvhbnr4i4ipJsms6G5bL53I/Qbbysd38cFfAzfoIJOzQbjUWYHpxsBz0LwkCtV',\
        'qwq':'xJfdT8hKSa0swVeTi0fEcVRoRG8b0LU%20zVdDFtA4oXX5SSQWon4U6rAaJPIskr9jf3F3OoOaSOJQ%20GJM314Nn1ENluv2wo100tG/9W0Nmd%20rz7Ov4Mdh9ztzqfuVusP8',\
        'cz': 'nY2gxoT7z%205fckN/aD5Or3GL3OA6IRw4nBHfepwQwtVD3k4FhDcMsAUUmMhjHSftuWG3yH5GRRCk9xWEd0yr253f/K3RxLqH54o3XAGcPC%209dZb8Mp0C34l3qkHtkbAx',\
        '01': 'G2IIMw6f8EIImjCA0mPelSO16VZvzyexn6cl1UyFpeetb%20B6KQ494mHy7mS4fPxCcX9lWpj3PskW7MfPF8oxu6M/EJsuHUilRqT/W9J0J3x58skJUBBepwXUhZGeLBQa',\
        '02': 'NHC01IrXa0mJI4w2RcydC16tl/XeKiZMhtwZDVkehF7KPrbwoukCbvZjJQsQLDSLs11nZFOd%201Pj8/uzBuEfpb3I35S3VZumE8dlGZ0PvU/REAntloAUXwwssCXyujJG',\
        '03': 'iZyz9jtCq87Lgu2SeRBIzsZ4Ql3lUet9loY74zCg%20JF7JRjNYc/6xDOJ31GeTSv41W/%20wY1yotoA6uQho1xp6krGGduRhGqOy42dT3nROwbJrZjc/WFCXLAF5RtXmeNy',\
        'cmh':'qeGksRchqjRqLNmzl6XmW3DpXXyyu080iTlcUHKqtPZH3ecAkGphV5Y8PSnQkMcXL%20lDSgr/uHKod9%20yhwcjVApr0PDskgfZVQbbnZyvAvwwkol/yPAtIOM63TWFINUQ',\
        'lhf':'rUcAB0Pr6BjuLOS5Jra3rKfuJgG7KwvyCPH5TGnl1aUhTXWquQltfvMWNByQAql/Rh2r0zmocxoNdcdTaI85pQEvw2LFD21v70qnFOvlr2b87S5477WdoMCfGKcK8RXv',\
        'zxh':'KLtHPBxFon7axefdwMYSW0ns6rhS2tcH5afa0ExQCesCUqOe6MfeBghUh0/pWn7pE%204/r3NUyi52Qo1Ha9UmVkiN8/ysLDPsY5zXpmGSlJm0eIW/X3gQ/k6xC7vZRhYj',\
        'gh': '7B3%20Fm%202FmdyKX5aOVF1fyq9x30W2FcUHCwJKSMXLtbNreMUr/i6LbllmTjs8bmlgdqPzb7u3t0hpZz3E%20QWj8F17VXLuPcYg6EZIFZqQAYAvfs6bd/xKSAdmd%20rKnxr',\

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
    print('\n\n\n等待', random_sleep_time(3), '秒再刷')
    
    time.sleep(random_sleep_time(3))
