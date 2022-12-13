import os
from shutil import copyfile
import time

BASE_DIR = 'server/'
NET_DIR = 'net/'

def main():
    filenames = os.listdir(BASE_DIR)
    for i, filename in enumerate(filenames):
        print('copying {} into net drive...  {}/{}'.format(filename, i + 1, len(filenames)))
        copyfile(BASE_DIR + filename, NET_DIR + filename)
        print('copied {} into net drive, waiting client complete...  {}/{}'.format(filename, i + 1, len(filenames)))

        while os.path.exists(NET_DIR + filename):
            time.sleep(3)

    print('transferred {} into client.  {}/{}'.format(filename, i + 1, len(filenames)))

if __name__ == "__main__":
    main()