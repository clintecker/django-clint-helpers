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
        full_path = settings.MEDIA_ROOT + self.file_path
        if os.path.exists(full_path):
            value = file(full_path).read()
            if hashlib:
              h = md5(value)
            else:
              h = md5.new(value)
            h = h.hexdigest()
            versioned_file = settings.MEDIA_ROOT + self.file_path.replace('.', '.%s.' % (h,))
            versioned_resource = settings.MEDIA_URL + self.file_path.replace('.', '.%s.' % (h,))
            if os.path.exists(versioned_file):
                return versioned_resource
        return settings.MEDIA_URL + self.file_path

def do_mediafilehash(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, file_path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    if not (file_path[0] == file_path[-1] and file_path[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return MediaFileHashNode(file_path[1:-1])

register.tag('media_file_hash', do_mediafilehash)