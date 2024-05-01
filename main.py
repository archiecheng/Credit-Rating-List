#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/30 11:04
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : main.py
# @Software: PyCharm

# get data from document
import pandas as pd
import numpy as np

company_file_list = pd.read_csv("./file/company_list.csv", header=None)
company_name_list = np.array(company_file_list[0])

# use Gemini to get the company credit rating
# import google gemini library
import google.generativeai as genai
import time

# configure api key
genai.configure(api_key="AIzaSyAGCECLDHnQJ580f5fe32fV6Ust1MFyCGk",transport="rest")

# 1. Generate text from text input
# 1.1 select a model
model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

company_rating_list = []
print("result is generating...please wait")
# 1.2 get response
for company_name in company_name_list:
    question = (
        f"Please provide {company_name}'s latest credit rating in the fixed format below, limited to the following rating agencies: Standard & Poor's. Answer format requirements: [Company Credit Rating]. For example: AA.")
    try:
        response = model.generate_content(question)
        # response = chat.send_message(question)
        company_rating_list.append(response.text)
        print(company_rating_list)
        time.sleep(2)
    except Exception as e:
        print(e)

# question = ("Please provide Walmart's latest credit rating in the fixed format below, limited to the following rating agencies: Standard & Poor's. Answer format requirements: [Company Credit Rating]. For example: AA.")
# response = chat.send_message(question)
# response = model.generate_content(question)
# print(response.text)
# company_rating_list.append(response.text)

# company_rating_list = ['BBB+', 'AA+', 'AA+', 'AA+', 'AAA', 'AA-', 'AAA', 'AAA', 'BBB', 'AA-', 'Cencora credit rating was not found.', 'AAA', 'AAA', 'BBB', 'AA+', 'BBB-', 'BBB', 'BBB', 'BB+', 'BBB+', 'BBB-', 'AA-', 'AA-', 'BBB-', 'BBB+', 'A+', 'BBB+', 'AAA', 'BBB+', 'BBB+', 'AA+', 'AA-', 'AA+', 'A-', 'A-', 'AA-', 'AAA', 'AA+', 'BBB', 'AA+', 'AAA', 'BBB+', 'BBB+', 'AAA+', 'AA', 'A-', 'A', 'A', 'AA-', 'BB+', 'AA+', 'NA', 'BBB', 'AA', 'A+', 'AA+', 'BBB+', 'BBB+', 'AA+', 'BBB+', 'BBB+', 'AA', 'AA', 'AAA', 'AA-', 'N/A', 'AA-', 'BBB', 'AA', 'AA-']
# for i in range(len(company_name_list)):
#     company_rating_list.append(i)
data_structure = {
    "Company":company_name_list.tolist(),
    "Rating":company_rating_list
}

df = pd.DataFrame(data_structure)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
print(df)
df.to_csv('company rating_30.csv')
print("result generating is done!")