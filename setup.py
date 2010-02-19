from setuptools import setup

setup(
    name='bleach',
    version='0.1',
    description='An easy whitelist-based HTML-sanitizing tool.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='james@mozilla.com',
    url='http://github.com/jsocol/bleach',
    license='BSD',
    packages=['bleach', 'django'],
    include_package_Data=True,
    zip_safe=False,
    install_requires=['html5lib'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
