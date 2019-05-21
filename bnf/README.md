# Bibliothèque nationale de France

## Harvesting Notes
* The API used is an SRU API
* base urls: 
	- IFEA: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=50&page=1&collapsing=true&exactSearch=false&query=dc.source%20all%20%22Institut%20Fran%C3%A7ais%20d%E2%80%99%C3%89tudes%20Anatoliennes%22%20%20and%20%28provenance%20adj%20%22bnf.fr%22%29
	- SALT: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=50&page=1&collapsing=true&exactSearch=false&query=%28provenance%20adj%20%22saltresearch%22%29
	- BO: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=50&page=1&collapsing=true&exactSearch=false&query=dc.source%20all%20%22Biblioth%C3%A8que%20Orientale%22%20%20and%20%28provenance%20adj%20%22bnf.fr%22%29
	- CEAlex: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=50&page=1&collapsing=true&exactSearch=false&query=dc.source%20all%20%22cealex%22%20%20and%20%28provenance%20adj%20%22bnf.fr%22%29
	- IDEO: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=15&page=1&collapsing=true&exactSearch=false&query=%28%28bibliotheque%20adj%20%22Institut%20dominicain%20d%27%C3%A9tudes%20orientales%22%29%29#resultat-id-3
	- IFAO: https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&startRecord=0&maximumRecords=50&page=1&collapsing=true&exactSearch=false&query=dc.source%20all%20%22Institut%20fran%C3%A7ais%20d%E2%80%99arch%C3%A9ologie%20orientale%22%20%20and%20%28provenance%20adj%20%22bnf.fr%22%29
* The SALT data is no longer resolvable
* The data is in the public domain and we have explicit approval from BnF and IDEO. We have no contact with the other institutions.

## Analysis Results

### BO
  srw:extraRecordData/link: |=========================|     77/77 | 100%
           srw:extraRecordData/nqamoyen: |=========================|     77/77 | 100%
          srw:extraRecordData/thumbnail: |=========================|     77/77 | 100%
            srw:extraRecordData/typedoc: |=========================|     77/77 | 100%
srw:recordData/oai_dc:dc/dc:contributor: |=====================    |     65/77 |  84%
    srw:recordData/oai_dc:dc/dc:creator: |==                       |      7/77 |   9%
       srw:recordData/oai_dc:dc/dc:date: |======================== |     75/77 |  97%
srw:recordData/oai_dc:dc/dc:description: |=========================|     77/77 | 100%
     srw:recordData/oai_dc:dc/dc:format: |=========================|     77/77 | 100%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|     77/77 | 100%
   srw:recordData/oai_dc:dc/dc:language: |=========================|     77/77 | 100%
  srw:recordData/oai_dc:dc/dc:publisher: |======================== |     76/77 |  98%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|     77/77 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |=========================|     77/77 | 100%
     srw:recordData/oai_dc:dc/dc:source: |=========================|     77/77 | 100%
      srw:recordData/oai_dc:dc/dc:title: |=========================|     77/77 | 100%
       srw:recordData/oai_dc:dc/dc:type: |=========================|     77/77 | 100%
                   srw:recordIdentifier: |=========================|     77/77 | 100%
                      srw:recordPacking: |=========================|     77/77 | 100%
                     srw:recordPosition: |=========================|     77/77 | 100%
                       srw:recordSchema: |=========================|     77/77 | 100%
                       
### CEAlex
               srw:extraRecordData/link: |=========================|    272/272 | 100%
           srw:extraRecordData/nqamoyen: |=========================|    272/272 | 100%
          srw:extraRecordData/thumbnail: |=========================|    272/272 | 100%
            srw:extraRecordData/typedoc: |=========================|    272/272 | 100%
srw:recordData/oai_dc:dc/dc:contributor: |                         |      1/272 |   0%
    srw:recordData/oai_dc:dc/dc:creator: |===                      |     35/272 |  12%
       srw:recordData/oai_dc:dc/dc:date: |===                      |     41/272 |  15%
