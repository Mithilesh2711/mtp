import os


count=0
s="\t1\t0\n"
dir_list = os.listdir("data")
print(len(dir_list))
with open("PchatbotL.release_ver",encoding='utf-8') as file:
    for line in file:
        if(count%2==0): 
            line = line.strip('\n')
            line = line + s

            arr=line.split('\t')
            if(len(arr[0].split(" "))<10 or len(arr[3].split(" "))>100): 
                count+=1
                continue

            if(len(arr)==8 and arr[4].isnumeric() and len(arr[0].split(" "))>=25 and len(arr[3].split(" "))<=50):
                with open("data25-50/"+arr[4],'a',encoding='utf-8') as file2:
                    file2.write(line)
            
            if(len(arr)==8 and arr[4].isnumeric() and len(arr[0].split(" "))>=10 and len(arr[3].split(" "))<=50):
                with open("data10-50/"+arr[4],'a',encoding='utf-8') as file3:
                    file3.write(line)

            if(len(arr)==8 and arr[4].isnumeric() and len(arr[0].split(" "))>=40 and len(arr[3].split(" "))<=100):
                with open("data40-100/"+arr[4],'a',encoding='utf-8') as file4:
                    file4.write(line)

            # if(len(arr)==8 and arr[4].isnumeric()):
            #     with open("data/"+arr[4],'a',encoding='utf-8') as file1:
            #         file1.write(line)
        count+=1


# import translators as ts          
# dir_list = os.listdir("data2")
# with open("PchatbotL.release_ver",encoding='utf-8') as file:
#     for line in file:
#         if(count%2==0): 
#             line = line.strip('\n')
#             line = line + s

#             arr=line.split('\t')
#             if(arr[4] in dir_list or len(arr[0].split(" "))>20 or len(arr[3].split(" "))>20): 
#                 count+=1
#                 continue
#             arr[0]=ts.google(arr[0], from_language='zh', to_language='en')
#             arr[3]=ts.google(arr[3], from_language='zh', to_language='en')
#             line = "\t".join(arr)
#             line=line
#             if(len(arr)==8 and arr[4].isnumeric()):
#                 with open("data2/"+arr[4],'a',encoding='utf-8') as file1:
#                     file1.write(line)
#         count+=1