from flask import Flask, render_template, url_for, redirect
from forms import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY']='f6f18f2b875e6effe3f747230b0d1ea1742e781f23ec1603'



courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    return render_template('index.html', form=form)