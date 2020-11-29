import sqlite3
import csv


conn = sqlite3.connect('2018_Financial_Data.sqlite3')
cur = conn.cursor()

with open('2018_Financial_Data.csv', 'rt', encoding='latin1') as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)

    next(csv_reader_object)

    for row in csv_reader_object:
        print(row)


        

# self._fieldnames = next(self.reader) -> hatte ich das nicht auch in Jupyter und musste erst die Nullstellen säubern?
#_csv.Error: line contains NUL