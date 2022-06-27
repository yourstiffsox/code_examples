#!/usr/bin/env python3
import re
import csv
import os

errordict = {}
infodict = {}
erruserdict = {}
userlist = []
finaldict = []

os.chdir('/Users/ryanw/OneDrive/Desktop')

#create base dictionaries from system log
with open('test.txt') as file:
    for line in file:
        temperr = ''
        username = re.search(r'.*?\((.*)\).*', line).group(1)
        try:
            temperr = re.search(r'ERROR (\w+ )*', line).group()
            try:
                erruserdict[username] += 1
            except KeyError:
                erruserdict[username] = 1
        except AttributeError:
            try:
                tempinf = re.search(r'INFO (\w+ )*', line).group()
            except AttributeError:
                pass
            try:
                infodict[username] += 1
            except KeyError:
                infodict[username] = 1
        if temperr != '':
            try:
                errordict[temperr] += 1
            except KeyError:
                errordict[temperr] = 1
#make a dictionary of errors and infos for each user
ds = [infodict, erruserdict]
d = {}
for k in erruserdict.keys():
    if k not in infodict:
        infodict[k] = 0
    try:
        d[k] = tuple(d[k] for d in ds)
    except KeyError:
        pass
# make user list
for key in infodict:
    if key not in userlist:
        userlist.append(key)
        tempuserdict = {}
        tempuserdict['Username'] = key
        finaldict.append(tempuserdict)
for key in erruserdict:
    if key not in userlist:
        userlist.append(key)
        tempuserdict = {}
        tempuserdict['Username'] = key
        finaldict.append(tempuserdict)
#make list of dictionaries with user error and info as the keys of each
userdictlist = []
for user in userlist:
         tempinf = d[user]
         tempdict = {}
         tempdict['Username'] = user
         try:
             tempdict['INFO'] = tempinf[0]
         except IndexError:
             tempdict['INFO'] = 0
         try:
             tempdict['ERROR'] = tempinf[1]
         except IndexError:
             tempdict['ERROR'] = 0
         userdictlist.append(tempdict)
#sort list of dicts
finallist = sorted(userdictlist, key=lambda x: x['Username'])
#make Error dict csv from errordict
with open('error_message.csv', 'w') as e:
    fieldnames = ['Error', 'Count']
    writer = csv.writer(e)
    writer.writerows(errordict.items())    
    
#make user stats csv file from finalist list of dictionaries
with open('user_statistics.csv', 'w') as final:
    header = ['Username', 'ERROR', 'INFO']
    writer = csv.DictWriter(final, fieldnames=header)
    writer.writeheader()
    writer.writerows(finallist)
print('Finished') 


