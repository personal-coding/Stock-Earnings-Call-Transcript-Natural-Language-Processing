import requests, codecs, time
from lxml import etree
import pandas as pd
import os.path

def write_to_file(file_name, data):
    with codecs.open("./" + file_name, "w", "utf-8") as f:
        f.write(data)

def read_file(file_name):
    data = list()
    with codecs.open("./" + file_name, encoding='utf-8') as f:
        for line in f:
            result = line.rstrip('\r').rstrip('\n').split('\t')
            data.append(result)

    return data

def response(article):
    print(article)

    time.sleep(1)

    main_url = 'https://seekingalpha.com{0}'
    response_text = requests.get(url=main_url.format(article), headers=headers).text
    tree = etree.HTML(response_text)

    final_text = ''

    for paragraph in tree.xpath("//div[@data-test-id='article-content']//p"):
        final_text += ''.join(paragraph.itertext()) + '\n'

    write_to_file('.' + article + '.txt', final_text)

headers = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'cookie': '_sasource=; session_id=252127c0-f660-43a1-9ec8-cc600d61806a; machine_cookie=4397208011929; _pprv={"consent":{"0":{"mode":"opt-in"},"1":{"mode":"opt-in"},"2":{"mode":"opt-in"},"3":{"mode":"opt-in"},"4":{"mode":"opt-in"},"5":{"mode":"opt-in"},"6":{"mode":"opt-in"},"7":{"mode":"opt-in"}}}; _pcid={"browserId":"l7hnvrk0k6wpdlva"}; __pat=-14400000; user_id=48681666; user_nick=russian_guy2010; user_devices=1; u_voc=44; marketplace_author_slugs=; user_cookie_key=1c5kbnu; has_paid_subscription=false; user_perm=; sapu=101; user_remember_token=e9c43ed5921d366c110a2ca402d4a9b9575a0ce6; pxcts=09b9bc9e-2ed3-11ed-b3c3-4a54764c7561; _pxvid=09b9aeb0-2ed3-11ed-b3c3-4a54764c7561; _sasource=; gk_user_access=1**1662671240; gk_user_access_sign=d1f4ec9011b95c429122e97a95318cc899ee614b; xbc={kpex}oT8V1U7iFe7hpRD4GWbYrGdxhqYSkCjh5CDfaA_R-t_NUFp-RU7zKtQYJk4V-9v-4Lg2gFbQSqDAhPsPoSHw3bhmriRUjj_XC-p5sKncXiHMR4Jsqjgk5mHEMQ1IkT-pA8cGcTi__CJGWdRfSwheUh1tFX7v5AoY2Z_gJ22BTgM8lzYZoNFBUgqbtkOBbghJPHsktcC0HwsMCrBXJIDZczKqgObCKs2mkXUDQHUFh33tVqOt1KJWC1c3AZo-X8fr2cb3teJDeTW9r_bgmQZ0RgGfuj1tcdybY_4X3jfY97rh0wnjKcxRoEQobC8bLl7Kfsc2dWQ-uq7pbeHBtwZ_YY89a_wBuQp2G26A6SWP8p7RpRxNHeUOAYpe76g5qkgUu2LSWtCQ03pIZa39EeEfzJ31UZpHjD3ZjWqo8K-Tc__iWHfR-9jChyU9HJynswDAQ5jDCW9QjnnzhKrGYAcjP0MN9tw-SwB4A-I5JN_y-1bsXnY2T8sgFDIa900Vi6rHSOnt_rum-59eN076xRhXD2XuP9Vu5jz98Pifa3Ax6sysQ4d9kmJ3hntgmzZN7FrvlCsax8EhKu3xQJObmTQlY32rMte_K-VJv_qx1yuLZPXSo5ZFP6jyAr34Q0IIvJs751cRdoFZ5o7byW5cQA6WylzFO1XVYZcSYYZfMvZ1ghYUlXkB1ACwGZByp-CIQSxF2a133CmKVMGgP8m3EmTXMr5NRgXq-imsUuLx11q2WW49yPT_40HoEh2RvPs_d4IK; session_id=6370d439-b997-455d-83b6-d79d7d5bff1c; LAST_VISITED_PAGE={"pathname":"https://seekingalpha.com/","pageKey":"ecbd1da5-31d6-4a6f-ad47-e9aa800696ad"}; _pctx={u}N4IgDghg5gpgagSxgdwJIBMQC4QBsDsArggG7IAMALGAMY0AcJElNIANCIQM4wBOX2AHaFcuDtz4BlAC4Rp3bCAiCA9oPYguCaTAxCRuAL5A; __pvi={"id":"v-2022-09-09-08-37-08-555-09bHVrbwyN6f8b6o-a0d682c333a84b455511e31242b21873","domain":".seekingalpha.com","time":1662730628555}; __tac=; __tae=1662730628721; __tbc={kpex}L9BJfoJlsxU92bbMefDXzlfE46uyHUEnwyvxN1Ac_Nd0m1J1BLZiJc7xKbDOeKnC',
    'Host': 'seekingalpha.com'
}

stock_tickers = pd.read_csv('./earnings_to_search.csv')

for index, row in stock_tickers.iterrows():
    article = row['article']

    try:
        if not os.path.isfile('.' + article + '.txt'):
            response(article)
    except:
        pass