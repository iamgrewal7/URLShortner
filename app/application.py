from flask import request, render_template, redirect, abort
from app.forms import UrlForm
from app.lib.url_shortner import UrlShortner
from app.settings import db, app
from app.models import URL

BASE_URL = 'https://mighty-waters-06458.herokuapp.com/ '

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    short_url = None
    if form.validate_on_submit():
        existing_url = URL.query.filter_by(url=form.url.data).first()
        if existing_url:
            short_url = f'{BASE_URL}/{UrlShortner.id_to_url(existing_url.id)}'
        else:
            new_url = URL(url=form.url.data)
            db.session.add(new_url)
            db.session.commit()
            short_url = f'{BASE_URL}/{UrlShortner.id_to_url(new_url.id)}'
    return render_template('index.html', form=form, short_url=short_url)

@app.route('/<path:short_url>')
def redirect_url(short_url):
    try:
        _id = UrlShortner.url_to_id(short_url)
        obj = URL.query.filter_by(id=_id).first()
    except OverflowError:
        return render_template('404.html')
                
    return redirect(obj.url) if obj else render_template('404.html')
    