srw:recordData/oai_dc:dc/dc:description: |=========================|    272/272 | 100%
     srw:recordData/oai_dc:dc/dc:format: |======================== |    270/272 |  99%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|    272/272 | 100%
   srw:recordData/oai_dc:dc/dc:language: |=========================|    272/272 | 100%
  srw:recordData/oai_dc:dc/dc:publisher: |=========================|    272/272 | 100%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|    272/272 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |======================== |    270/272 |  99%
     srw:recordData/oai_dc:dc/dc:source: |=========================|    272/272 | 100%
      srw:recordData/oai_dc:dc/dc:title: |=========================|    272/272 | 100%
       srw:recordData/oai_dc:dc/dc:type: |=========================|    272/272 | 100%
                   srw:recordIdentifier: |=========================|    272/272 | 100%
                      srw:recordPacking: |=========================|    272/272 | 100%
                     srw:recordPosition: |=========================|    272/272 | 100%
                       srw:recordSchema: |=========================|    272/272 | 100%

### IDEO
srw:extraRecordData/link: |=========================|     60/60 | 100%
           srw:extraRecordData/nqamoyen: |=========================|     60/60 | 100%
          srw:extraRecordData/thumbnail: |=========================|     60/60 | 100%
            srw:extraRecordData/typedoc: |=========================|     60/60 | 100%
srw:recordData/oai_dc:dc/dc:contributor: |=========                |     23/60 |  38%
    srw:recordData/oai_dc:dc/dc:creator: |=========================|     60/60 | 100%
       srw:recordData/oai_dc:dc/dc:date: |=====                    |     13/60 |  21%
srw:recordData/oai_dc:dc/dc:description: |=========================|     60/60 | 100%
     srw:recordData/oai_dc:dc/dc:format: |=========================|     60/60 | 100%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|     60/60 | 100%
   srw:recordData/oai_dc:dc/dc:language: |=========================|     60/60 | 100%
  srw:recordData/oai_dc:dc/dc:publisher: |=====                    |     12/60 |  20%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|     60/60 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |=========================|     60/60 | 100%
     srw:recordData/oai_dc:dc/dc:source: |=========================|     60/60 | 100%
    srw:recordData/oai_dc:dc/dc:subject: |====                     |     10/60 |  16%
      srw:recordData/oai_dc:dc/dc:title: |=========================|     60/60 | 100%
       srw:recordData/oai_dc:dc/dc:type: |=========================|     60/60 | 100%
                   srw:recordIdentifier: |=========================|     60/60 | 100%
                      srw:recordPacking: |=========================|     60/60 | 100%
                     srw:recordPosition: |=========================|     60/60 | 100%
                       srw:recordSchema: |=========================|     60/60 | 100%
                       
### IFAO
srw:extraRecordData/link: |=========================|    278/278 | 100%
           srw:extraRecordData/nqamoyen: |=========================|    278/278 | 100%
          srw:extraRecordData/thumbnail: |=========================|    278/278 | 100%
            srw:extraRecordData/typedoc: |=========================|    278/278 | 100%
srw:recordData/oai_dc:dc/dc:contributor: |=                        |     14/278 |   5%
    srw:recordData/oai_dc:dc/dc:creator: |======================== |    270/278 |  97%
       srw:recordData/oai_dc:dc/dc:date: |====================     |    231/278 |  83%
srw:recordData/oai_dc:dc/dc:description: |=========================|    278/278 | 100%
     srw:recordData/oai_dc:dc/dc:format: |=========================|    278/278 | 100%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|    278/278 | 100%
   srw:recordData/oai_dc:dc/dc:language: |===                      |     43/278 |  15%
  srw:recordData/oai_dc:dc/dc:publisher: |======================== |    272/278 |  97%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|    278/278 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |=========================|    278/278 | 100%
     srw:recordData/oai_dc:dc/dc:source: |=========================|    278/278 | 100%
    srw:recordData/oai_dc:dc/dc:subject: |======================== |    267/278 |  96%
      srw:recordData/oai_dc:dc/dc:title: |=========================|    278/278 | 100%
       srw:recordData/oai_dc:dc/dc:type: |======================== |    277/278 |  99%
                   srw:recordIdentifier: |=========================|    278/278 | 100%
                      srw:recordPacking: |=========================|    278/278 | 100%
                     srw:recordPosition: |=========================|    278/278 | 100%
                       srw:recordSchema: |=========================|    278/278 | 100%
                       
