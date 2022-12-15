
import asyncio
import time

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(3)
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
starttime = time.time()
asyncio.run(main())
endtime = time.time()
du = endtime -starttime
print('du is {}'.format(du))
