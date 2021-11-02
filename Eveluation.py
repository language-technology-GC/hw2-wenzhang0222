#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:51:13 2021

@author: wenzhang
"""

import logging


def main():
    
    
    incorrect = 0
    
    seen = 0
    
    with open("predictions.txt", "r") as source:
        
        for line in source:

            if line.startswith("T-"):

                word1 = line.split("\t")[-1]
                
                seen += 1

            elif line.startswith("H-"):

                word2 = line.split("\t")[-1]
                
                if word1 != word2:
                    
                    incorrect += 1
                
    wer = 100 * (incorrect / seen)
            
    logging.info("wer: %.2f", wer)
                 
    print(f"WER:{wer}")
    
main()