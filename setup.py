from setuptools import setup
from setuptools import find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'pygithub>=1.39',
    'click>=6.7',
    'hues>=0.2.2'
]

setup(
    name='thanksforked',
    version='0.0.1',
    description="Thanks with a ⭐️ the projects you forked",
    long_description=readme,
    author="Etienne Napoleone",
    author_email='etienne_napo@hotmail.com',
    # download_url=
    url='https://github.com/etienne-napoleone/thanksforked',
    project_urls={
        'Source': 'https://github.com/etienne-napoleone/thanksforked',
        'Tracker': 'https://github.com/etienne-napoleone/thanksforked/issues',
    },
    packages=find_packages(include=['thanksforked']),
    entry_points={
        'console_scripts': [
            'thanksforked=thanksforked.thanksforked:main',
        ],
    },
    python_requires='python>=3.5',
    install_requires=requirements,
    license="MIT License",
    keywords='thanksforked',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities'
    ],
)
