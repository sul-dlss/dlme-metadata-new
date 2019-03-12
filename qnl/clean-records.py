from lxml import etree
import glob

oai = "{http://www.openarchives.org/OAI/2.0/}"

file_names = glob.glob('british-library/data/*.xml')
record_count = 0
en = 0
ar = 0
qnlhc_ar = 0
qnlhc_en = 0
bl_t = 0

for record in file_names:
    tree = etree.parse(record)
    id = tree.find('/*/{http://www.openarchives.org/OAI/2.0/}identifier').text
    # location = tree.find('/*/*/{http://www.loc.gov/mods/v3}physicalLocation').text
    if "qnlhc" in id:
        record_count +=1
        if "ar" in id:
            qnlhc_ar += 1
        else:
            qnlhc_en += 1
    if "en" in id:
        en += 1
    if "ar" in id:
        ar += 1
    if "81055" in id:
        bl_t += 1
    # if "British Library" in location:
    #     BL += 1

print("QNLHC records: " + str(record_count))
print("QNLHC English records: " + str(qnlhc_en))
print("QNLHC Arabic records: " + str(qnlhc_ar))
print("British Library English records: " + str(en - qnlhc_en))
print("British Library Arabic records: " +str(ar - qnlhc_ar))
print("Total English records: " + str(en))
print("Total Arabic records: " +str(ar))
print("Test: " + str(bl_t))
# print("BL record count: " + str(BL))
