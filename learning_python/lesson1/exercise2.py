#!/usr/bin/env python
"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it
up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

$ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.

"""
ip_addr = input("Please enter an IP address: ")
ip_octets = ip_addr.split(".")
octet_1 = ip_octets[0]
octet_2 = ip_octets[1]
octet_3 = ip_octets[2]
octet_4 = ip_octets[3]

# Functions
def decimalToBinary(n):  
    return bin(n)  
def decimalToHex(n):  
    return hex(n)

octet_1 = int(ip_octets[0])
octet_2 = int(ip_octets[1])
octet_3 = int(ip_octets[2])
octet_4 = int(ip_octets[3])

octet1_to_bin = decimalToBinary(octet_1)
octet2_to_bin = decimalToBinary(octet_2)
octet3_to_bin = decimalToBinary(octet_3)
octet4_to_bin = decimalToBinary(octet_4)

octet1_to_Hex = decimalToHex(octet_1)
octet2_to_Hex = decimalToHex(octet_2)
octet3_to_Hex = decimalToHex(octet_3)
octet4_to_Hex = decimalToHex(octet_4)

line = "------------------------------------------------------------"

array = [line,octet_1,octet1_to_bin,octet1_to_Hex,octet_2,octet2_to_bin,octet2_to_Hex,octet_3,octet3_to_bin,octet3_to_Hex,octet_4,octet4_to_bin,octet4_to_Hex]

col_1 = ["Octet1","------",{array[1]},{array[2]},{array[3]}]
col_2 = ["\nOctet2","------",{array[4]},{array[5]},{array[6]}]
col_3 = ["\nOctet3","------",{array[7]},{array[8]},{array[9]}]
col_4 = ["\nOctet4","------",{array[10]},{array[11]},{array[12]}]

for item in col_1:
  print(item)

for item in col_2:
  print(item)

for item in col_3:
  print(item)

for item in col_4:
  print(item)