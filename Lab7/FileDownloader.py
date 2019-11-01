import logging


class FileHandlerByHttp:
    logging.basicConfig(filename="fileExceptionLogger", level=logging.INFO)

    @staticmethod
    def fileDownload(url):
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

    @staticmethod
    def fileIterator(fileName):
        with open(fileName) as file:
            for line in file:
                line = str(line).lower().strip('\n').split(' ')
                yield line

    @staticmethod
    def wordCounter(generator, fileName):
        countOfWord = 0
        for line in generator(fileName):
            countOfWord += len(line)
        return countOfWord

    @staticmethod
    def wordStatsGetter(generator, fileName):
        lib = dict()
        for line in generator(fileName):
            for iterator in line:
                if not iterator in lib:
                    lib[iterator] = 1
                else:
                    lib[iterator] += 1
        return lib
