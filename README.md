# REST API untuk e-Learning UTM

Merupakan API sederhana yang dibangun menggunakan Flask v2 dengan Python 3.6+. 

API ini dibuat sebagai studi kasus untuk memenuhi tugas Kerja Praktek.

## Import Database

Buat database lalu impor SQL yang telah ada.

```sql
CREATE DATABASE elearning;
USE elearning;
SOURCE path/to/elearning.sql;
```

## Instalasi

Instal requirements menggunakan pip di dalam virtual environment.

### Windows
```bash
python -m venv myenv
.\myenv\Scripts\activate
pip install requirements.txt
```

### Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
```

## Konfigurasi .env

Ubah isi berkas `.env` dan sesuaikan.

```
MYSQL_HOST = 'YOUR_HOST'
MYSQL_USER = 'USERNAME'
MYSQL_PASSWORD = 'PASSWORD'
MYSQL_DB = 'elearning'
```

## Running API
Untuk menjalankan API dapat menggunakan perintah berikut.
```bash
flask run
```

## Deployment

Untuk deployment di OS Linux menggunakan gunicorn seperti berikut.

```bash
pip3 install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

Opsi deployment lainnya dapat dilihat di [Flask - Deployment Option](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html) .
