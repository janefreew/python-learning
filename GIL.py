# import time

# start_time = time.perf_counter()
# def CountDown(n):
#     while n > 0:
#         n -= 1

# end_time = time.perf_counter()
# print(' {} seconds'.format( end_time - start_time))




# from threading import Thread

# n = 100000000
# start_time = time.perf_counter()

# t1 = Thread(target=CountDown, args=[n // 2])
# t2 = Thread(target=CountDown, args=[n // 2])
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time = time.perf_counter()
# print(' {} seconds'.format( end_time - start_time))


# GIL，是最流行的 Python 解释器 CPython 中的一个技术术语。
# 它的意思是全局解释器锁，本质上是类似操作系统的 Mutex。
# 每一个 Python 线程，在 CPython 解释器中执行时，都会先锁住自己的线程，阻止别的线程执行。

# CPython 使用引用计数来管理内存，所有 Python 脚本中创建的实例，都会有一个引用计数，来记录有多少个指针指向它。
# 当引用计数只有 0 时，则会自动释放内存。


# 所以说，CPython 引进 GIL 其实主要就是这么两个原因：
# 一是设计者为了规避类似于内存管理这样的复杂的竞争风险问题（race condition）；
# 二是因为 CPython 大量使用 C 语言库，但大部分 C 语言库都不是原生线程安全的
# （线程安全会降低性能和增加复杂度）。

# 不同版本的 Python 中，check interval 的实现方式并不一样。




import threading



for i in range(500):
    n = 0

    def foo():
        global n
        n += 1
    threads = []
    for i in range(100):
        t = threading.Thread(target=foo)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(n)


    # 总的来说，你只需要重点记住，绕过 GIL 的大致思路有这么两种就够了：
    # 绕过 CPython，使用 JPython（Java 实现的 Python 解释器）等别的实现；
    # 把关键性能代码，放到别的语言（一般是 C++）中实现。