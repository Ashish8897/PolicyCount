# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:30:38 2021

@author: akengari
"""
import pandas as pd


def read_sheet(test1,resultant):
    transactions=['Cancellation','Renewal','Policy Change','Submission','Reinstatement','Rewrite','Rewrite New Term']

    for transaction in transactions:   
        select_home=[]
        df = pd.read_excel(test1,transaction)
        states=['Florida','Georgia','Michigan','Tennessee']
        product_code=['Homeowners','PersonalAuto','LegacyAuto']
        print(count(select_home,product_code,states,df))
        #result=dict([(transaction, count(select_home,product_code,states,df))])
        #resultant.append(result)    

def count(select_home,product_code,states,df):
    for product in product_code:
        temp=[]
        total=[]
        df_product=df.loc[df['PRODUCTCODE']==product]
       
        for state in states:
            
            df_state= df_product.loc[df_product['STATE']==state]
            
            temp.append(df_state.shape[0])
        count=sum(temp)
        temp.append(count)
        select_home.append(temp)
    print('select home',select_home)
    total=[]
    sum1=0
    for i in range(len(select_home[0])):
        print(i)
        sum1=select_home[0][i]+select_home[1][i]+select_home[2][i]  
        print('sum is',sum1)
        total.append(sum1)
    select_home.append(total)    
        
        
        
    return  dict([('SELECT HOME', select_home[0]),('SELECT AUTO', select_home[1]),('LEGACY AUTO', select_home[2]),('TOTAL', select_home[3])])

test1="C:/Users/AKENGARI/Downloads/Copy of PolicyCounts_Bound.xlsx"
resultant=[]
read_sheet(test1, resultant)    