from urllib.request import urlopen
import io
from colorthief import ColorThief
import ssl

# code line to avoid [SSL: CERTIFICATE_VERIFY_FAILED] error on mac
ssl._create_default_https_context = ssl._create_unverified_context


def palette_generator(link):
    fd = urlopen(link)
    f = io.BytesIO(fd.read())
    color_thief = ColorThief(f)
    dominant_color = color_thief.get_color(quality=1)
    color_palette = color_thief.get_palette(quality=1)
    return dominant_color, color_palette
