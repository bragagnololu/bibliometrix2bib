# bibliometrix2bib
This repository contains a Python function that converts a .xlsx bibliometrix file from R to a .bib file. Then, it can be imported in reference managers, such as Mendeley (other reference managers were not tested).

## 1 Inputs

The function **xlsx2bib** takes two arguments:

    xlsx2bib(folder_data,output)

    folder_data = bibliometrix_input.xlsx #path for the .xlsx bibliometrix file
    base_filename = output_refs.bib #output file (.bib)

## System requirements
    Python 3.0
    pandas
