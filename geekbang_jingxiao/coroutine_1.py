
import asyncio
import time
def my_profile(func):
    def wrapper(url):
        starttime = time.time()
        func(url)
        endtime = time.time()
        du = endtime -starttime
        return du        
    return wrapper

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
# @my_profile
async def main(urls):
    for url in urls:
        await crawl_page(url)
        
starttime = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
endtime = time.time()
du = endtime -starttime
print('du is {}'.format(du))
