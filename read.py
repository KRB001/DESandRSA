import csv
from convert import *

class TableReader():

    def __init__(self):
        self.name = "Google Scraper"
        self.message = ""
        self.key = ""
        self.pc1 = []
        self.pc2 = []
        self.c_d_shifts = []
        self.ip = []
        self.e = []

        with open('tables/pc1.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.pc1.append(row)

        with open('tables/pc2.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.pc2.append(row)

        with open('tables/ip.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ip.append(row)

        with open('tables/e.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.e.append(row)

        with open('tables/sample_key.txt', newline='') as file:
            self.key = file.read()
            self.key = ascii_to_binary(self.key)

        with open('tables/message.txt', newline='') as file:
            self.message = file.read()
            self.message = ascii_to_binary(self.message)

        with open('tables/shifts.txt', newline='') as file:
            self.c_d_shifts = file.read()

    def get_key(self):
        return self.key

    def get_pc1(self):
        return self.pc1

    def get_pc2(self):
        return self.pc2

    def get_ip(self):
        return self.ip

    def get_e(self):
        return self.e

    def get_c_d_shifts(self):
        return self.c_d_shifts

    def get_message(self):
        return self.message