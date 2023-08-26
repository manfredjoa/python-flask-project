# Wine API with Command Line Application

## Introduction

Welcome to my Wine API with Command Line Application mini project!

The data for this API came from the master.json file found in my previous project [Wine About It - Server](https://github.com/manfredjoa/wine-about-it-server). You may also want to check out the [Wine About It - Client](https://github.com/manfredjoa/wine-about-it-client)!

It will help to have a browser extension such as [JSONVue](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) to parse the data into a more readable json format.

## Data Model

Since the json file had fields written in Pascal case and Python is written in snake case, to maintain consistency in naming conventions across the different file types, I used the following command in the terminal to change each field name to snake case:

<br>

```
sed -i '' -e 's/JSONFieldName/python_field_name/g master.json'
```

<br>

---

<br>

| Field         | Type         | Description                                                        |
| ------------- | ------------ | ------------------------------------------------------------------ |
| name          | CharField    | The name of the wine                                               |
| country_state | CharField    | The country/state the wine is from                                 |
| region        | CharField    | The specific region the wine is from within its country/state      |
| product_type  | CharField    | The type of wine                                                   |
| varietal_type | CharField    | The specific variety of the wine's type                            |
| description   | TextField    | A description of the wine                                          |
| image         | CharField    | A link to an image of the wine                                     |
| flag          | CharField    | A link to an image of the country's flag of which the wine is from |
| correct       | IntegerField | The number of times the user has correctly identified the wine     |
| incorrect     | IntegerField | The number of times the user has incorrectly identified the wine   |

## CRUD Functionality

### GET

- **_/wines_** - Returns a list of all wines
- **_/wines/\<id\>_** - Returns a wine by id

### POST

- **_/wines_** - Creates a new wine

### PUT

- **_/wines/\<id\>_** - Updates a wine by id

### DELETE

- **_/wines/\<id\>_** - Deletes a wine by id

## Command Line Application

The command line application allows the user to interact with the API in a fun and educational way! The user can use the flashcards containing data from the API to test their knowledge of different types of wine. The user can also create their own flashcards and save them to the database. Simply follow the installation instructions below to get started!

Once installation is complete, follow along with the prompts to either create a new flashcard or select the number of randomly shuffled flashcards you would like to train with. Each flashcard also contains the correct and incorrect fields which describe the number of times the user has correctly or incorrectly identified that specific wine's type.

## Technologies Used

- Python
- PostgreSQL
- Peewee
- Flask

## Installation

If you would like to use this API for your own project, you can clone this repository and run the following commands in your terminal from within the cloned repository:

Install Pipenv

```
pip3 install pipenv
```

Install Dependencies (flask, peewee, psycopg2-binary)

```
pipenv install
```

Activate Virtual Environment

```
pipenv shell
```

Create Database (PostgreSQL)

```
createdb wines
```

Create Tables & Seed Database

```
python3 seed.py
```

Run Server (_as needed_) for CRUD functionality involving endpoints and Postman

```
nodemon --exec python3 app.py
```

Open Command Line Application

```
python3 wine_flashcards.py
```

## Next Steps

- Pagination of API
- Creating another model that can be referenced by the wine model
- Adding more training options to the flashcards in the command line application, such as training by country/state, region, or varietal type

## Thoughts

I found it way easier (and much quicker) to create this API than I did with my previous project back-end project, [Plants API](https://github.com/manfredjoa/plants-api). Of course being that this is a mini project compared to a unit project, I took the shortcut of using data I already had access to instead of creating my own data.

I still found it surprising how I was able to create this rather quickly, considering how I learned Python in 2 days and PostgreSQL and Flask each in less than a day. I think this is a testament to how easy it is to pick up new languages and frameworks once you have a solid foundation in programming.

I also wanted to point out that it could have been a very simple fix for me to change the field names from Pascal case to snake case in the json file, simply by using cmd + f and selecting all instances of the word and changing it that way. However, I challenged myself to find another way to do this and learned something new that I can use in the future!

I also loved and had a lot of fun creating a command line application to supplement the API. I think it's a great way to interact with an API besides using it as a data library. I also think it's a great way to test the API and make sure it's working as intended and that the database is actually being updated based on user input.

I enjoyed working with Python, PostgreSQL, Peewee, and Flask and look forward to creating more command line applications in the future!
