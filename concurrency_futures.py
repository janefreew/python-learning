
import concurrent.futures
import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
            
        for future in concurrent.futures.as_completed(to_do):
            future.result()
def main():
    sites = [
        'https://baike.baidu.com/item/Microsoft%20Windows/3304184?fromModule=lemma_inlink&fromtitle=windows&fromid=165458',
        'https://baike.baidu.com/item/Windows%20Server/271508?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8/100571?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA/140338?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E5%B5%8C%E5%85%A5%E5%BC%8F%E8%AE%A1%E7%AE%97%E6%9C%BA/693492?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E4%B8%93%E7%94%A8%E8%AE%A1%E7%AE%97%E6%9C%BA/4201208?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E7%A8%8B%E5%BA%8F/8800242?fromModule=lemma_inlink',
        'https://baike.baidu.com/item/%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80/1379708?fromModule=lemma_inlink'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()

