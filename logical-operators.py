# Short Circuiting 
# >
# <
# ==
is_Friend = False
is_User = True

if is_Friend or is_User:
    print('best friends forever')

# example

print(4 < 5)
print(4 > 5)
print(4 == 5)
# print(4 = 5) this for to assign the variable
print('hello' == 'hello')
print('a' > 'b')
print('a' > 'A')
#print('a' > 'b') is false because print(97>98)
#print('a' > 'A') is false because print(97>65)
## Must use the ASCII CODE of the Characters
# Use below to check 
ord('a')
# Reverse
chr(97)

#Short Circuiting is something is false, everything is going to be false
print(1 < 2 > 3 < 4)
print(1 >= 0)
print(1 <= 0)

print(0 != 1)

# <> == >= <= !=
# and or not 

print(not(True))
print(not(False))

print(not(1 == 1))
print(not(True))

