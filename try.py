def add(a, b):
    try:
        print(a + b)
    except TypeError:
        print("文字列と数字は足し算できません。")
    else:
        print("例外は発生しませんでした。")
    finally:
        print("処理完了")

add(1, 3)
print("-----")
add(1, "2")

"""
4
例外は発生しませんでした。
処理完了
-----
文字列と数字は足し算できません。
処理完了
"""
