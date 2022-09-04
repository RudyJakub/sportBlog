from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user, login_required
from sportblog.models import Article, User
from sportblog.editor_site.forms import ArticleForm


editor_site = Blueprint(
    'editor_site',
    __name__
)


@editor_site.route('/', methods=['GET'])
@login_required
def main():
    articles = Article.query.all()
    if current_user.is_editor == False:
        return redirect(url_for('auth.login'))
    return render_template('editor_site/main.html', articles=articles)


@editor_site.route('/create_article', methods=['GET', 'POST'])
@login_required
def create_article():
    if current_user.is_editor == False:
        return redirect(url_for('auth.login'))
    form = ArticleForm()
    if form.validate_on_submit():
        Article.create(form.title.data, form.content.data, current_user)
        flash('New article has been created!', 'success')
        print("Created!")
        return redirect(url_for('editor_site.main'))
    return render_template(
        'editor_site/create_article.html',
        title='New Article',
        form=form,
        legend='New Article'
        )
