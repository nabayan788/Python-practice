
# %% 1-01 リストを作成
my_list = []

for i in range(1,11):
    my_list.append(i)

print(my_list)

# %% 1-02 分岐条件を学ぶ
num = int(input("整数を入力してください："))

if num  > 0:
    print("正の数です")

elif num < 0:
    print("負の数です")

else:
    print("ゼロです")


# %% 1-03 条件に合うリストを作成する
my_list = []

for i in range(1, 31):

    if i % 3 == 0:
        my_list.append(i)

print(my_list)

# %% 1-04ループ処理

for i in range(1, 31):

    if i % 10 == 0:
        print("10の倍数")

    else:
        print(i)

# %% 1-05 リスト内包表記

numbers = [i for i in range(1, 31) if i % 3 == 0]
print(numbers)

# %% 1-06 リストを結合する

# リスト作成
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# リスト結合
my_list = my_list1 + my_list2

print(my_list)

# %%　1-06 応用
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

marged_iter = chain(list1, list2, list3)
marged_list = list(marged_iter)

print(marged_list)

# %% 1-07 リストから要素を取り出す
my_list = [1, 2, 3]

a, b, c = my_list

print(a, c)

# %% 1-07 応用
my_list = [1, 2, 3, 4, 5]

a, b, *other = my_list
print(a)
print(b)
print(other)

# %% 1-08 リストを昇順ソート
my_list = [50, 20, 30, 10, 40]

ascending_list = sorted(my_list)
print(ascending_list)

# %% 1-08 応用
my_list = [50, 20, 30, 10, 40]

decending_list = sorted(my_list, reverse = True)
print(decending_list)

# %% 1-09 リストのスライス
my_list = [1, 2, 3, 4, 5]
second_four = my_list[1:4]
print(second_four)

# %% 1-10 タプルの基本操作
my_tuple = (10, 20, 30)
select_element = my_tuple[1]
print(select_element)

# %% 1-11 辞書を作成する
# 辞書登録

my_dict = {
    "name" : "Alice",
    "age" : "30",
    "city" : "New York"
}

print(my_dict)
print(my_dict["age"])

# %% 1-12 辞書を結合する
my_dict1 = {"A" : "111", "B" : "222", "C" : "333"}
my_dict2 = {"D" : "444", "E" : "555"}
my_dict3 = {"F" : "666"}

my_dict = {**my_dict1, **my_dict2, **my_dict3}
print(my_dict)

# %% 1-12 応用１
my_dict1 = {"A" : "111", "B" : "222", "C" : "333"}
my_dict2 = {"D" : "444", "E" : "555"}
my_dict3 = {"F" : "666"}

my_dict1.update(my_dict2)
my_dict1.update(my_dict3)
print(my_dict1)

# %% 1-12 応用２
my_dict1 = {"A" : "111", "B" : "222", "C" : "333"}
my_dict2 = {"D" : "444", "E" : "555"}
my_dict3 = {"F" : "666"}

combined_dict = my_dict1 | my_dict2 | my_dict3
print(combined_dict)

# %% 1-13 関数を作成

my_list = [10, 20, 30, 40, 50]

def calculate_average (x):

    # 平均値を算出する
    total = sum(x)
    count = len(x)
    average = total / count
    return average

average = calculate_average(my_list)
print(average)
# %% 1-13 模範解答

def calculate_average (numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("平均値：", average)

# %% 1-13 応用

def calculate_average (numbers):

    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)

# リストを定義
numbers = [10, 20, 30, 40, 50]

# 関数を使って平均値を計算
average = calculate_average(numbers)

# 結果を表示
print("平均値：" , average)

# %% 1-14 lambda式の基本

# lambda式を使って関数を定義する
average = lambda numbers : sum(numbers) / len(numbers)

# リストを定義
my_list = [10, 20, 30, 40, 50]

# 関数を使って計算する
average_value = average(my_list)

print("平均値：", average_value)

# %% 1-15 lambda式ソート

my_list = [(1, 2), (3, 1), (2, 4)]

sort_list = sorted(my_list, key = lambda x: x[1])

print("第二要素にもとづいて昇順にソートされたリスト：" , sort_list)
# %%
