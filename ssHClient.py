import pandas as pd
from csv import writer
import paramiko

try:
    print("File Reading")
    df = pd.read_csv('book2.csv')
except:
    print("Invalid File Path")

length = len(df['IP'])
for i in range(0,length):
    ip=df['IP'][i]
    hostname = str(ip)
    username = "admin"
    password = "ExnUSA#1"

    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("Connecting To server")
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        

    stdin, stdout, stderr = client.exec_command("diag traffictest server-intf VpnEqxW1w1")
    print(stdout.readlines())
    
    stdin2, stdout2, stderr2 = client.exec_command("diag traffictest client-intf VpnEqxW1w1")
    print(stdout2.readlines())
    
    stdin3, stdout3, stderr3 = client.exec_command("diag traffictest port 5221")
    print(stdout3.readlines())
    
    list_row=[]
    stdin4, stdout4, stderr4 = client.exec_command("diag traffictest run -c 10.251.34.5")
    print(stdout4.readlines())
    
    
    # for line in stdout4:
    #     print(line.strip())
    
    
    err = stderr4.readlines()
    if err:
        print(err)
    
    list_row.append(stdout4.read().decode())
    
    with open('UploadTestRecords.csv', 'a') as f_object:
    	# Pass this file object to csv.writer()
    	# and get a writer object
    	writer_object = writer(f_object)
    
    	# Pass the list as an argument into
    	# the writerow()
    	writer_object.writerow(list_row)
    
    	#Close the file object
    	f_object.close()
    
    stdin5, stdout5, stderr5 = client.exec_command("diag traffictest server-intf VpnEqxW1w2")
    print(stdout5.readlines())
    
    stdin6, stdout6, stderr6 = client.exec_command("diag traffictest client-intf VpnEqxW1w2")
    print(stdout6.readlines())
    
    stdin7, stdout7, stderr7 = client.exec_command("diag traffictest port 5221")
    print(stdout7.readlines())
    
    list_row2=[]
    
    stdin8, stdout8, stderr8 = client.exec_command("diag traffictest run -c 10.251.34.5 -R VpnEqxW1w2")
    print(stdout8.readlines())
    
    with open('DownloadTestRecords.csv', 'a') as f_object:
    	# Pass this file object to csv.writer()
    	# and get a writer object
    	writer_object = writer(f_object)
    
    	# Pass the list as an argument into
    	# the writerow()
    	writer_object.writerow(list_row)
    
    	#Close the file object
    	f_object.close()
        
    client.close()
        








