from django import template
try:
  from hashlib import md5
  from hashlib import sha1
  hashlib = True
except:
  import md5, sha
  hashlib = False
 
register = template.Library()
 
@register.filter
def md5(value):
    "Returns the hex digest of an MD5 hash of a string"
    if hashlib:
      h = md5(value)
    else:
      h = md5.new(value)
    return h.hexdigest()
    
@register.filter
def sha1(value):
    "Returns the hex digest of an SHA-1 hash of a string"
    if hashlib:
      h = sha1(value)
    else:
      h = sha.new(value)
    return h.hexdigest()