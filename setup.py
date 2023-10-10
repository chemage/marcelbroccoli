from setuptools import setup

setup(
    name="marcelbroccoli",
    version="1.0.7",
    description="Marcel's custom functions",
    url="https://github.com/chemage/marcelbroccoli",
    author="Marcel Gerber",
    author_email="me@marcelgerber.ch",
    license="none",
    packages=["marcelbroccoli"],
    install_requires=['python_dotenv', 'colorama'],
    zip_safe=False
)
