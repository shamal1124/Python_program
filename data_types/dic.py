# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:18:25 2024

@author: dyp
"""

dc = {"nm" : "shamal","lm" : "gaykwad", "age" : 21 , "clg":"dypcet" }
print(dc)
print("length : ",len(dc))
print("get function : ",dc.get("nm"))
print("keys function : ",dc.keys())
print("values function : ",dc.values())
dc.update({"age": 20})
print("update function : ",dc)
print("pop function : ",dc.pop("age"))
dc["dep"] = "cse" 
print("positem function : ",dc.popitem())
dc1 = dc.copy()
print("copied dictonary : ",dc1)
dc1.clear()
print("clear function : ",dc1)
print("from keys function : ",dc.fromkeys("age"))
print("itms function : ",dc.items())
print("set default : ",dc.setdefault("clg"))