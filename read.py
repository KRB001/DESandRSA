import csv
from convert import *

class TableReader():

    def __init__(self):
        self.name = "Google Scraper"
        self.message = ""
        self.key = ""
        self.pc1 = []
        self.pc2 = []
        self.s_tables = []
        self.c_d_shifts = []
        self.ip = []
        self.e = []
        self.p = []
        self.ip1 = []

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

        for i in range(8):
            with open('tables/s' + str(i+1) + '.csv', newline='') as file:
                s = []
                reader = csv.reader(file)
                for row in reader:
                    s.append(row)
                self.s_tables.append(s)

        with open('tables/p.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.p.append(row)

        with open('tables/ip-1.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ip1.append(row)

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

    def get_p(self):
        return self.p

    def get_ip1(self):
        return self.ip1

    def get_s_tables(self):
        return self.s_tables

    def get_c_d_shifts(self):
        return self.c_d_shifts

    def get_message(self):
        return self.message