import logging


class FileHandlerByHttp:
    logging.basicConfig(filename="fileExceptionLogger", level=logging.INFO)

    def fileDownload(self, url):
        try:
            from urllib.request import urlopen
            response = urlopen(url)
            html = response.read().decode('utf-8')
            inputStringToTextFile = str(html)
            dataInStrings = inputStringToTextFile.split('\\n')
            fileObjectSave = open('dataFile.txt', 'w')
            fileObjectSave.writelines(dataInStrings)
            fileObjectSave.close()
            return fileObjectSave.name
        except ReferenceError as e:
            print("Bad connection reference")
            logging.exception(e)
        except Exception as e:
            print("Unexpected error:")
            logging.exception(e)

    def fileIterator(self, fileName):
        with open(fileName) as file:
            for line in file:
                line = str(line).lower().strip('\n').split(' ')
                yield line

    def wordCounter(self, generator, fileName):
        countOfWord = 0
        for line in generator(fileName):
            countOfWord += len(line)
        return countOfWord

    def wordStatsGetter(self, generator, fileName):
        lib = dict()
        for line in generator(fileName):
            for iterator in line:
                if not iterator in lib:
                    lib[iterator] = 1
                else:
                    lib[iterator] += 1
        return lib


if __name__ == '__main__':
    urlFile = input()
    httpHandler = FileHandlerByHttp()
    file = httpHandler.fileDownload(urlFile)
    httpHandler.wordCounter(httpHandler.fileIterator, file)
    httpHandler.wordStatsGetter(httpHandler.fileIterator, file)