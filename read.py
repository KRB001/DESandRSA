import csv
from convert import *

class TableReader():

    def __init__(self):
        self.name = "Google Scraper"
        self.key = []
        self.pc1 = []
        self.c_d_shifts = []

        with open('tables/pc1.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.pc1.append(row)

        with open('tables/sample_key.txt', newline='') as file:
            self.key = file.read()
            self.key = ascii_to_binary(self.key)

        with open('tables/shifts.txt', newline='') as file:
            self.c_d_shifts = file.read()

    def get_key(self):
        return self.key

    def get_pc1(self):
        return self.pc1

    def get_c_d_shifts(self):
        return self.c_d_shifts