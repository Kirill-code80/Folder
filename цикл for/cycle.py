spisok = [16, 46, 26, 36]
r_obj = range(len(spisok))
e_obj = enumerate(spisok)
for i in r_obj:
    if i == 1:
        break
for i in e_obj:
    if i[0] == 1:
        break
for i in r_obj:
    print(i)
for i in e_obj:
    print(i)

    

 