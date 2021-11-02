#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:02:38 2021

@author: wenzhang
"""

import pandas as pd

import requests

import csv

import argparse



url = "https://raw.githubusercontent.com/language-technology-GC/hw2-wenzhang0222/master/ice_train.tsv"

res = requests.get(url, allow_redirects = True)

with open("ice_train.tsv", "wb") as file:
    
    file.write(res.content)
    
sales_team = pd.read_csv("ice_train.tsv")


url = "https://raw.githubusercontent.com/language-technology-GC/hw2-wenzhang0222/master/ice_dev.tsv"

res = requests.get(url, allow_redirects = True)

with open("ice_dev.tsv", "wb") as file:
    
    file.write(res.content)

sales_team = pd.read_csv("ice_dev.tsv")



url = "https://raw.githubusercontent.com/language-technology-GC/hw2-wenzhang0222/master/ice_test.tsv"

res = requests.get(url, allow_redirects = True)

with open("ice_test.tsv", "wb") as file:
    
    file.write(res.content)

sales_team = pd.read_csv("ice_test.tsv")



def main(args: argparse.Namespace) -> None:
    
    with open("ice_train.tsv", "r") as source:
        
        with open("train.ice.g", "w") as sink:
            
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
                
                print(" ".join(i[0]), file = sink)        
           
    with open("ice_train.tsv", "r") as source:
        
        with open("train.ice.p", "w") as sink:
           
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
                
                print(i[1], file = sink)
            
    with open("ice_dev.tsv", "r") as source:
        
        with open("dev.ice.g", "w") as sink:
           
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
                
                print(" ".join(i[0]), file = sink)
            
    with open("ice_dev.tsv", "r") as source:
        
        with open("dev.ice.p", "w") as sink:
           
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
                
                print(i[1], file = sink)
            
    with open("ice_test.tsv", "r") as source:
       
        with open("test.ice.g", "w") as sink:
            
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
                
                print(" ".join(i[0]), file = sink)
            
    with open("ice_test.tsv", "r") as source:
        
        with open("test.ice.p", "w") as sink:
            
            reader = csv.reader(source, delimiter = "\t")
            
            for i in reader:
               
                print(i[1], file = sink)
                

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument("--ice.g", help = "path to ice.g file")
    
    parser.add_argument("--ice.p", help = "path to ice.p file")
    
    main(parser.parse_args())
    

