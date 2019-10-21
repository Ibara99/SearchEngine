import numpy as np

#Read data
import json
#preprocessing
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

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

namaFile1 = "items_liputan6_2.json"

data1 = readJSON(namaFile1)

pre = []
words = []
jumlah = len(data1) #jumlah doc
c = 1;
for d in data1:
    print(c/jumlah, "%")
    #calling pre func
    tmp = [preprosesing(d)]
    pre += tmp
    
    # get list of each word
    for w in tmp:
        if not w in words:
            words.append(w)
    c+=1
    
raise Exception("Selesai")


tf = [] # doc
idf = [] # doc
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
    tf.append(tmp)
    idf.append((np.log(jumlah/df)))
