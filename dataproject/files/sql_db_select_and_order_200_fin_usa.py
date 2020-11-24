import sqlite3
import csv


conn = sqlite3.connect('2018_Financial_Data.sqlite3')
cur = conn.cursor()

with open('portfolio.csv') as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    for row in csv_reader_object:
        print(row)
