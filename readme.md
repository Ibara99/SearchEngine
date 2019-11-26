# Simple Search Engine - Dokumentasi

> Repo ini merupakan tugas mata kuliah Teknologi Mesin Pencarian pada Universitas Trunojoyo Madura, tapel 2019/2020. Mata kuliah ini diampu oleh bu Suzan dan dilakukan berkelompok. 

> Anggota kelompok : 1) Shelly Linggarwati, 2) Bimo Dwi M., dan 3) saya;

***

## Hal hal yang perlu dipersiapkan

Bahasa pemrograman yang digunakan pada projek ini adalah Python dengan library (bukan built-in):

1. Scrapy 1.7.3; digunakan untuk proses Scraping/Crawling website;
2. Sastrawi 1.0.1; digunakan untuk Text Processing
3. Numpy 1.17.4; digunakan untuk memudahkan saat mengolah data
4. Flask 1.1.1 dan Jinja2 2.10.3; digunakan untuk menampilkan hasil berupa website sederhana


Tema yang digunakan pada project Mesin Pencarian ini adalah "Jagung". Beberapa website yg digunakan pada project ini setidaknya ada 4 website, yaitu:

1. Detik
2. liputan 6
3. Merdeka
4. tentangjagung.blogspot.com

***

Terdapat tiga folder utama; yaitu :

1. tmp
2. __preprocessing
3. website

ketiganya memiliki peran masing-masing;

## Folder tmp

merupakan folder untuk menjalankan Spider atau crawling Scrapy;

## Folder preprocessing;

merupakan folder untuk melakukan proses pembersihan data, yang meliputi Tokenisasi, Stemming, Stopword removal, dan lain sebagainya. Penjelasan mengenai proses pembersihan data dapat dilihat pada project saya yang lain, yaitu Simple Web Crawling.

## website

merupakan folder untuk menjalankan app Flask;

# Kekurangan:

proses pencarian masih lama karena masih menghitung kemiripan dokumen. Seharusnya masih bisa ditingkatkan lagi, misalnya dilakukan proses indexing;

# Memiliki Pertanyaan?

Hubungi saya melalui Email (liat bio).