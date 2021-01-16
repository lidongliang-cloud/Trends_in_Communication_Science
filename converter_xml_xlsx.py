import xml.etree.cElementTree as et
import pandas as pd
import sys

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None

input_path = sys.argv[1]
output_name = sys.argv[2]

def main(input_path,output_name):
    """ main """
    parsed_xml = et.parse(input_path)
    dfcols = ['resultID', 'journal', 'issn','title','doi','abstract','lang','pubtype','year','month','day', 'authors','affils','subjects']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsed_xml.getroot():
        resultID = node.attrib.get('resultID')
        journal = node.find('header/controlInfo/jinfo/jtl')
        issn = node.find('header/controlInfo/jinfo/issn')
        title = node.find('header/controlInfo/artinfo/tig/')
        doi = node.find('header/controlInfo/artinfo/ui')
        abstract = node.find('header/controlInfo/artinfo/ab')
        lang = node.find('header/controlInfo/language')
        pubtype = node.find('header/controlInfo/artinfo/pubtype')
        author_list = []
        affil_list = []
        subject_list = []
        for y in node.iter('dt'):
            year = y.attrib.get('year') 
        for m in node.iter('dt'):
            month = m.attrib.get('month')
        for d in node.iter('dt'):
            day = m.attrib.get('day')
        for aus in node.iter('au'):
            author_list.append(aus.text)
        for aff in node.iter('affil'):
            affil_list.append(aff.text)
        for sub in node.iter('subj'):
            subject_list.append(sub.text)

        df_xml = df_xml.append(
            pd.Series([resultID, 
                       getvalueofnode(journal), 
                       getvalueofnode(issn), 
                       getvalueofnode(title),
                       getvalueofnode(doi),
                       getvalueofnode(abstract),
                       getvalueofnode(lang),
                       getvalueofnode(pubtype),
                       year,
                       month,
                       day,
                       author_list,
                       affil_list,
                       subject_list], 
                       index=dfcols),
                       ignore_index=True) # to list
    df_xml = pd.DataFrame(df_xml) # to dataframe
    df_xml.to_excel(output_name) # to excel

if __name__ == "__main__":
    main(input_path,output_name) # Let's go!