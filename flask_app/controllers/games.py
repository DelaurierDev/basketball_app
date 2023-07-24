from flask_app import app
from flask import render_template, redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.game import Game

@app.route("/view")
def viewall():
    if 'user_id' not in session:
        flash('Must login')
        return redirect('/')
    
    return render_template("allgames.html")

@app.route("/new")
def new():
    if 'user_id' not in session:
        flash('Must login')
        return redirect('/')
    
    return render_template("newgame.html")