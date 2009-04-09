from distutils.core import setup

setup(name='clint_helpers',
      version='0.2',
      description='A little library of things that I keep having to recreate in Django apps',
      author='Clint Ecker',
      author_email='me@clintecker.com',
      url='http://github.com/clintecker/django-clint-helpers/tree/master',
      packages=['clint_helpers',],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )