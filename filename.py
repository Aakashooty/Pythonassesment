#!usr/bin/python3
import os, fnmatch
print("Enter the filename ")
fn=input()
l=len(fn)
fn=fn+".*"
c=0
path="/home/aakash/Documents/python"
for root, di, files in os.walk(path):
    for n in files:
        if fnmatch.fnmatch(n, fn):
            print(n[l:])
            c+=1
    if c==0:
        print("File doesnot exist")
