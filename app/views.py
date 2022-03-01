# The views file contains the routes to webpages and might also house logic for your web app.
from flask import render_template, flash, redirect, url_for
from app.forms import NewStudentForm
import sqlite3

from app import app


@app.route("/")
def index():
    con = sqlite3.connect("app/database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template('index.html', rows=rows)


@app.route("/add-new", methods=["GET", "POST"])
def addNew():
    form = NewStudentForm()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        city = form.city.data
        pincode = form.pincode.data

        # con = sqlite3.connect('app/database.db')
        # cur = con.cursor()
        #
        # qry = "INSERT INTO students (name,address,city,pincode) VALUES (?, ?, ?, ?)"
        # val = (name, address, city, pincode)
        # cur.execute(qry, val)
        #
        # con.commit()
        # msg = "Record successfully added" + str(cur.rowcount)
        #
        # flash(msg, 'info')
        # return redirect(url_for('index'))
        try:
            # decided to use sqlAlchemy
            con = sqlite3.connect('app/database.db')
            cur = con.cursor()

            qry = "INSERT INTO students (name,address,city,pincode) VALUES (?, ?, ?, ?)"
            val = (name, address, city, pincode)
            cur.execute(qry, val)

            con.commit()
            msg = str(cur.rowcount) + "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            flash(msg, 'info')
            return redirect(url_for('index'))
            # con.close()

    return render_template('new-student.html', form=form)
