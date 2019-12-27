import abc
import os
import hashlib
import threading


class IRunner:
    @abc.abstractmethod
    def Run(self):
        pass


class IPrinter:
    @abc.abstractmethod
    def Print(self):
        pass


class ConsolePrinter(IPrinter):
    def Print(self, str):
        print(str)


class DuplicateFinder(IRunner):
    blockSize = 512

    def FindDuplicate(self):
        path = "F://"
        listOfFolders = self.FindFolders(path)
        threads = []
        for i in range(listOfFolders.__len__()):
            thread = threading.Thread(target=self.FindDuplicatesInFolder(listOfFolders[i]))
            threads.append(thread)
            thread.start()
        for i in threads:
            i.join()

    def FindDuplicatesInFolder(self, path):
        hashes = {}
        for root, directories, files in os.walk(path):
            for name in files:
                self.path = os.path.join(root, name)
                filehash = self.HashFile(self.path)
                hashes[filehash].append(self.path)
        duplicate_files = []
        for k, v in hashes.items():
            if list(hashes.values()).count(v) > 1:
                duplicate_files.append(k)

    def HashFile(self, path):
        try:
            with open(path, 'rb') as file:
                md5_hash = hashlib.md5()
                chunk = file.read(self.blockSize)
                while chunk:
                    md5_hash.update(chunk)
                    chunk = file.read(self.blockSize)
                    return md5_hash.hexdigest()
        except PermissionError as e:
            return e

    def FindFolders(self, path):
        folders = []
        for r, d, f in os.walk(path):
            for folder in d:
                folders.append(os.path.join(r, folder))
        return folders

    def Run(self):
        self.FindDuplicate()


if __name__ == '__main__':
    a = DuplicateFinder()
    a.Run()
