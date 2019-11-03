up = ord('A')
low = ord('a')
str = "b7h8ii;h"
s = ""
add = 0
for ch in str:
    s += chr(ord(ch)-add)
    add+=1

print(s)
