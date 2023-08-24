from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import random
from app import Wine


def wine_flashcards():
    wine_list = []
    for wine in Wine.select():
        wine_list.append(model_to_dict(wine))

    number_of_wines = len(wine_list)

    def train():
        play_again = "y"

        while (play_again.lower() == "y"):
            random.shuffle(wine_list)
            correct = 0
            incorrect = 0

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
                        correct += 1
                    else:
                        print(
                            f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                        flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                        flashcard.incorrect += 1
                        flashcard.save()
                        incorrect += 1

                elif wine_list[i]['product_type'] == "White Wine":
                    white = wine_list[i]['product_type'][0:5].lower()
                    if response.lower() == white:
                        print("Correct!")
                        flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                        flashcard.correct += 1
                        flashcard.save()
                        correct += 1
                    else:
                        print(
                            f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                        flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                        flashcard.incorrect += 1
                        flashcard.save()
                        incorrect += 1

                else:
                    rose = wine_list[i]['product_type'][0:4].lower()
                    if response.lower() == rose:
                        print("Correct!")
                        flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                        flashcard.correct += 1
                        flashcard.save()
                        correct += 1
                    else:
                        print(
                            f"Incorrect! {wine_list[i]['name']} is a {wine_list[i]['product_type']}.")
                        flashcard = Wine.get(Wine.id == wine_list[i]['id'])
                        flashcard.incorrect += 1
                        flashcard.save()
                        incorrect += 1

            play_again_response = input(
                f"You got {correct} correct and {incorrect} incorrect. Would you like to play again (y or n)? ")
            if play_again_response.lower() == "y":
                play_again = "y"
                correct = 0
                incorrect = 0
            else:
                play_again = "n"
                print("It was nice training with you today. Goodbye!")

    def create():
        name = input("What is the name of the wine? ")
        country_state = input("What country or state is the wine from? ")
        region = input("What region is the wine from? ")
        product_type = input("What type of wine is it (red, white, or rose)? ")
        varietal_type = input("What is the varietal type of this wine? ")
        description = input("Please describe the wine: ")
        image = input("Please provide a link to an image of the wine: ")
        flag = input("Please provide a link to a flag of the wine: ")

        confirm_create_wine = input(
            f"You entered\nName: {name}\nCountry / State: {country_state}\nRegion: {region}\nProduct Type: {product_type}\nVarietal Type: {varietal_type}\nDescription: {description}\nImage: {image}\nFlag: {flag}\nIs this correct (y or n)? ")

        if confirm_create_wine.lower() == "y":
            new_wine_flashcard = Wine(name=name, country_state=country_state, region=region, product_type=product_type,
                                      varietal_type=varietal_type, description=description, image=image, flag=flag)
            new_wine_flashcard.save()
            print(
                f"{new_wine_flashcard.name} has been added as a flashcard to the database!")
        else:
            print("Creating flashcard cancelled.")
            start()

    def start():
        create_or_train = input(
            f"Welcome to your Wine Flashcards!\nYou currently have {number_of_wines} cards. Would you like to create a new card or train with your existing cards? Enter c for create or t for train: ")

        if create_or_train.lower() == "c":
            print("Let's create a new card!")
            create()
            wine_flashcards()
        elif create_or_train.lower() == "t":
            train()
        else:
            print("Invalid response. Please try again.")
            start()

    start()


wine_flashcards()
