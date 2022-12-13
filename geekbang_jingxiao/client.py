import os
from shutil import copyfile
import time

BASE_DIR = 'client/'
NET_DIR = 'net/'

def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print('downloading {} into locdisk...'.format(filename))
            copyfile(NET_DIR + filename, BASE_DIR + filename)
            os.remove(NET_DIR + filename) 
            # 我们需要删除这个文件，网盘会提我们同步这个操作，从而 server 知晓已完成
            print('downloaded {} into local disk.'.format(filename))
        time.sleep(3)

if __name__ == "__main__":
    main()
