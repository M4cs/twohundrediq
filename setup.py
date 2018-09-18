
#!/usr/bin/python3
from setuptools import setup

setup(
    name='twohundrediq',
    version='1.0',
    description='HQ Trivia Bot For Windows and iPhone',
    long_description='This python package lets you read LonelyScreen and read HQ Trivia questions and answers then looking them up and returing the correct answer!',
    author='Max Bridgland',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    platform="Windows",
    keywords="hq trivia bot answer auto lookup ocr text recognition",
    author_email='mabridgland@protonmail.com',
    url='https://github.com/M4cs/twohundrediq',
    packages=['twohundrediq'],
    scripts=['bin/twohundrediq'],
    install_requires=[
        "colorama==0.3.9",
        "crayons==0.1.2",
        "nltk==3.3",
        "numpy==1.15.1",
        "opencv-python==3.4.3.18",
        "Pillow==5.2.0",
        "psutil==5.4.7",
        "pypiwin32==223",
        "pytesseract==0.2.4",
        "pywin32==223",
        "pywin32-ctypes==0.2.0",
        "tesseract==0.1.3",
        "wikipedia==1.4.0"
    ]
)
