#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import json
import sys
import csv


# In[2]:


ACCESS_KEY="AKIAJTESX5VNX4H7NVKQ"
SECRET_KEY="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"


# In[3]:



def get_kv_map(file_name):

    with open(file_name, 'rb') as file:
        img_test = file.read()
        bytes_test = bytearray(img_test)
        print('Image loaded', file_name)

    # process using image bytes
    client = boto3.client('textract', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY,region_name="us-east-2")
    response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['FORMS'])

    # Get the text blocks
    blocks=response['Blocks']
    

    # get key and value maps
    key_map = {}
    value_map = {}
    block_map = {}
    for block in blocks:
        block_id = block['Id']
        block_map[block_id] = block
        if block['BlockType'] == "KEY_VALUE_SET":
            if 'KEY' in block['EntityTypes']:
                key_map[block_id] = block
            else:
                value_map[block_id] = block

    return key_map, value_map, block_map


# In[4]:


def find_value_block(key_block, value_map):
    for relationship in key_block['Relationships']:
        if relationship['Type'] == 'VALUE':
            for value_id in relationship['Ids']:
                value_block = value_map[value_id]
    return value_block


# In[5]:


def get_text(result, blocks_map):
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    if word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] == 'SELECTED':
                            text += 'X '    

                                
    return text


def print_kvs(kvs):
    for key, value in kvs.items():
        print(key, ":", value)


# In[6]:


def get_kv_relationship(key_map, value_map, block_map):
    kvs = {}
    for block_id, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text(key_block, block_map)
        val = get_text(value_block, block_map)
        kvs[key] = val
    csv_name="C:\\Users\\Chirag\\Desktop\\Insurance_Claims\\Mn247xyz\\Mn247xyz_MedicalForm_Entities.csv"
    with open(csv_name, 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, kvs.keys())
        w.writeheader()
        w.writerow(kvs)
    return kvs


# In[7]:


def main(file_name):

    key_map, value_map, block_map = get_kv_map(file_name)

    # Get Key Value relationship
    kvs = get_kv_relationship(key_map, value_map, block_map)
    print("\n\n== FOUND KEY : VALUE pairs ===\n")
    print_kvs(kvs)


# In[8]:


if __name__ == "__main__":
    file_name = "C:\\Users\\Chirag\\Desktop\\Insurance_Claims\\Mn247xyz\\Mn247xyz_MedicalForm.png"
    main(file_name)


# In[41]:





# In[ ]:




