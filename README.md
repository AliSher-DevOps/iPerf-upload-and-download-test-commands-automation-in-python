# iPerf-upload-and-download-test-commands-automation-in-python
iPerf upload and download test commands automation in python using SSHCLIENT

# Upload Test Commands
diag traffictest server-intf VpnEqxW1w1
diag traffictest client-intf VpnEqxW1w1
diag traffictest port 5221
diag traffictest run -c 10.251.34.5


# Download Test Commands
diag traffictest server-intf VpnEqxW1w2
diag traffictest client-intf VpnEqxW1w2
diag traffictest port 5221
diag traffictest run -c 10.251.34.5 -R VpnEqxW1w2
