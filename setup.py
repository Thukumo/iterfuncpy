from setuptools import setup, find_packages

setup(
    name="IterFunc",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[],
    author="つくも",
    author_email="0t0nashi0kayu@gmail.com",
    description="ちょっと楽にするために作ったライブラリ(超小機能)",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thukumo/wildcardpy",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        #"License :: OSI Approved :: MIT License", #ここもSUSHI-WARE LICENSEに
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)