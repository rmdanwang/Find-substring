# Homework 6 by Ru Meng(Dan) Wang

#this is to verify that function find works the same as the find() built in function
str = "abracadabra"
print(str.find("ada"))

def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = 0
    ix1 = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix+ix1] != achar[ix1]:
            ix = ix+1
            ix1 = 0
            continue
        else:
            ix1 = ix1 + 1
        if ix1 == len(achar):
            found = True
    if found:
        return ix
    else:
        return -1

print(find("abracadabra", "ada"))