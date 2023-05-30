# Personalized Dialogue Generation by History Filtration and Query Grouping

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
