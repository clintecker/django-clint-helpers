from django import template
try:
  from hashlib import md5 as gen_md5
  from hashlib import sha1 as gen_sha
  hlib = True
except:
  import md5 as gen_md5
  import sha as gen_sha
  hlib = False
 
register = template.Library()
 
@register.filter
def md5(value):
  "Returns the hex digest of an MD5 hash of a string"
  if hlib:
    h = gen_md5(value)
  else:
    h = gen_md5.new(value)
  return h.hexdigest()
    
@register.filter
def gen_sha1(value):
  "Returns the hex digest of an SHA-1 hash of a string"
  if hlib:
    h = gen_sha(value)
  else:
    h = gen_sha.new(value)
  return h.hexdigest()