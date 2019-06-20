#!/usr/bin/env python
ip = input("Enter IP Address: ")
ip_split = ip.split(".")
print(f"{ip_split[0]:<12} {ip_split[1]:<12} {ip_split[2]:<12} {ip_split[3]:<12}")
