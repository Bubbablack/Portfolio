import setuptools



setuptools.setup(
    name="Bubbabblack", 
    version="1.0.0",
    author="Kevin Z Mntambo",
    author_email="author@example.com",
    description="This program adds numbers in the screen and can handle different deliminators given, the correct format.",
    long_description="This program adds numbers in the screen and can handle different deliminators given, the one adheres to these ,- integer,integer,integer e.g 1,2 or 1,2,3,4, - integer \n integer,integer e.g 1\n2,3 - //delimiter \n integer delimiter intege e.g //;\n1;2,- //[delimiter][delimiter]\n integer delimiter integer e.g //[\*][%]\n1\*2%3, no negetive numbers and numbers over a 999 won't be considered",
    url="https://github.com/Umuzi-org/Kevin-Mntambo-266-string-calculator-python.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)