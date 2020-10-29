from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'some string no one can guess'


class DeleteForm(FlaskForm):
    blank = StringField("작성", validators=[DataRequired()])
    delete = SubmitField('삭제')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/board')
def board():
    myform = DeleteForm()
    return render_template('board.html', form=myform)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/author')
def author():
    return render_template('author.html')


@app.route('/writing')
def writing():
    return render_template('writing.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
