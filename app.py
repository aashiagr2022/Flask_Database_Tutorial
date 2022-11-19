from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

email_globe = ""


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anon@cute2012'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = (str)(details['fname'])
        lastName = (str)(details['lname'])
        email = (str)(details['email'])
        age = (str)(details['age'])
        cur = mysql.connection.cursor()

        print("Came here")

        cur.execute(f'Insert into MyAppUsers values ("{firstName}" , "{lastName}","{email}",{age});')

        mysql.connection.commit()
        cur.close()
    return render_template('index.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        details = request.form
        email = (str)(details['email'])

        print("came here")

        cur = mysql.connection.cursor()

        print("Email is", email)

        cur.execute(f'Select * from MyAppUsers where email = "{email}";')
        rows = cur.fetchall() 

        if rows == None:
            print("There are no results for this query")
        else:
            print("rows are", rows[0])
            global email_globe
            email_globe = rows[0][2]
            return render_template("display.html", rows = rows[0])


        mysql.connection.commit()
        cur.close()

    return render_template('login.html')

@app.route('/modify.html', methods=['GET', 'POST'])
def modify():
    
    
    if request.method == "POST":

        print("came to modify")

        form = request.form

        details = request.form
        firstName = (str)(details['fname'])
        lastName = (str)(details['lname'])
        email = (str)(details['email'])
        age = (str)(details['age'])

        print("came here")

        cur = mysql.connection.cursor()

        print("Email is", email)

        global email_globe
        email_globe = email
        cur.execute(f'Update MyAppUsers set firstName = "{firstName}", lastName = "{lastName}", age = {age} where email = "{email}";')

        print("Change made")

        mysql.connection.commit()
        cur.close()

    return render_template('modify.html')
    
@app.route("/delete.html", methods=['GET', 'POST'])
def delete():

    if request.method == "POST":

        print("Came for delete")
        global email_globe
        curr_em = email_globe
        cur = mysql.connection.cursor()

        print("Email is", email_globe)
        
        print(f'Delete from myappusers where email = "{curr_em}";')
        
        cur.execute(f'Delete from myappusers where email = "{curr_em}";')

        print("yes")

        mysql.connection.commit()
        cur.close()
    
    return render_template("delete.html")



if __name__ == '__main__':
    app.run()