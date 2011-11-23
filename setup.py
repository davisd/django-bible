from distutils.core import setup

setup(
    name='django-bible',
    version='1.0',
    author='David Davis',
    author_email='davisd@davisd.com',
    packages=['bible'],
    data_files=[('.',['LICENSE'])],
    url='http://www.davisd.com/projects/django-bible/',
    license='LICENSE',
    description='django-bible is a Python package / django app for interfacing' \
        ' with the Holy Bible.',
    long_description=open('README').read()
)

