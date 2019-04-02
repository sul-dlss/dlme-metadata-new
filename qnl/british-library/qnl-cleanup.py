import glob, os, re
from lxml import etree

oai_ns = "{http://www.openarchives.org/OAI/2.0/}"

for file in glob.glob('/Users/jtim/Dropbox/DLSS/DLME/dlme-metadata/qnl/british-library/data/*.xml'):
     tree = etree.parse(file)
     id = tree.find(oai_ns + "header/" + oai_ns + "identifier").text
     if 'qnlhc' in id:
         os.remove(file)
         print("File Removed!")
     elif '_ar' in id:
         os.remove(file)
         print("File Removed!")
