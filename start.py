from flask import Flask,render_template,request,  redirect
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        email=request.form.get('email')
       
        conn=sqlite3.connect('databases.db')
        c=conn.cursor()
        sql_query=f"""SELECT * FROM user WHERE name='{username}' AND password='{password}'"""
        c.execute(sql_query)
        
        results=c.fetchall()
        c.close()
        return render_template('refer.html',headings=username,mylist=results)
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        conn=sqlite3.connect('databases.db')
        c=conn.cursor()
        username=request.form.get('username')
        password=request.form.get('password')
        reenter=request.form.get('re-enter')
        email=request.form.get('email')
        contact=request.form.get('contact')
        
        if  not username :
            return "Please enter your username"
        if  not password :
            return "Please enter your password"
        if  not reenter :
            return "Please enter your password again"
        if password !=reenter:
            return "Password notmatched"
        if  not email :
            return "Please enter your email"
        if  not contact :
            return "Please enter your contact"
        
        
        sql_query=f"""INSERT INTO user VALUES(
                    '{username}',
                    '{password}',
                    '{email}',
                    '{contact}'
                    )"""
        c.execute(sql_query)
        conn.commit()
        return "Congratulations for your registration"  
    
@app.route('/<username>',methods=['GET','POST'])
def user_in(username):
    if request.method=='GET':
        return render_template('inside.html')
    else:   
        conn=sqlite3.connect('databases.db')
        c=conn.cursor()
        problem=request.form.get('problem')
        pin_code=request.form.get('pincode')
        sql_query=f"SELECT name,contact,email FROM {problem} WHERE pincode='{pin_code}'"
        c.execute(sql_query)
        conn.commit()
        result=c.fetchall()
        column_name=['Username', 'contact','gmail']
        conn.close()
        return render_template('view1.html',headings=column_name,mylist=result)
    
    
              
@app.route('/fjhjfdfcfenhnejhbe3uhiu3emke4848',methods=['GET','POST'])
def A_login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        conn=sqlite3.connect('databases.db')
        c=conn.cursor()
        c.execute(f"""SELECT * FROM user 
                    """)
        result=c.fetchall()
        column_name=['Username', 'Password', 'Email', 'Contact']
        conn.close()
        return render_template('view.html',headings=column_name,mylist=result)       
    
@app.route('/sms>',methods=['GET','POST'])
def sms():
    resp=MessagingResponse()
    resp.message("Thanks for the sms")
    
    print(str(resp))
    
    return (str(resp))
 