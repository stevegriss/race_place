# import sqlite3

# conn = sqlite3.connect('database.db')
# print('db is connected')

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")
# conn.close()
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def home():
      return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      nm = request.form['nm']
      addr = request.form['add']
      city = request.form['city']
      pin = request.form['pin']

      db = db_connection()

      try:
         db.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)", (nm,addr,city,pin))
         db.commit()
         db.close()
         msg = "Record successfully added"

      except:
         msg = "error in insert operation"

      finally:
         return render_template("result.html", msg = msg)

         # with sql.connect("database.db") as con:
         #    cur = con.cursor()
         #    cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)", (nm,addr,city,pin))

         #    con.commit()
         #    msg = "Record successfully added"

      # except:
      #    con.rollback()
      #    msg = "error in insert operation"

      # finally:
      #    return render_template("result.html", msg = msg)
      #    con.close()

@app.route('/list')
def list():
   db = db_connection()

   # con = sql.connect("database.db")
   # con.row_factory = sql.Row
   
   # cur = con.cursor()
   rows = db.execute("select * from students").fetchall()
   
   # rows = db.fetchall()
   return render_template("list.html", rows = rows)

if __name__ == "__main__":
   app.run(debug=True)
   app.run(host="0.0.0.0", port=5000)
