import csv
import argparse
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Specifies input arguments
def setup_parser():
    parser = argparse.ArgumentParser(description="This is to define the input files")
    parser.add_argument('-v', '--VAF', help="This is the VAF cutoff", required=True, dest="VAF_input",  type=int)
    parser.add_argument('-c', '--cli', help="Activate or deactivate ClinVar filter", action = 'store_true', required=False, dest="clinvar_input")
    parser.add_argument('-f', '--file', help="This is the input file", required=True, dest="filename")
    return parser

# Reads input NGS data table, creates ClnVar filtered output file if requested, checks presence of required columns
def files_generation(filename,output_file_VAF,VAF_input,clinvar_input):
    if clinvar_input == True:
        output_file_VAF_clinvar = open(ROOT_DIR + "/VAF_ClinVar_output" + str(VAF_input) + ".csv", "w")
    else:
        output_file_VAF_clinvar = None
    with open(filename) as csvfile:
        file_input_dict = csv.DictReader(csvfile)
        headers = file_input_dict.fieldnames
        if "VAF" and "ClinVar" in headers:
            write_output_file_VAF(headers,output_file_VAF,file_input_dict,VAF_input,clinvar_input,output_file_VAF_clinvar)
        else:
            print("Please check the headers")

# Writes VAF filtered output file
def write_output_file_VAF(headers,output_file_VAF,file_input_dict,VAF_input,clinvar_input,output_file_VAF_clinvar):
    for sequential_column in headers:
        output_file_VAF.write(sequential_column + ",")
    output_file_VAF.write("\n")
    if clinvar_input == True:
        for sequential_column in headers:
            output_file_VAF_clinvar.write(sequential_column + ",")
        output_file_VAF_clinvar.write("\n")
    for row in file_input_dict:
        if "VAF" in row:
            if float(row["VAF"]) >= VAF_input:
                for sequential_column in headers:
                    output_file_VAF.write(row[sequential_column]+",")
                output_file_VAF.write("\n")
                if clinvar_input == True:
                    write_output_file_VAF_clinvar(clinvar_input,output_file_VAF_clinvar,row)

# Writes ClnVar filtered output file
def write_output_file_VAF_clinvar(clinvar_input,output_file_VAF_clinvar,row):
    if clinvar_input == True:
        if "ClinVar" in row:
            if row["ClinVar"] != "-":
                for sequential_column_VAF in row:
                    output_file_VAF_clinvar.write(row[sequential_column_VAF] + ",")
                output_file_VAF_clinvar.write("\n")


#  Given data and arguments, it uses a threshold to generate a VAF filtered output file and a CLinvar filtered file if requested
def main():
    parser_result=setup_parser()
    args = parser_result.parse_args()
    VAF_input = args.VAF_input
    clinvar_input = args.clinvar_input
    filename = args.filename
    output_file_VAF = open(ROOT_DIR+"/VAF_output_"+str(args.VAF_input)+".csv", "w")
    files_generation(filename,output_file_VAF,VAF_input,clinvar_input)


if __name__ == "__main__":
    main()