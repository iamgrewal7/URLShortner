from flask import request, render_template, redirect, abort
from forms import UrlForm
from lib.url_shortner import UrlShortner
from settings import db, app
from models import URL
import sys

BASE_URL = 'http:localhost:5000'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    short_url = None
    print(form.url.data, file=sys.stdout)
    print(form.validate_on_submit(), file=sys.stdout)
    if form.validate_on_submit():
        existing_url = URL.query.filter_by(url=form.url.data).first()
        print(existing_url, file=sys.stdout)
        if existing_url:
            short_url = f'{BASE_URL}/{UrlShortner.id_to_url(existing_url.id)}'
        else:
            new_url = URL(url=form.url.data)
            db.session.add(new_url)
            db.session.commit()
            short_url = f'{BASE_URL}/{UrlShortner.id_to_url(new_url.id)}'
    print(short_url, file=sys.stdout)
    return render_template('index.html', form=form, short_url=short_url)

@app.route('/<path:short_url>')
def redirect_url(short_url):
    try:
        _id = UrlShortner.url_to_id(short_url)
        obj = URL.query.filter_by(id=_id).first()
    except OverflowError:
        return render_template('404.html')
                
    return redirect(obj.url) if obj else render_template('404.html')
    

if __name__ == '__main__':
    app.run()
