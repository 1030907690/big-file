# -*- coding: utf-8 -*-

'''
2019年1月15日18:42:25
git 上传
'''

import os


if __name__ == '__main__':
    print("start");
    print("add .")
    os.system("git add .")

    random_input = input(" 请输入提交描述:");
    print("git commit -m "+random_input);
    os.system("git commit -m " + random_input);

    print("git push");
    os.system("git push");

    print( "当前路径 : " + os.getcwd());
    print("end");
    random_input = input(" 请输入任意字符结束. ");