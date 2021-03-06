# NGS Results Filter
This file is meant to filter NGS results table in Python3.
The filters can be changed.
Filters here applied:
* a VAF cutoff
* Presence in ClinVar database

### Input files required:
#### 1. NGS data table.
It can be generated as per the user’s preference, however mandatory for a successful run are:
* format: csv
* the headers have to be the first line of the csv file, and have to include “VAF” and “ClinVar”
* no empty cells
  An examples of an input files is available. Please note that this example is provided as a format example only

#### 2. Run python script:
if requesting VAF filter only:
```
python3 NGS_result_table_filter.py -v VAF_desired_cutoff -f /path_to/input_file.csv
```

if requesting both VAF and ClinVar filters:

```
python3 NGS_result_table_filter.py -v VAF_desired_cutoff -c -f /path_to/input_file.csv
```


#### 3. Bash script with:
An examples of a specification files is available:
```
./my_NGS_filter_old.sh
```


If used, citation is welcome
Please do get in contact with comments and suggestions
Cheers!
