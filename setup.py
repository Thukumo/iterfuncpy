from setuptools import setup, find_packages

setup(
    name="StringCombiner",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="つくも",
    author_email="0t0nashi0kayu@gmail.com",
    description="ちょっと楽にするために作ったライブラリ(関数2つ)",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thukumo/wildcardpy",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)