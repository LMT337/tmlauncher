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

#matching pse's
# 159951154	NWD257834
# 159944996	NWD396619
# 159944147	NWD789136
# 159945663	NWD884418
# 159945429	NWD233846
# 159945833	NWD748619
# 159945912	NWD146608
# 159945648	NWD833538
# 159951483	NWD932630
# 159945441	NWD828614
# 159951117	NWD507538
# 159945846	NWD209906
# 159950439	NWD801520


sample_pse = {}

def sample_name(sample_reader):

    sample_results = []
    
    for sample_email in sample_reader:
        # remove white space from dictionary
        sample_new = {k.replace(' ', ''): v for k, v in sample_email.items()}

        # remove -lib1 from sample name
        sample_name = sample_new['Library']
        sample = sample_name.split('-')[0]
        sample_results.append(sample)

    return sample_results

def sample_pse_match(sample_email_list, workfile_reader):

    sample_pse = {}

    #Find sample matches in workflow tsv, return pse's and sample names
    for workfile in workfile_reader:
        if workfile['Sample Full Name'] in sample_email_list:
            sample_pse[workfile['Sample Full Name']] = workfile['PSE']

    return sample_pse


with open(master_file) as master_tsv, open(args.file) as workfile_csv, \
     open(args.sample_qc) as sample_tsv, open( outfile, 'w') as outfilecsv:

    master_reader = csv.DictReader(master_tsv, delimiter="\t")
    workfile_reader = csv.DictReader(workfile_csv, delimiter="\t")
    sample_reader = csv.DictReader(sample_tsv, delimiter="\t")

    print(master_reader)
    print(workfile_reader)
    print(sample_reader)
    sample_email_list = sample_name(sample_reader)
    sample_pse_dict = sample_pse_match(sample_email_list, workfile_reader)
    print(sample_pse_dict)
    # header_fields = header + qc_header
    # w = csv.DictWriter(outfilecsv, header_fields, delimiter="\t")
    # w.writeheader()



