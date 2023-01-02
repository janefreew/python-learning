# task  eventloop
# 假设任务只有两个状态：一是预备状态；二是等待状态
# 所谓的预备状态，是指任务目前空闲，但随时待命准备运行。
# 等待状态，是指任务已经运行，但正在等待外部的操作完成，比如 I/O 操作。
# event loop 会维护两个任务列表，分别对应这两种状态；


import asyncio
import aiohttp
import time

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))

async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)

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
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()
