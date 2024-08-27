[![SUSHI-WARE LICENSE](https://img.shields.io/badge/license-SUSHI--WARE%F0%9F%8D%A3-blue.svg)](https://github.com/MakeNowJust/sushi-ware)
# IterFunc(仮)
## 概要
Python<br>
文字列の一部をワイルドカード的にして、イテレータで引数に渡した関数の戻り値を受け取れます<br>
なんかいい感じの関数思いついたら書き足す...はず<br>
## インストール
依存: setuptools
```sh
#シェルで
pip install git+https://github.com/thukumo/iterfuncpy.git
```

## 使い方
```python
from iterfunc import iter_func
for i in iter_func(lambda x: x, "?hoge??"):
    print(i) # 0hoge00, 0hoge01, 0hoge02, ... 9hoge98, 9hoge99
```
