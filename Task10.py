import os
from urllib import request
from threading import Thread


class DownloadFilesWithUrl(Thread):
    def __init__(self, url, number):
        Thread.__init__(self)
        self.number = number
        self.url = url

    def run(self):
        fileRequestToOpen = request.urlopen(self.url)
        fileName = os.path.basename(self.url)
        blockSize = 1024 * 2
        with open(fileName, "wb") as handler:
            while True:
                fileInfo = fileRequestToOpen.read(blockSize)
                if not fileInfo:
                    break
                handler.write(fileInfo)
        print(f"Thread {self.number} finished to download {self.url}")


if __name__ == "__main__":
    print("Type your url to download file: ")
    urls = input()
    thread1 = DownloadFilesWithUrl(urls, 1)
    thread1.start()
    thread2 = DownloadFilesWithUrl(urls, 2)
    thread2.start()
