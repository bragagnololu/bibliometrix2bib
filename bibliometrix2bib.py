'''
This code transform a bibliometrix excel from R file into a .bib file again
'''

import pandas as pd
import csv
import sys

folder_data = r"G:\Drives compartilhados\Tese de Doutorado - Lucimara\Bibliometric Review\Bib files\Bibliometrix-Export-File-2021-04-16.xlsx"
base_filename = r'G:\Drives compartilhados\Tese de Doutorado - Lucimara\Bibliometric Review\Bib files/oi.bib'

def xlsx2bib(folder_data,output):
    
    data = pd.read_excel(folder_data)
    
    if data.shape[1] != 29:
        print("The dataframe doesn't contain 29 columns. Please insert a bibliometrix original file.")
        sys.exit(1)
    
    #Renaming columns
    data.columns = ['author', 'author_keywords', 'keywords', 'affiliation', 'abbrev_source_title', 'abstract',
                   'art_number', 'correspondence_address1', 'document_type', 'doi',
                   'editor', 'isbn', 'issn', 'journal', 'language', 'note',
                   'number', 'pages', 'publisher', 'source', 'title', 'volume',
                   'year', 'CR', 'AU_UN', 'AU1_UN', 'AU_UN_NR', 'SR_FULL', 'SR']
    
    # Getting data type
    data['type_upd'] = data['document_type'].str.split(' ').str[0]
    data.insert(0,"type","@" + data['type_upd']+ "{" + 
                data['author'].str.split(' ').str[0] + data['year'].astype(str) + ",")
    
    # Updating authors names as pattern
    data['author'] = ("author={" + data['author'].replace(' ',', ', regex=True)
                            .replace(';',' and ', regex=True)
                            + "}, ")
    
    data_names = list(data.columns)
    cols_names = data_names[2:24]
    
    for col in cols_names:
        data[col] = (col+"={" + data[col].astype(str)
                                + "}, ")
    
    
    # Delete excedent columns
    data = data.drop(['document_type', 'type_upd', 'CR', 'AU_UN', 'AU1_UN', 
               'AU_UN_NR','SR_FULL','SR',], axis=1)
    
    # Add final column
    data['final'] = "}"
    
    data.to_csv(output, encoding='utf-8', index=False, header=False, 
                sep="\t", quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
    
    return

