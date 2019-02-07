import errno
import os
from lxml import etree
from sickle import Sickle
from sickle.iterator import OAIResponseIterator

def to_str(bytes_or_str):
    '''Takes bytes or string and returns string'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

sickle = Sickle('http://cdm21044.contentdm.oclc.org/oai/oai.php', iterator=OAIResponseIterator)

records = sickle.ListRecords(metadataPrefix='oai_dc', set='Kitapvehat')
file_name = 'data/kitapvehat.xml'
if not os.path.exists(os.path.dirname(file_name)):
    try:
        os.makedirs(os.path.dirname(file_name))
    except OSError as exc: 
        if exc.errno != errno.EEXIST:
            raise
    
with open(file_name, 'w') as f:
    for page in records:
        f.write(to_str(records.next().raw.encode('utf8')))
    
f.close()

