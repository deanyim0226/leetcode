"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



"""
class Solution:
    def defangIPaddr(self, address: str) -> str:

        str = address
    
        for i in range(len(str)):
            
            if str[i] == ".":
                
                new_str = str.replace(".", "[.]")
            
                i += 1
                return new_str