import json, requests, codecs, time
import pandas as pd

def write_to_file(file_name, data):
    with codecs.open("./" + file_name, "a", "utf-8") as f:
        f.write(data)

def read_file(file_name):
    data = list()
    with codecs.open("./" + file_name, encoding='utf-8') as f:
        for line in f:
            result = line.rstrip('\r').rstrip('\n').split('\t')
            data.append(result)

    return data

def response(ticker, page_num):
    print(ticker, page_num)

    time.sleep(5)

    main_url = 'https://seekingalpha.com/api/v3/symbols/{0}/transcripts?id={0}&page[size]=50&page[number]={1}'
    response_text = requests.get(url=main_url.format(ticker, page_num), headers=headers).text
    json_response = json.loads(response_text)

    if page_num == 1:
        total_pages = json_response['meta']['page']['totalPages']

        for i in range(2, total_pages + 1):
            response(ticker, i)

    publishOn = ''
    title = ''
    links = ''

    for articles in json_response['data']:
        publishOn = articles['attributes']['publishOn']
        title = articles['attributes']['title']
        links = articles['links']['self']

        write_to_file('./articles_links.txt', '%s\t%s\t%s\t%s\n' % (ticker, publishOn, title, links))

headers = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'cookie': 'machine_cookie=4397208011929; _pprv={"consent":{"0":{"mode":"opt-in"},"1":{"mode":"opt-in"},"2":{"mode":"opt-in"},"3":{"mode":"opt-in"},"4":{"mode":"opt-in"},"5":{"mode":"opt-in"},"6":{"mode":"opt-in"},"7":{"mode":"opt-in"}}}; _pcid={"browserId":"l7hnvrk0k6wpdlva"}; __pat=-14400000; session_id=07697a1e-60c8-4f07-87f1-4006dce49a5e; user_id=48681666; user_nick=russian_guy2010; user_devices=1; u_voc=44; marketplace_author_slugs=; user_cookie_key=1c5kbnu; has_paid_subscription=false; user_perm=; sapu=101; user_remember_token=e9c43ed5921d366c110a2ca402d4a9b9575a0ce6; gk_user_access=1**1662571938; gk_user_access_sign=2d8e89fcaf1992528d5a1d63360ced8acf4f9ad2; pxcts=09b9bc9e-2ed3-11ed-b3c3-4a54764c7561; _pxvid=09b9aeb0-2ed3-11ed-b3c3-4a54764c7561; _sasource=; __tac=; __tae=1662571963924; LAST_VISITED_PAGE={"pathname":"https://seekingalpha.com/article/4461908-facebook-inc-fb-ceo-mark-zuckerberg-on-q3-2021-results-earning-call-transcript","pageKey":"6cec6c2a-742a-416d-8915-0faae0c93259"}; _pctx={u}N4IgDghg5gpgagSxgdwJIBMQC4QBsDsALvmABwB2YAblAJ4BsAVgPboBGIANCAK4DOMAE59s5Hrlzd+QgMqEIhfthARyzclxB8EhGBlHjcAXyA; __pvi={"id":"v-2022-09-08-09-44-21-168-I9yLlDK6zDuGXfcH-62b77c9904f8d4be970fc2fad5c9ab40","domain":".seekingalpha.com","time":1662651376414}; __tbc={kpex}L9BJfoJlsxU92bbMefDXzlfE46uyHUEnwyvxN1Ac_Nd0m1J1BLZiJc7xKbDOeKnC; xbc={kpex}7U3ogJCz-qcJS2lhvFzxt1PzipHTwrj51aUqALimTiIp-omNegRWXKocnStSWcYRemVK9MjWk4G7NV8wArgwZ34PSNV_lQhjgVL9CzHMOsjLZbbY9EZG2bau6UXTl875E0VOsfjwEW9FJcQapBp0AYh0eaWyIAFf2eHOYIlACSA8lzYZoNFBUgqbtkOBbghJ1jtRHdw0l8ofD3ZCrWLB5NkNRSHMzFNyYMCZe7R6_VXtVqOt1KJWC1c3AZo-X8fr971m8imQD0JcUghlN0qZjwGfuj1tcdybY_4X3jfY97qqCsk7lT2K2Fvz1ea-khxDfsc2dWQ-uq7pbeHBtwZ_YY89a_wBuQp2G26A6SWP8p7RpRxNHeUOAYpe76g5qkgUu2LSWtCQ03pIZa39EeEfzJ31UZpHjD3ZjWqo8K-Tc__iWHfR-9jChyU9HJynswDAQ5jDCW9QjnnzhKrGYAcjP0MN9tw-SwB4A-I5JN_y-1bsXnY2T8sgFDIa900Vi6rHSOnt_rum-59eN076xRhXD2XuP9Vu5jz98Pifa3Ax6sysQ4d9kmJ3hntgmzZN7FrvlCsax8EhKu3xQJObmTQlY32rMte_K-VJv_qx1yuLZPXSo5ZFP6jyAr34Q0IIvJs751cRdoFZ5o7byW5cQA6WylzFO1XVYZcSYYZfMvZ1ghYUlXkB1ACwGZByp-CIQSxF2a133CmKVMGgP8m3EmTXMr5NRgXq-imsUuLx11q2WW49yPT_40HoEh2RvPs_d4IK',
    'Host': 'seekingalpha.com'
}

stock_tickers = pd.read_csv('./SP500 Data.csv')

for index, row in stock_tickers.iterrows():
    ticker = row['Tickers']

    try:
        response(ticker, 1)
    except:
        pass