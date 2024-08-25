# 概要
文字列の一部をワイルドカード的にして楽にforループで関数実行してくれるだけです</br>
なんかいい感じの関数思いついたら書き足す...はず<br>
# インストール
依存しているライブラリはないです
```sh
#シェルで
pip install git+https://github.com/thukumo/wildcardpy.git
```

# 使い方
```python
import iterfunc
iterfunc.generate_combinations(lambda x: int(x)**2, "??") #[1, 1, 4, 9 ...
iterfunc.generate_combinations(print, "hoge??") # hoge00 hoge01 ...
```
