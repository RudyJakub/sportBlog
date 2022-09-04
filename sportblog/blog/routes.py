from flask import render_template, request, Blueprint


blog = Blueprint('blog', __name__)


@blog.route('/')
@blog.route('/home')
def home():
    return render_template('blog/home.html')


@blog.route('/about')
def about():
    return render_template('blog/about.html')
