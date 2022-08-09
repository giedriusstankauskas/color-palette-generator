from flask import Flask, render_template
from urllib.request import urlopen
import io
from colorthief import ColorThief
import ssl
from models import UploadForm

app = Flask(__name__)
app.secret_key = "these boots are made for walking"

# code line to avoid [SSL: CERTIFICATE_VERIFY_FAILED] error on mac
ssl._create_default_https_context = ssl._create_unverified_context

link_vilnius = "https://www.govilnius.lt/images/5e7a4e63386e6abfe189ed63?w=1200&h=630"


def palette_generator(link):
    fd = urlopen(link)
    # fd = open('static/images/vilnius.jpeg', "rb")
    f = io.BytesIO(fd.read())
    color_thief = ColorThief(f)
    dominant_color = color_thief.get_color(quality=1)
    color_palette = color_thief.get_palette(quality=1)
    return dominant_color, color_palette


@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        link = form.image_url.data
        dominant_color, color_palette = palette_generator(link)
        return render_template("palette.html", dominant_color=dominant_color, palette=color_palette)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
