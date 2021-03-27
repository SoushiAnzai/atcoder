import re
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")
# re pythonの正規表現モジュール
# re.match(パターン, 対象) 正規表現一致確認