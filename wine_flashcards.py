from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import random
from app import Wine


def wine_flashcards():
    wine_list = []
    for wine in Wine.select():
        wine_list.append(model_to_dict(wine))

    number_of_wines = len(wine_list)

    random.shuffle(wine_list)

    def train():
        number_of_cards = int(input(
            f"Let's train! How many cards would you like to use (1 - {number_of_wines})? "))

        for i in range(0, number_of_cards):
            response = input(
                f"What type of wine is {wine_list[i]['name']} (red, white, or rose)? ")

            if wine_list[i]['product_type'] == "Red Wine":
                red = wine_list[i]['product_type'][0:3].lower()
                if response.lower() == red:
                    print("Correct!")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.correct += 1
                    flashcard.save()
                else:
                    print(
                        f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.incorrect += 1
                    flashcard.save()

            elif wine_list[i]['product_type'] == "White Wine":
                white = wine_list[i]['product_type'][0:5].lower()
                if response.lower() == white:
                    print("Correct!")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.correct += 1
                    flashcard.save()
                else:
                    print(
                        f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.incorrect += 1
                    flashcard.save()

            else:
                rose = wine_list[i]['product_type'][0:4].lower()
                if response.lower() == rose:
                    print("Correct!")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.correct += 1
                    flashcard.save()
                else:
                    print(
                        f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                    flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                    flashcard.incorrect += 1
                    flashcard.save()

    def start():
        create_or_train = input(
            f"Welcome to your Wine Flashcards! You currently have {number_of_wines} cards. Would you like to create a new card or train with your existing cards? Enter c for create or t for train: ")

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
