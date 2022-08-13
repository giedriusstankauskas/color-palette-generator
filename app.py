from flask import Flask, render_template
from models import UploadForm
from color_thief import palette_generator
import datetime

app = Flask(__name__)
app.secret_key = "these boots are made for walking"


@app.route('/', methods=["GET", "POST"])
def index():
    year = datetime.datetime.now().year
    form = UploadForm()
    if form.validate_on_submit():
        link = form.image_url.data
        dominant_color, color_palette = palette_generator(link)
        return render_template("palette.html", dominant_color=dominant_color, palette=color_palette, link=link, year=year)
    return render_template("index.html", form=form, year=year)


if __name__ == "__main__":
    app.run(debug=True)
