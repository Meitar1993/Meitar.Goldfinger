from flask import render_template, request, redirect, Blueprint
import mysql.connector

Assignment10 = Blueprint('Assignment10', __name__,
                         static_folder='static',
                         static_url_path='/Assignment10',
                         template_folder='templates')

# ----------- DATABASE CONNECTION ----------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root123',
                                         database='web_cv')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# ----------- GET ----------- #
@Assignment10.route("/Assignment10")
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('Assignment10.html', users=query_result)

# ----------- INSERT ----------- #
@Assignment10.route("/Insert_user", methods=['GET', 'POST'])
def insert():
    FullName = request.form['FullName']
    UserName = request.form['UserName']
    query = "insert into users(FullName, UserName) values ('%s', '%s')" % (FullName, UserName)
    interact_db(query=query, query_type='commit')
    return redirect('/Assignment10')

# ----------- UPDATE ----------- #
@Assignment10.route("/Update_user", methods=['POST'])
def update():
    FullName = request.form['FullName']
    UserName = request.form['UserName']
    query = "update users set UserName = '%s' where FullName='%s';" % (FullName, UserName)
    interact_db(query, query_type='commit')
    return redirect("/Assignment10")

# ----------- DELETE ----------- #
@Assignment10.route("/Delete_user", methods=['POST'])
def delete():
    FullName = request.form['FullName']
    query = "delete from users where FullName='%s';" % FullName
    interact_db(query, query_type='commit')
    return redirect("/Assignment10")


