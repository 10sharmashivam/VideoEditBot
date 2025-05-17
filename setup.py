from setuptools import setup, find_packages

setup(
    name="VideoEditBot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "transformers==4.44.2",
        "torch==2.4.1",
        "ffmpeg-python==0.2.0",
        "gunicorn==23.0.0",
    ],
)