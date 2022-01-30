import pandas as pd
import xml.etree.ElementTree as ET
import traceback
import logging
import sys

test_file = sys.argv[1]
class_file = sys.argv[2]

data_frame_init = pd.read_csv(test_file, sep='\t')
data_frame_class = pd.read_csv(class_file, sep='\t')
data_frame = pd.DataFrame(
    {
        "claim-id" : [],
        "claim-text" : [],
        "class" : []
    }
)

file = open(test_file, 'r')
row = file.readline()

cpt = 1

while row:
    try:
        row = row.split("\t")
        '''if (row[1] is None or (row[0] is None)):
            row = file.readline()
            print("error ligne " + str(cpt))
            pass'''
        root = ET.fromstring("<root>" + row[2] + "</root>")
        claim_class = []
        class_fileO = open(class_file, "r")
        row_class = class_fileO.readline()
        find = False
        while row_class:
            row_class = row_class.split("\t")
            if row_class[1] == str(row[0]) and row_class[2] == row[1]:
                claim_class.append(row_class[4][:-1])
                find = True
            if find and (row_class[1] != str(row[0]) or row_class[2] != row[1]):
                break
            row_class = class_fileO.readline()
        class_fileO.close()

        for elem in root.iter('claim'):
            claim_id = elem.attrib.get("num")
            claim_text = ""
            for mots in elem.find('claim-text').itertext():
                claim_text += mots
            '''if claim_id is None:
                print(elem.attrib)
                pass'''
            tmp_data_frame = pd.DataFrame(
                {
            "claim-id" : [str(row[0]) + row[1] + claim_id],
            "claim-text" : [claim_text],
            "class" : [claim_class]
                }
            )
            data_frame = pd.concat([data_frame, tmp_data_frame])
        if (cpt % 10 == 0):
            data_frame.to_csv("test2.csv", sep="\t", mode="a")
            data_frame = pd.DataFrame(
                {
                    "claim-id": [],
                    "claim-text": [],
                    "class": []
                }
            )
        row = file.readline()
        print(cpt)
        cpt += 1
    except Exception as e:
        logging.error(traceback.format_exc())
        # Logs the error appropriately.
file.close()
data_frame.to_csv("test.csv", sep="\t", mode="a")



