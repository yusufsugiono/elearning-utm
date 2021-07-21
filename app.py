from flask import Flask, request
from markupsafe import escape
from flask_mysqldb import MySQL, MySQLdb
from dotenv import load_dotenv
import os

# Memanggil konfigurasi .env
load_dotenv()

app = Flask(__name__)

# Konfigurasi Database
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

# Menghubungkan Database
mysql = MySQL(app)

# Routes
@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        # Menangani method POST
        query = mysql.connection.cursor()
        try:
            # Ambil data
            url = request.json['url']
            judul = request.json['judul']
            pemateri = request.json['pemateri']
            matakuliah = request.json['matakuliah']
            semester = request.json['semester']

            query.execute("""
                INSERT INTO video
                VALUES (NULL, %s, %s, %s, %s, %s)
                """, (
                    url,
                    judul,
                    pemateri,
                    matakuliah,
                    semester
                    ))
            result = mysql.connection.insert_id()
        except:
            result = False

        mysql.connection.commit()
        query.close()
        if result :
            return {
                'status' : 'success',
                'inserted_id' : result
            }, 201
        else:
            return {
                'status' : 'fail',
                'message' : 'Gagal menyimpan data!'
            }, 400
    else:
        # Menangani method GET
        query = mysql.connection.cursor()
        query.execute("""
            SELECT * FROM video
            """)
        data = query.fetchall()
        query.close()

        result = []
        for item in data:
            result.append({
                    'id' : item[0],
                    'url' : item[1],
                    'judul' : item[2],
                    'pemateri' : item[3],
                    'matakuliah' : item[4],
                    'semester' : item[5]
                })

        return {
            'status' : 'success',
            'total' : len(result),
            'data' : result
        }

@app.route('/video/<id>', methods=['GET', 'PUT', 'DELETE'])
def videoWithId(id):
    query = mysql.connection.cursor()
    query.execute("""
        SELECT * FROM video WHERE id = %s
        """, (escape(id),))
    data = query.fetchall()
    query.close()

    if len(data) < 1:
        return {
            'status' : 'fail',
            'message' : 'Data tidak ditemukan!'
        }, 404

    if request.method == "GET":
        result = []
        for item in data:
            result.append({
                    'id' : item[0],
                    'url' : item[1],
                    'judul' : item[2],
                    'pemateri' : item[3],
                    'matakuliah' : item[4],
                    'semester' : item[5]
                })

        return {
            'status' : 'success',
            'data' : result
        }
    elif request.method == 'PUT':
        try:
            query = mysql.connection.cursor()
            # Ambil data
            url = request.json['url']
            judul = request.json['judul']
            pemateri = request.json['pemateri']
            matakuliah = request.json['matakuliah']
            semester = request.json['semester']

            query.execute("""
                UPDATE video SET url=%s , judul=%s, pemateri=%s, matakuliah=%s, semester=%s
                WHERE id=%s
                """, (
                    url,
                    judul,
                    pemateri,
                    matakuliah,
                    semester,
                    escape(id)
                    ))
            mysql.connection.commit()
            query.close()
            return {
                'status' : 'success',
                'message' : 'Data berhasil diperbarui!'
            }, 200
        except:
            return {
                'status' : 'fail',
                'message' : 'Gagal memperbarui data!'
            }, 400

    else:
        try:
            query = mysql.connection.cursor()
            

            query.execute("""
                DELETE FROM video WHERE id=%s
                """, (
                    escape(id),
                    ))
            mysql.connection.commit()
            query.close()
            return {
                'status' : 'success',
                'message' : 'Data berhasil dihapus!'
            }, 200
        except:
            return {
                'status' : 'fail',
                'message' : 'Gagal menghapus data!'
            }, 400

@app.route('/video/semester/<smt>')
def videoWithSmt(smt):
    query = mysql.connection.cursor()
    query.execute("""
        SELECT * FROM video WHERE semester = %s
        """, (escape(smt),))
    data = query.fetchall()
    query.close()

    if len(data) < 1:
        return {
            'status' : 'fail',
            'message' : 'Data tidak ditemukan!'
        }, 404

    result = []
    for item in data:
        result.append({
                'id' : item[0],
                'url' : item[1],
                'judul' : item[2],
                'pemateri' : item[3],
                'matakuliah' : item[4],
                'semester' : item[5]
            })

    return {
        'status' : 'success',
        'data' : result
    }

@app.route('/video/matakuliah/<mk>')
def videoWithMk(mk):
    query = mysql.connection.cursor()
    query.execute("""
        SELECT * FROM video WHERE matakuliah = %s
        """, (escape(mk),))
    data = query.fetchall()
    query.close()

    if len(data) < 1:
        return {
            'status' : 'fail',
            'message' : 'Data tidak ditemukan!'
        }, 404

    result = []
    for item in data:
        result.append({
                'id' : item[0],
                'url' : item[1],
                'judul' : item[2],
                'pemateri' : item[3],
                'matakuliah' : item[4],
                'semester' : item[5]
            })

    return {
        'status' : 'success',
        'data' : result
    }

@app.route('/search')
def searchByKeyword():
    keyword = request.args.get('keyword')
    query = mysql.connection.cursor()
    query.execute("""
        SELECT * FROM video
        WHERE judul LIKE %s
        """, ('%'+keyword+'%',))
    data = query.fetchall()
    query.close()

    if len(data) < 1:
        return {
            'status' : 'fail',
            'message' : 'Data tidak ditemukan!'
        }, 404

    result = []
    for item in data:
        result.append({
                'id' : item[0],
                'url' : item[1],
                'judul' : item[2],
                'pemateri' : item[3],
                'matakuliah' : item[4],
                'semester' : item[5]
            })

    return {
        'status' : 'success',
        'data' : result
    }

# Run app
if __name__ == '__main__':
    app.run()