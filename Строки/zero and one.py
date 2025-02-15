a="0110"
b="1010"
def _cipher(a,b):
    s=""
    for i in range(len(a)):
        if a[i]==b[i]:
            s+="0"
        else:
            s+="1"
    return s
def xor_uncipher(a,b):
    return _cipher(a,b)

c=_cipher(a,b)
print(c)
print(xor_uncipher(c,b))
    
    
