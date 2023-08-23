from app import data
import random


def wine_flashcards():
    random.shuffle(data)

    def train():
        number_of_cards = int(input(
            f"Let's train! How many cards would you like to use (1 - {len(data)})? "))
        for index in range(0, number_of_cards):
            response = input(f"What type of wine is {data[index]['name']}? ")
            print(response)

    def start():
        create_or_train = input(
            f"Welcome to your Wine Flashcards! You currently have {len(data)} cards. Would you like to create a new card or train with your existing cards? Enter c for create or t for train: ")

        if create_or_train == "c":
            print("Let's create a new card!")
            # create()
        elif create_or_train == "t":
            train()
        else:
            print("Invalid response. Please try again.")
            start()

    start()


wine_flashcards()
