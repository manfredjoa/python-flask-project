from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import random
import json
from app import Wine

file = open('master.json')
data = json.load(file)

# Just realized this is using data from master.json, not the actual database!


def wine_flashcards():
    random.shuffle(data)

    def train():
        number_of_cards = int(input(
            f"Let's train! How many cards would you like to use (1 - {len(data)})? "))

        for i in range(0, number_of_cards):
            response = input(
                f"What type of wine is {data[i]['name']} (red, white, or rose)? ")

            if data[i]['product_type'] == "Red Wine":
                red = data[i]['product_type'][0:3].lower()
                if response.lower() == red:
                    print("Correct!")
                    data[i]['correct'] += 1
                else:
                    print(
                        f"Incorrect! {data[i]['name']} is a {data[i]['product_type']}.")
                    data[i]['incorrect'] += 1

            elif data[i]['product_type'] == "White Wine":
                white = data[i]['product_type'][0:5].lower()
                if response.lower() == white:
                    print("Correct!")
                    data[i]['correct'] += 1
                else:
                    print(
                        f"Incorrect! {data[i]['name']} is a {data[i]['product_type']}.")
                    data[i]['incorrect'] += 1

            else:
                rose = data[i]['product_type'][0:4].lower()
                if response.lower() == rose:
                    print("Correct!")
                    data[i]['correct'] += 1
                else:
                    print(
                        f"Incorrect! {data[i]['name']} is a {data[i]['product_type']}.")
                    data[i]['incorrect'] += 1

    def start():
        create_or_train = input(
            f"Welcome to your Wine Flashcards! You currently have {len(data)} cards. Would you like to create a new card or train with your existing cards? Enter c for create or t for train: ")

        if create_or_train.lower() == "c":
            print("Let's create a new card!")
            # create()
        elif create_or_train.lower() == "t":
            train()
        else:
            print("Invalid response. Please try again.")
            start()

    start()


wine_flashcards()
