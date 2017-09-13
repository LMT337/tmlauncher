import csv
import os
import datetime
import argparse
parser = argparse.ArgumentParser()


parser.add_argument("file", type=str)
parser.add_argument("sample_qc", type=str)

args = parser.parse_args()


path = os.path.basename(os.getcwd())
master_file = path + '.master.tsv'
print(master_file)
now = datetime.datetime.now()
print (now.year)

outfile = 'test.py'

with open(master_file) as master_tsv, open(args.file) as workfile_csv, \
     open(args.sample_qc) as sample_tsv, open( outfile, 'w') as outfilecsv:

    master_reader = csv.DictReader(master_tsv, delimiter="\t")
    workfile_reader = csv.DictReader(workfile_csv, delimiter="\t")
    sample_reader = csv.DictReader(sample_tsv, delimiter="\t")

    print(master_reader)
    print(workfile_reader)
    print(sample_reader)
    # header_fields = header + qc_header
    # w = csv.DictWriter(outfilecsv, header_fields, delimiter="\t")
    # w.writeheader()



