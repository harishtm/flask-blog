from flask import render_template, request,flash, redirect, url_for
from app import app, db
from app.models import Post



@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        print "=====>", request.form
        post=Post(request.form['title'], request.form['body'])
        db.session.add(post)
        db.session.commit()
        flash('New entry was successfully posted')
        return redirect("/", code=302)
    return render_template('add.html')


@app.route('/' )
def index():
    #post = Post.query.filter_by(id=10)
    post = Post.query.filter_by()
    return render_template('index.html', post=post)

