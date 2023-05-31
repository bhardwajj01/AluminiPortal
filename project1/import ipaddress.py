import ipaddress
data={
    "prefixes": [{
    "ipv4Prefix": "8.8.4.0/24"
  }, {
    "ipv4Prefix": "8.8.8.0/24"
  }, {
    "ipv4Prefix": "8.34.208.0/20"
  }, {
    "ipv4Prefix": "8.35.192.0/20"
  }, {
    "ipv4Prefix": "23.236.48.0/20"
  }, {
    "ipv4Prefix": "23.251.128.0/19"
  }, {
    "ipv4Prefix": "34.0.0.0/15"
  }, {
    "ipv4Prefix": "34.2.0.0/16"
  }, {
    "ipv4Prefix": "34.3.0.0/23"
  }, {
    "ipv4Prefix": "34.3.3.0/24"
  }, {
    "ipv4Prefix": "34.3.4.0/24"
  }, {
    "ipv4Prefix": "34.3.8.0/21"
  }, {
    "ipv4Prefix": "34.3.16.0/20"
  }, {
    "ipv4Prefix": "34.3.32.0/19"
  }, {
    "ipv4Prefix": "34.3.64.0/18"
  }, {
    "ipv4Prefix": "34.3.128.0/17"
  }, {
    "ipv4Prefix": "34.4.0.0/14"
  }, {
    "ipv4Prefix": "34.8.0.0/13"
  }, {
    "ipv4Prefix": "34.16.0.0/12"
  }, {
    "ipv4Prefix": "34.32.0.0/11"
  }, {
    "ipv4Prefix": "34.64.0.0/10"
  }, {
    "ipv4Prefix": "34.128.0.0/10"
  }, {
    "ipv4Prefix": "35.184.0.0/13"
  }, {
    "ipv4Prefix": "35.192.0.0/14"
  }, {
    "ipv4Prefix": "35.196.0.0/15"
  }, {
    "ipv4Prefix": "35.198.0.0/16"
  }, {
    "ipv4Prefix": "35.199.0.0/17"
  }, {
    "ipv4Prefix": "35.199.128.0/18"
  }, {
    "ipv4Prefix": "35.200.0.0/13"
  }, {
    "ipv4Prefix": "35.208.0.0/12"
  }, {
    "ipv4Prefix": "35.224.0.0/12"
  }, {
    "ipv4Prefix": "35.240.0.0/13"
  }, {
    "ipv4Prefix": "64.15.112.0/20"
  }, {
    "ipv4Prefix": "64.233.160.0/19"
  }, {
    "ipv4Prefix": "66.22.228.0/23"
  }, {
    "ipv4Prefix": "66.102.0.0/20"
  }, {
    "ipv4Prefix": "66.249.64.0/19"
  }, {
    "ipv4Prefix": "70.32.128.0/19"
  }, {
    "ipv4Prefix": "72.14.192.0/18"
  }, {
    "ipv4Prefix": "74.125.0.0/16"
  }, {
    "ipv4Prefix": "104.154.0.0/15"
  }, {
    "ipv4Prefix": "104.196.0.0/14"
  }, {
    "ipv4Prefix": "104.237.160.0/19"
  }, {
    "ipv4Prefix": "107.167.160.0/19"
  }, {
    "ipv4Prefix": "107.178.192.0/18"
  }, {
    "ipv4Prefix": "108.59.80.0/20"
  }, {
    "ipv4Prefix": "108.170.192.0/18"
  }, {
    "ipv4Prefix": "108.177.0.0/17"
  }, {
    "ipv4Prefix": "130.211.0.0/16"
  }, {
    "ipv4Prefix": "136.112.0.0/12"
  }, {
    "ipv4Prefix": "142.250.0.0/15"
  }, {
    "ipv4Prefix": "146.148.0.0/17"
  }, {
    "ipv4Prefix": "162.216.148.0/22"
  }, {
    "ipv4Prefix": "162.222.176.0/21"
  }, {
    "ipv4Prefix": "172.110.32.0/21"
  }, {
    "ipv4Prefix": "172.217.0.0/16"
  }, {
    "ipv4Prefix": "172.253.0.0/16"
  }, {
    "ipv4Prefix": "173.194.0.0/16"
  }, {
    "ipv4Prefix": "173.255.112.0/20"
  }, {
    "ipv4Prefix": "192.158.28.0/22"
  }, {
    "ipv4Prefix": "192.178.0.0/15"
  }, {
    "ipv4Prefix": "193.186.4.0/24"
  }, {
    "ipv4Prefix": "199.36.154.0/23"
  }, {
    "ipv4Prefix": "199.36.156.0/24"
  }, {
    "ipv4Prefix": "199.192.112.0/22"
  }, {
    "ipv4Prefix": "199.223.232.0/21"
  }, {
    "ipv4Prefix": "207.223.160.0/20"
  }, {
    "ipv4Prefix": "208.65.152.0/22"
  }, {
    "ipv4Prefix": "208.68.108.0/22"
  }, {
    "ipv4Prefix": "208.81.188.0/22"
  }, {
    "ipv4Prefix": "208.117.224.0/19"
  }, {
    "ipv4Prefix": "209.85.128.0/17"
  }, {
    "ipv4Prefix": "216.58.192.0/19"
  }, {
    "ipv4Prefix": "216.73.80.0/20"
  }, {
    "ipv4Prefix": "216.239.32.0/19"
  }]
}
prefixes = data["prefixes"]

for prefix in prefixes:
    ip_prefix = prefix["ipv4Prefix"]
    network = ipaddress.ip_network(ip_prefix)
    start_ip = network.network_address
    end_ip = network.broadcast_address
    
    print("IP Address:", ip_prefix)
    print("Start:", start_ip)
    print("End:", end_ip)
    print()


# # #     ip_prefix = prefix["ipv6_prefix"]
# # #     network = ipaddress.ip_network(ip_prefix)
# # #     start_ip = network.network_address
# # #     end_ip = network.broadcast_address
    
# # #     print("IP Address:", ip_prefix)
# # #     print("Start:", start_ip)
# # #     print("End:", end_ip)
# # #     print()

# #how to convert a txt file's data into json format and remove duplicates also.........
