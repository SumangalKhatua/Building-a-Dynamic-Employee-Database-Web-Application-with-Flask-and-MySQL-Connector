from flask import Flask,render_template,url_for,redirect,request,session
import mysql.connector


connection=mysql.connector.connect(host='localhost',port='3306',database='company',user='root',password='')

cursor=connection.cursor()

app = Flask(__name__)
app.secret_key = "super secret key"



@app.route("/logout")
def logout():
    return redirect(url_for("login"))




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login",methods=["GET","POST"])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor.execute('select * from users  username=%s And password=%s',(username,password))
        record= cursor.fetchone()
        if record:
            session["login"]=True
            session["username"]=record[1]
            return redirect(url_for('home'))
        else:
            msg='Incorrect username or password.Try again'
    return render_template('index.html',msg=msg)
            
            


@app.route("/IT")
def it():
    cursor.execute("select * from employee where Department='IT'")
    value=cursor.fetchall()
    
    return render_template("registration.html",data=value,name="IT")


@app.route("/HR")
def hr():
    cursor.execute("select * from employee where Department='HR'")
    value=cursor.fetchall()
    
    return render_template("registration.html",data=value,name="HR")


@app.route("/Finance")
def finance():
    cursor.execute("select * from employee where Department='Finance'")
    value=cursor.fetchall()
    
    return render_template("registration.html",data=value,name="Finance")

    
if __name__ == "__main__":
    app.run(debug=True)