#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 06:52:28 2024

@author: gonzaresu
"""

import random

# ピザメニュー辞書 (ピザ名と具材のペア)
pizza_menu = {
    # Starter Menu
    "Garlic Pizza": ["garlic", "fresh herbs"],
    "Cinque Formaggi": ["parmesan cheese", "feta", "brie", "gorgonzola", "mozzarella", "herbs"],
    "Pesto Cheese": ["basil pesto base", "mozzarella", "herbs"],

    # Vegan
    "The Vegan": ["tomato base", "baby spinach", "pumpkin", "mushrooms", "sweet potato", "vegan mozzarella", "herbs"],

    # Vegetarian
    "Margherita": ["tomato", "herbs"],
    "Genovese": ["tomato", "spanish onion", "garlic", "mushrooms", "fresh capsicum", "kalamata olives"],
    "Ramses": ["tomato", "kalamata olives", "mushrooms", "feta", "roast capsicum", "herbs"],
    "Veggie Extreme": ["tomato", "feta", "baby spinach leaves", "spanish onion", "fire-roasted capsicum", "char-grilled eggplant slices", "sweet potato", "kalamata olives"],

    # Meat
    "Aussie": ["tomato", "ham", "egg (optional)", "herbs"],
    "Hawaiian": ["tomato", "ham", "pineapple"],
    "Ultra Death": ["tomato", "spicy salami", "ultra death chilli", "jalapenos"],
    "Pepperoni": ["tomato", "ham", "mushroom", "kalamata olives", "herbs"],
    "Mexicano": ["tomato", "kalamata olives", "jalapenos", "tabasco", "spicy salami"],
    "Calabrese": ["tomato", "mushroom", "fresh capsicum", "spicy salami", "anchovies", "chilli"],
    "Fruscolino Special": ["tomato", "mushroom", "fresh capsicum", "spicy salami", "anchovies", "egg"],
    "Meat Lovers": ["tomato", "ham", "mushroom", "spicy salami", "oven-roasted chicken"],

    # Chicken
    "Fior Di Latte": ["tomato", "baby spinach", "semi-dried tomatoes", "kalamata olives", "garlic", "mozzarella"],
    "Chicken Divola": ["tomato", "oven-roasted chicken", "spicy salami", "herbs"],
    "BBQ Chicken": ["tomato", "bbq base", "oven-roasted chicken", "spanish onion", "capsicum", "herbs"],
    "Tandoori Chicken": ["tomato", "tandoori chicken", "spanish onion", "capsicum", "sweet potato", "mozzarella", "mint yogurt"],
    "Peri Peri Chicken": ["tomato", "peri peri chicken", "spanish onion", "capsicum", "garlic", "mozzarella", "peri peri sauce", "rocket"],

    # Prosciutto & Lamb
    "Prosciutto": ["tomato", "fior di latte", "prosciutto", "baby spinach leaves"],
    "Gourmet Lamb": ["tomato", "marinated lamb", "feta", "roast capsicum", "paprika", "tzatziki"],
    "Traditional Lamb": ["tomato", "sweet potato", "marinated lamb", "spanish onion", "garlic", "rocket"],

    # Seafood
    "Marinara": ["tomato", "prawns", "anchovies", "garlic", "herbs"],
    "Mediterranean": ["tomato", "fior di latte", "roast capsicum", "spinach", "paprika", "tzatziki"]
}

def generate_question():
    # ランダムにピザを選択
    pizza_name = random.choice(list(pizza_menu.keys()))
    ingredients = pizza_menu[pizza_name]
    return pizza_name, ingredients

def main():
    print("ピザメニュークイズへようこそ！\n")
    while True:
        # 問題を生成
        pizza_name, ingredients = generate_question()
        
        print(f"ピザ名: {pizza_name}")
        print("このピザの具材をすべて答えてください（1つずつ改行で入力してください）:")
        
        user_ingredients = []
        while True:
            user_input = input("具材を入力（終了時はEnterのみ押してください）: ").strip()
            if user_input == "":
                break
            user_ingredients.append(user_input)
        
        # 答えをチェック
        if sorted(user_ingredients) == sorted(ingredients):
            print("正解です！次の問題に進みます。\n")
        else:
            print("不正解です。もう一度具材を試してください。\n")
            print(f"ヒント: このピザの具材は {len(ingredients)} 種類です。")

# 実行
if __name__ == "__main__":
    main()
