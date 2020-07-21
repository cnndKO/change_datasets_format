#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: mulina
# @FileName: __init__.py.py
# @CreateTime: 2020/6/9  21:06
# @Software: PyCharm
"""主要将类似NCBI-disease单词和标注在同一文件、且句子间以空行相隔的数据集
拆分，形成句子为一行，句子和标签分离的数据集
示例：
it  O
is  O
new  0
com  B
method  I
.  O
转成
it is new com method.
O O O B I O
"""
import pandas as pd
import os
import csv
filename = "./NCBI-disease/test.tsv"
newfilename = "./NCBI-disease/testb.words.txt"
tagfilename = "./NCBI-disease/testb.tags.txt"
def change_NCBI_disease_format(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.split('	')
            with open(newfilename, 'a+') as fw:
                if line[0] == "\n":  # 句子结束
                    fw.write("\n")
                    line.append("")
                    line[1] = "\n"
                else:
                    fw.write(line[0] + ' ')
            fw.close()

            with open(tagfilename, 'a+') as ft:
                if line[1] == "\n":  # 句子结束
                    ft.write("\n")
                else:
                    ft.write(line[1].strip("\n") + ' ')
            ft.close()

change_NCBI_disease_format(filename)
