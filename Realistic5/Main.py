import hashlib
import os
from past.builtins import xrange

your_list = '1234567890abcdefghijklmnopqrstuvwxyz?:'
complete_list = []
for current in xrange(5):
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a
input("list complete. press enter to continue(" + str(len(complete_list))+") passwords to try")
for i in complete_list:
    print("[+]Trying: " + i +"\t", end="")
    print(str(hashlib.new('md4', i.encode('utf-8')).hexdigest()))
    if str(hashlib.new('md4', i.encode('utf-8')).hexdigest()) == "e78966268a13410f5cb4888c61795abc":
        print("PASSWORD FOUND: " + i)
        command = "echo FOUND--------------------------------"
        os.system("echo PASSWORD FOUND : " + i + ">> tries.txt")
        input("-------------------------------")
        exit(1)
