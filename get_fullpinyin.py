#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    程序功能：将文本文件中的汉字转换成拼音全拼，文本文件中每行一个字符串，且只有汉字字符,字符之间不能有空格。
    执行：将此脚本、word.data、name.txt置于同一路径下，在该路径下，执行：python get_fullpinyin.py name.txt 执行成功将在此路径下生成pinyinname_list.txt文件。
    Author:han
"""

__version__ = '0.1'
__all__ = ["PinYin"]

import os.path
from sys import argv
scriptname, filename = argv


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NoFileFound")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    # 获取字符串拼音全拼
    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")
        
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result


if __name__ == "__main__":
    test = PinYin()
    test.load_word()

    txt = open(filename,'r')
    name_list = txt.readlines()
    txt.close()

    pinyinname_list = open('pinyinname_list.txt','w')
    for name in name_list:
	name = name.strip().decode('gbk')
	pinyinname = ''.join(test.hanzi2pinyin(string=name)).strip()

	pinyinname_list.write(pinyinname + '\n')

    print (u'已生成pinyinname_list.txt文件！')
    pinyinname_list.close()


