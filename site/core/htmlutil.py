import re
from django.utils.html import strip_spaces_between_tags
from django.conf import settings
 
RE_MULTISPACE = re.compile(r"\s{2,}")
RE_NEWLINE = re.compile(r"\n")

def minify_html(html):
    html = strip_spaces_between_tags(html.strip())
    html = RE_MULTISPACE.sub(" ", html)
    html = RE_NEWLINE.sub("", html)
    return html