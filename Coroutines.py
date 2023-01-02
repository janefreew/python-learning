
import time

# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))

# def main(urls):
#     for url in urls:
#         crawl_page(url)

# main(['url_1', 'url_2', 'url_3', 'url_4'])


import asyncio

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     for url in urls:
#         await crawl_page(url)

# start_time = time.perf_counter()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end_time = time.perf_counter()

# print('in {} seconds'.format( end_time - start_time))


# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     for task in tasks:
#         await task
# start_time = time.perf_counter()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end_time = time.perf_counter()

# print('in {} seconds'.format( end_time - start_time))




# import asyncio

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     await asyncio.gather(*tasks)
# start_time = time.perf_counter()

# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end_time = time.perf_counter()
# print('in {} seconds'.format( end_time - start_time))

# ########## 输出 ##########




import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')

asyncio.run(main())



import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

asyncio.run(main())  # 1 程序进入 main() 函数，事件循环开启；

