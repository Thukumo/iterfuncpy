[![SUSHI-WARE LICENSE](https://img.shields.io/badge/license-SUSHI--WARE%F0%9F%8D%A3-blue.svg)](https://github.com/MakeNowJust/sushi-ware)
# ここにタイトルを入れる
## 概要
文字列の一部をワイルドカード的にして、イテレータで引数に渡した関数の戻り値を受け取れます<br>
なんかいい感じの関数思いついたら書き足す...はず<br>
## インストール
依存しているライブラリはないです
```sh
#シェルで
pip install git+https://github.com/thukumo/wildcardpy.git
```

## 使い方
```python
import iterfunc
for i in iterfunc.iter_func(lambda x: x, "???"):
    print(i) # 000 001 002 ... 997 998 999
```
