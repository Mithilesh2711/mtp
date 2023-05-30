import os
from transformers import BertTokenizer, BertModel
import torch
import numpy as np

print("cuda: ",torch.cuda.is_available())

device = torch.device("cuda:0") 


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

# Load model from HuggingFace Hub
tokenizer = BertTokenizer.from_pretrained('shibing624/text2vec-base-chinese')
model = BertModel.from_pretrained('shibing624/text2vec-base-chinese')
model.to(device)

dir_list = os.listdir("D:\mtp\DHAP chinese\DHAP\TData2")
dir_list2 = os.listdir("D:\mtp\DHAP chinese\DHAP\FData40-100")
print(len(dir_list))
c=0

for file in dir_list:
    if(file in dir_list2): 
        c+=1
        print(file,c)
        continue
    if(os.path.getsize("D:/mtp/DHAP chinese/DHAP/TData2/"+file)>100000):
        resp = []
        resp_emb = []
        c=0
        with open("D:/mtp/DHAP chinese/DHAP/TData2/"+file, encoding='utf-8') as f:
            for line in f:
                c+=1
                resp.append(line.split('\t')[3])
                if(c%100==0):
                    encoded_input = tokenizer(resp, padding=True, truncation=True, return_tensors='pt')
                    encoded_input = encoded_input.to(device)

                    with torch.no_grad():
                        model_output = model(**encoded_input)
                        resp_emb1 = mean_pooling(model_output, encoded_input['attention_mask'])
                        resp_emb1 = resp_emb1.to(dtype=torch.long, device=torch.device("cpu"))
                        resp_emb1.tolist()
                        resp_emb+=resp_emb1
                    resp = []

        
        median = [0]*768
        
        for i in range(len(resp_emb)):
            for j in range(len(resp_emb[i])):
                median[j] += resp_emb[i][j]
        median = [x / len(resp_emb) for x in median]

        dist = []
        for i in range(len(resp_emb)):
            k = 0
            for j in range(len(resp_emb[i])):
                k += abs(median[j]-resp_emb[i][j])
            dist.append(k)
        
        
        idx = np.argsort(dist)
        c = 0

        if(len(idx)>400):
            idx = idx[0:400]

        print(file)

        
        with open("D:/mtp/DHAP chinese/DHAP/TData2/"+file, encoding='utf-8') as f, open("D:/mtp/DHAP chinese/DHAP/FData40-100/"+file,'a',encoding='utf-8') as file1:
            for line in f:
                if(c in idx):
                    file1.write(line)
                c+=1
    else:
        with open("D:/mtp/DHAP chinese/DHAP/TData2/"+file, encoding='utf-8') as f, open("D:/mtp/DHAP chinese/DHAP/FData40-100/"+file,'a',encoding='utf-8') as file1:
            for line in f:
                file1.write(line)



# count=0
# s="\t1\t0\n"
# with open("PchatbotL.release_ver",encoding='utf-8') as file:
#     for line in file:
#         if(count%2==0): 
#             line = line.strip('\n')
#             line = line + s

#             arr=line.split('\t')
#             if(len(arr[0].split(" "))>50 or len(arr[3].split(" "))>50): 
#                 count+=1
#                 continue

#             if(len(arr)==8 and arr[4].isnumeric()):
#                 with open("data/"+arr[4],'a',encoding='utf-8') as file1:
#                     file1.write(line)
#         count+=1