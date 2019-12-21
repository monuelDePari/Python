import sqlite3
import abc
import turtle

"""Single Responsibility Principle, simple logger writes and reads exception messages"""


class LoggerFile:

    def readLog(self):
        logMessage = open("log.txt", "r")
        print(logMessage.read())

    def writeLog(self, exceptionMessage):
        logMessage = open("log.txt", "a")
        logMessage.write(exceptionMessage)
        logMessage.close()


"""Open-Closed Principle"""


class Logger():

    def __init__(self):
        pass

    def readLog(self):
        pass

    def writeLog(self, exceptionMessage):
        pass


class LoggerFile(Logger):

    def __init__(self):
        logMessage = open("log.txt", "x")
        logMessage.close()

    def readLog(self):
        logMessage = open("log.txt", "r")
        print(logMessage.read())

    def writeLog(self, exceptionMessage):
        logMessage = open("log.txt", "a")
        logMessage.write(exceptionMessage)
        logMessage.close()


class DBLogger(Logger):

    def __init__(self):
        connectionString = sqlite3.connect("mydatabase.db")
        connection = connectionString.cursor()
        connection.execute("""CREATE TABLE LOG (logMessage text)""")
        connectionString.commit()
        connection.close()

    def readLog(self):
        connectionString = sqlite3.connect("mydatabase.db")
        connection = connectionString.cursor()
        connection.execute("""SELECT * FROM LOG""")
        print(connection.fetchall())
        connectionString.commit()
        connection.close()

    def writeLog(self, exceptionMessage):
        connectionString = sqlite3.connect("mydatabase.db")
        connection = connectionString.cursor()
        connection.execute("""INSERT INTO LOG (logMessage text) VALUES %s""" % exceptionMessage)
        connectionString.commit()
        connection.close()


"""Liskov Substitution Principle, we can substitute at GamingMouse either PCMouse class or OfficeMouse class"""


class PCMouse:
    def definePosition(self):
        pass

    def movePosition(self):
        pass


class OfficeMouse(PCMouse):
    def definePosition(self):
        pass

    def movePosition(self):
        pass

    def movePreviousPage(self):
        pass

    def moveNextPage(self):
        pass


class GamingMouse(OfficeMouse):
    def definePosition(self):
        pass

    def movePosition(self):
        pass

    def movePreviousPage(self):
        pass

    def moveNextPage(self):
        pass

    def bindKey(self):
        pass


"""Interface Segregation Principle"""


class ICircleDraw(abc.ABC):
    @abc.abstractmethod
    def Draw(self, radius):
        pass


class IRectangleDraw(abc.ABC):
    @abc.abstractmethod
    def Draw(self, width, height):
        pass


class CircleDraw(ICircleDraw):
    def Draw(self, radius):
        t = turtle.Turtle()
        t.circle(radius)


class RectangleDraw(IRectangleDraw):
    def Draw(self, width, height):
        row = width * '*'
        for a in range(height):
            print(row)


"""DI"""


class Printer:
    def fetch_remote_data(self):
        print('Printer called')
        return 1


class PC:
    def __init__(self, printer: Printer):
        self.printer = printer

    def do_stuff(self):
        printer_result = self.printer.fetch_remote_data()
        print(f'the printer returned a result: {printer_result}')
        # do something with the data and return a result


def Run():
    printer = Printer()
    logic = PC(printer=Printer)

    print(logic.do_stuff())
