#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 06:50:29 2024

@author: gonzaresu
"""

import random

# コーヒーの種類、サイズ、オプションのリスト
coffee_types = {
    "Latte": "L",
    "Flat White": "F",
    "Cappuccino": "C",
    "Magic": "M",
    "Long Black": "LB",
    "Short Black": "SB",
    "Long Macchiato": "LM",
    "Short Macchiato": "SM",
    "Espresso": "E",
    "Ristretto": "R",
}

sizes = {
    "Small": "S",
    "Large": "L",
}

options = {
    "Strong": "S",
    "Weak": "W",
}

location = {
    "Takeaway": "T",
    "Dine-in": "D",
}

def generate_random_order():
    # ランダムな注文を生成
    coffee = random.choice(list(coffee_types.keys()))
    size = random.choice(list(sizes.keys()))
    option = random.choice(list(options.keys()))
    loc = random.choice(list(location.keys()))
    return coffee, size, option, loc

def main():
    print("コーヒー注文略語クイズを始めます！正しい略語を入力してください。\n")
    while True:
        # ランダムな注文を生成
        coffee, size, option, loc = generate_random_order()

        # 正解の略語
        correct_answer = f"{coffee_types[coffee]} {sizes[size]} {location[loc]} {options[option]}"

        # 問題を表示
        print(f"注文: {coffee}, サイズ: {size}, オプション: {option}, 持ち帰り/店内: {loc}")
        
        # ユーザーの回答をチェック
        while True:
            user_input = input("略語を入力してください: ").strip()
            if user_input == correct_answer:
                print("正解です！次の問題に進みます。\n")
                break
            else:
                print("不正解です。もう一度試してください。\n")

# 実行
if __name__ == "__main__":
    main()