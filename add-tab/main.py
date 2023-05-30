import os
arr = sorted(os.listdir('data'))
for k in arr:
    str=""
    f1 = open('data/'+k,encoding='utf-8')
    for l in f1.readlines():
        p = l.split(' ')
        f=0
        for w in range(0,len(p)):
            if(f==1):
                f=0
                continue
            if(p[w].isnumeric() and p[w+1].isnumeric()):
                str = str + "\t" + p[w] + "\t" + p[w+1] + "\t"
                f=1
            elif(w==len(p)-2):
                str+= p[w]+"\t"
            else:
                str = str + p[w]+" "
    f1.close()
    with open('data/'+k, 'w', encoding='utf-8') as file:
        file.writelines( str )
        

