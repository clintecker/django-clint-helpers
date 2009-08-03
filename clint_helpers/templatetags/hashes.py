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
 
def md5_filter(value):
    "Returns the hex digest of an MD5 hash of a string"
    if hashlib:
      h = md5(value)
    else:
      h = md5.new(value)
    return h.hexdigest()

def sha1_filter(value):
    "Returns the hex digest of an SHA-1 hash of a string"
    if hashlib:
      h = sha1(value)
    else:
      h = sha.new(value)
    return h.hexdigest()

register.filter('md5', md5_filter)
register.filter('sha1', sha1_filter)