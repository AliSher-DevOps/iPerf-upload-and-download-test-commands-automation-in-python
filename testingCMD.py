import pandas as pd

import paramiko

import os

try:
    
    print("File Reading")
    
    df = pd.read_csv('book2.csv')
    
except:
    
    print("Invalid File Path")
    
length = len(df['IP'])

for i in range(0,length):
    
    ip=df['IP'][i]
    
    host = "ssh admin@"+ip

    command_to_excute='cmd /k "'+host+' & diag traffictest server-intf VpnEqxW1w1 & diag traffictest client-intf VpnEqxW1w1 & diag traffictest port 5221 & diag traffictest run -c 10.251.34.5 "'
    os.system(command_to_excute)