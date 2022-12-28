import json
import requests
import os
max_index=0
node_red_ip='http://127.0.0.1:1880/'
# Reading from file
chats = []
with open("Data.txt", "r") as infile:
    
    for i in infile:
        data = i.split(",")
        index, flag, df_strength = int(data[0]), (data[1]), int(data[2].strip("\n"))
        max_index=max(index,max_index)
        chats.append([index, flag, df_strength])


os.remove("Data.txt")
print(chats,max_index)
for i in range(len(chats)-max_index-1,len(chats)):
    print(chats[i])
    index=chats[i][0]
    df_strength=chats[i][2]
    flag=(chats[i][1]=="True")
    print(flag)
    if(flag):
        df_strength=int(df_strength/2)
    else:
        df_strength=df_strength+10
    r = requests.post(node_red_ip+'DefenceValue', data = {'index':index,'df_strength':df_strength})