### IFEA
srw:extraRecordData/link: |=========================|    415/415 | 100%
           srw:extraRecordData/nqamoyen: |=========================|    415/415 | 100%
          srw:extraRecordData/thumbnail: |=========================|    415/415 | 100%
            srw:extraRecordData/typedoc: |=========================|    415/415 | 100%
    srw:recordData/oai_dc:dc/dc:creator: |=============            |    220/415 |  53%
       srw:recordData/oai_dc:dc/dc:date: |======================== |    412/415 |  99%
srw:recordData/oai_dc:dc/dc:description: |=========================|    415/415 | 100%
     srw:recordData/oai_dc:dc/dc:format: |=========================|    415/415 | 100%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|    415/415 | 100%
   srw:recordData/oai_dc:dc/dc:language: |=========================|    415/415 | 100%
  srw:recordData/oai_dc:dc/dc:publisher: |=========================|    415/415 | 100%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|    415/415 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |=========================|    415/415 | 100%
     srw:recordData/oai_dc:dc/dc:source: |=========================|    415/415 | 100%
    srw:recordData/oai_dc:dc/dc:subject: |=========================|    415/415 | 100%
      srw:recordData/oai_dc:dc/dc:title: |=========================|    415/415 | 100%
       srw:recordData/oai_dc:dc/dc:type: |=========================|    415/415 | 100%
                   srw:recordIdentifier: |=========================|    415/415 | 100%
                      srw:recordPacking: |=========================|    415/415 | 100%
                     srw:recordPosition: |=========================|    415/415 | 100%
                       srw:recordSchema: |=========================|    415/415 | 100%
                       
### SALT
srw:extraRecordData/link: |=========================|    404/404 | 100%
           srw:extraRecordData/nqamoyen: |=========================|    404/404 | 100%
          srw:extraRecordData/thumbnail: |=========================|    404/404 | 100%
            srw:extraRecordData/typedoc: |=========================|    404/404 | 100%
srw:recordData/oai_dc:dc/dc:contributor: |==================       |    303/404 |  75%
   srw:recordData/oai_dc:dc/dc:coverage: |                         |      2/404 |   0%
    srw:recordData/oai_dc:dc/dc:creator: |                         |      3/404 |   0%
       srw:recordData/oai_dc:dc/dc:date: |======================== |    394/404 |  97%
srw:recordData/oai_dc:dc/dc:description: |=================        |    290/404 |  71%
     srw:recordData/oai_dc:dc/dc:format: |=======================  |    376/404 |  93%
 srw:recordData/oai_dc:dc/dc:identifier: |=========================|    404/404 | 100%
   srw:recordData/oai_dc:dc/dc:language: |=========================|    404/404 | 100%
  srw:recordData/oai_dc:dc/dc:publisher: |==================       |    296/404 |  73%
   srw:recordData/oai_dc:dc/dc:relation: |=========================|    404/404 | 100%
     srw:recordData/oai_dc:dc/dc:rights: |=========================|    404/404 | 100%
     srw:recordData/oai_dc:dc/dc:source: |                         |     15/404 |   3%
    srw:recordData/oai_dc:dc/dc:subject: |====                     |     66/404 |  16%
      srw:recordData/oai_dc:dc/dc:title: |=========================|    404/404 | 100%
       srw:recordData/oai_dc:dc/dc:type: |======================== |    403/404 |  99%
                   srw:recordIdentifier: |=========================|    404/404 | 100%
                      srw:recordPacking: |=========================|    404/404 | 100%
                     srw:recordPosition: |=========================|    404/404 | 100%
                       srw:recordSchema: |=========================|    404/404 | 100%
