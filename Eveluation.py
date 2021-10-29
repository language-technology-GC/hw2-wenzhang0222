#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:02:38 2021

@author: wenzhang
"""


def main():
    with open ("predictions.txt","r") as source:
        with open ("THlines.txt", 'w') as sink:
            for curline in source:
                if curline.startswith("T") or curline.startswith("H"):
                    print(curline, file=sink)

                     

def match():
    with open ("THlines.txt", 'r') as source:
        correct = 0
        seen = 0
        for a,b in line.startswith("T"):
            for c, d, e in line.startswith("H"):
                if b==e:
                    correct += 1
                else:
                    pass
                seen += 1
                
        WER = 100 * ((seen-correct) / seen)
        logging.info(WER: %.2f)
        
     
main()
            