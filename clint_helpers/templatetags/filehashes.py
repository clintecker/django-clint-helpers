from django import template
register = template.Library()
from django.conf import settings
import os

hashlib = False
try:
  from hashlib import md5
  from hashlib import sha1
  hashlib = True
except:
  import md5
  import sha
 
def assetmd5(value):
    
    
    if hashlib:
      h = md5(value)
    else:
      h = md5.new(value)
    return h.hexdigest()

class MediaFileHashNode(template.Node):
    def __init__(self, file_path):
        self.file_path = file_path
    def render(self, context):
        full_path = settings.MEDIA_ROOT + file_path
        print full_path

def do_mediafilehash(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, file_path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return MediaFileHashNode(file_path[1:-1])

register.filter('mediafilehash', assetmd5)