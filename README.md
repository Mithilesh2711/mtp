# Personalized Dialogue Generation by History Filtration and Query Grouping

# Abstract
Personalized dialogue generation deals with generating a response to the query
that will signify the user’s chatting personality using the user’s dialogue history
for the training. This problem has gained much attention in recent years because

of the increasing use of personal assistance chatbots. This problem requires get-
ting responses by handling both the user’s dialogue history and the context of

the query for which the response will be generated. Since the dialogue history of
users are likely to be large and may contain noisy utterances, it is required to
handle the history by removing unwanted parts of the history and maintaining
the user’s personality pattern in its responses. Major previous works using the
user’s dialogue history randomly truncate the history to reduce the size. By such
random truncation, it not only misses the valuable data but also the model is

feeding with invaluable data, which left us with a scope of improvement by ade-
quately handling the history data. Inspired by this, we are finding the filtered

history of all users based on the responses that more closely signify the user’s
personality. Also, previously, to find the context of the query, similar queries from
the user history were taken or similar users were first extracted and then similar
query from these users were taken. Finding similar users with large history don’t
work, as encoding significant history in a single embedding vector misses much
information. To handle this issue, we are finding a group of queries with the same

context as the current one. In this way, we are finding query context and differ-
ent forms of query. These are our two major works in this paper and the result

proved that they have outperformed the previous works in all different levels of
evaluation metrics by the range of 10-25%.

Please do the operarion on main/model folder as this is the main project directory

# Preinstallation
First, install the python packages in your **Python3** environment:
```
  pip install -r requirements.txt
```

Then, you should download the pre-trained word embeddings to initialize the model training. We provide two word embeddings in the Google Drive:
- sgns.weibo.bigram-char, folloing [Li et al.](https://github.com/Embedding/Chinese-Word-Vectors), Chinese word embeddings pre-trained on Weibo. [Google Drive](https://drive.google.com/drive/folders/1UqUNtO5SVjyYTERfi4IvVTHopjFtqNNO?usp=sharing)
- Fasttext embeddings, English word embedding pre-trained on Reddit set. [Google Drive](https://drive.google.com/drive/folders/1UqUNtO5SVjyYTERfi4IvVTHopjFtqNNO?usp=sharing)

You can pre-train your own embeddings(with the same format, i.e., the standard txt format), and use it in the model.

After downloading, you should put the embedding file to the path ```EMB_FILE```.

# Data

You should provide the dialogue history of users for training the model. For convenience, we provide a very small subset of [PChatbot](https://github.com/qhjqhj00/SIGIR2021-Pchatbot) in the ```data/``` as the demo data. In the direcotry, each user's dialogue history is saved in one text file. Each line in the file should contain ```post text, user id of post, post timestamp, response text, user id of response, response timestamp, _, _ ```, with tab as the seperator. 

You can refer to ```seq2seq/dataset/perdialogDatasets.py``` for more details about the data processing.

If you are interested in the dataset [PChatbot](https://github.com/qhjqhj00/SIGIR2021-Pchatbot), please go to its official repository for more details. 

# Model Training

python runModel.py  --device 0  --bidirectional  --use_attn  --random_seed 2808  --src_vocab_size 40000  --tgt_vocab_size 40000  --data_path './FData40-100'  --word2vec_path './EMB_FILE/sgns.weibo.bigram-char-withheader'  --result_path './res.txt'

# Model Evaluation

python evaluate.py --result_path './res.txt' --emb_path './EMB_FILE/sgns.weibo.bigram-char-withheader'   
