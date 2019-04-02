# Qatar National Library

## Harvesting Notes
* IP address must be whitelisted by QNL before harvesting 
* There are two separate metadata records for each resource: one in Arabic and one in English; these are contained in the same record element and can be mapped to the same field in the config file
* Images are available through IIIF
* Records have been harvested and a WIP script has been created to delete unapproved records and merge the Arabic and English records into a single record. Need to add name, note, and subject following the same pattern as abstract an typeOfResource.

## Analysis Results
           {http://www.loc.gov/mods/v3}abstract: |=======================  |  29611/31908 |  92%
    {http://www.loc.gov/mods/v3}accessCondition: |=========================|  31908/31908 | 100%
         {http://www.loc.gov/mods/v3}identifier: |=========================|  31908/31908 | 100%
           {http://www.loc.gov/mods/v3}language: |=========================|  31908/31908 | 100%
           {http://www.loc.gov/mods/v3}location: |=========================|  31908/31908 | 100%
               {http://www.loc.gov/mods/v3}name: |========                 |  10891/31908 |  34%
               {http://www.loc.gov/mods/v3}note: |====                     |   6197/31908 |  19%
         {http://www.loc.gov/mods/v3}originInfo: |=========================|  31908/31908 | 100%
{http://www.loc.gov/mods/v3}physicalDescription: |=========================|  31908/31908 | 100%
         {http://www.loc.gov/mods/v3}recordInfo: |=========================|  31908/31908 | 100%
            {http://www.loc.gov/mods/v3}subject: |==========               |  13826/31908 |  43%
          {http://www.loc.gov/mods/v3}titleInfo: |=========================|  31908/31908 | 100%
     {http://www.loc.gov/mods/v3}typeOfResource: |=======================  |  29611/31908 |  92%
