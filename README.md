# Color Palette Generator
 A Flask web application to pick dominant and palette colors from an image URL using colorthief package.

<hr>
Home screen<br>
<img src="static/images/scr1.png" width="400">
<hr>
Enter image URL<br>
<img src="static/images/scr2.png" width="400">
<hr>
Get your image, dominant color and color palette displayed<br>
<img src="static/images/scr3.png" width="400">
<hr>

## Initial Setup
<hr>

Clone repo and create a virtual environment
```
$ git clone https://github.com/giedriusstankauskas/color-palette-generator.git
$ cd color-palette-generator
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install -r requirements.txt
```

Start Flask app.
```
$ (venv) export FLASK_APP=app.py
$ (venv) flask run
```
