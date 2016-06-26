#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" 
    程序功能：取文本文件中的汉字拼音首字母，文本文件中每行一个字符串，且只有汉字字符,字符之间不能有空格。
    执行：将此脚本、word.data、name.txt置于同一路径下，在该路径下，执行：python get_firstpinyin.py name.txt 执行成功将在此路径下生成firstPinyinName_list.txt文件。
    代码主体及字库文件抄自以下后生：
        Author:cleverdeng
        E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
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
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")
        
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result


    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)


if __name__ == "__main__":
    test = PinYin()
    test.load_word()

    # 获取拼音首字母
    def get_first_pinyin(pinyin_string):
	full_pinyin_list = test.hanzi2pinyin(string=pinyin_string)
    	letter_list = []
    	for pinyin in full_pinyin_list:
    	    letter_list.append(pinyin[0])
    	return ''.join(letter_list)

    txt = open(filename,'r')
    name_list = txt.readlines()
    txt.close()

    PinyinName_list = open('firstPinyinName_list.txt','w')
    for name in name_list:
	name = name.strip()
	fullname = name.decode('gbk')             # 处理utf格式的文本时，参数需设置为utf-8，或修改文本编码格式为gbk
	firstPinyin = get_first_pinyin(fullname)				# 取首字母

	namestr = name + '\t'*2 + firstPinyin.strip()
	PinyinName_list.write(namestr + '\n')
    print (u'已生成 firstPinyinName_list.txt 文件！')     #在linux shell中执行时应去掉此处的u
    PinyinName_list.close()


