import numpy as np

#Read data
import csv
import json
#preprocessing
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def write_json(nama_file, tipe="w"):
    try:
        with open("bobot.json", "w") as json_file:
            json.dump(ind, json_file)
        return True
    except:
        return False

def read_csv(nama_file):
    with open(nama_file, newline='\n') as csvfile:
        data = []
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in spamreader:
            data.append(row)
        return data

def write_csv(nama_file, isi, tipe='w'):
    'tipe=w; write; tipe=a; append;'
    with open(nama_file, mode=tipe) as tbl:
        tbl_writer = csv.writer(tbl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in isi:
            tbl_writer.writerow(row)

def readJSON(namaFile, encoding="urf8"):

    campur = []
    with open(namaFile, encoding="utf8") as json_file:    
        data = json.load(json_file)
        for d in data:
            campur += [f"{d['judul']} {d['isi']} "]
    return campur

def tokenisasi(txt):
    tmp = ""
    for ch in txt:
        if not ch.isalpha():
            tmp += " "
        else:
            tmp += ch
    return tmp

def preprosesing(txt):
    #tokenisasi
    txt = tokenisasi(txt)

    # generate stopword
    SWfactory = StopWordRemoverFactory()
    stopword = SWfactory.create_stop_word_remover()

    # generate stemmer
    Sfactory = StemmerFactory()
    stemmer = Sfactory.create_stemmer()
    hasil = ''
    for i in txt.split():
        # Menghilangkan Kata tidak penting
        stop = stopword.remove(i)

        # mengubah ke kata dasar
        stem = stemmer.stem(stop)
        hasil += stem  + ' '
    return hasil.split()

anu = input("pre?")
if (anu == "y"):
    namaFile1 = "items_liputan6_2.json"

    data1 = readJSON(namaFile1)

    pre = []
    c = 1;
    for d in data1:
        print(c/jumlah, "%")
        #calling pre func
        tmp = [preprosesing(d)]
        pre += tmp
        c+=1
        
    raise Exception("Selesai")
pre = read_csv("output_pre.csv")

# get list of each word
jumlah = len(pre) #jumlah doc
words = []
for d in pre:
    for word in d:
        if not word in words:
            words.append(word)

tf = [] # doc
idf = [] # doc
tfidf = []
for w in words:
    tmp = [] #word
    df = 0
    #tf
    for d in pre:
        if w in d:
            #ini buat idf
            df +=1
        #ini buat tf
        tmp.append(d.count(w))
    tmp_idf = np.log(jumlah/df)
    tf.append(tmp)
    idf.append(tmp_idf)

    #tfidf
    tfidf.append(np.array(tmp) * tmp_idf)

#TINGGAL LOAD BOBOT.JSON SAMA SIMILIARITY
