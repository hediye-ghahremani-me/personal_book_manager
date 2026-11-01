# Personal book manager
![Python](https://img.shields.io/badge/python-3.13-blue)

A simple book manager built with python

## Features
- Save books data
- Add multiple books
- Load saved books
- Display all saved books
- Admin mode with password authentication

## Project structure
```bash
personal_book_manager/
│   .env.example
│   .gitignore
│   books.py
│   main.py
│   README.md
│   requirements.txt
│
├───images
│       demo.gif
│       screenshot_main.png
```

## File / Folder description
| File / Folder | Description |
|---|---|
| `images/` | Contains project screenshots and demo GIFs. |
| `.env.example` | Provides an example of the required environment variables. |
| `.gitignore` | Specifies files and folders Git should ignore. |
| `books.py` | Contains functions for loading, saving, and displaying books. |
| `main.py` | The main project file for running the application. |
| `README.md` | Provides project documentation and usage instructions. |
| `requirements.txt` | Lists the required Python dependencies. |
| `demo.gif` | Shows a short demonstration of the application. |
| `screenshot_main.png` | Displays a screenshot of the main application. |

## How it works
1. The program starts by asking for the user’s name and welcoming them.
2. The user is asked whether they want to enter admin mode or not.
3. If they choose to enter admin mode, they must enter the correct password.
4. The program loads saved books from `books.json.` If the file doesn’t exist, it starts with an empty list.
5. The user enters the number of books they want to add and then enter their names one by one.
6. All books, including previously saved ones, are displayed to the user.
7. Finally, the updated book list is saved to `books.json` so it can be loaded the next time the program runs.

## Troubleshooting
| Error | Meaning | Possible Cause | First Thing to Check |
|---|---|---|---|
| `FileNotFoundError` | Required file not found. | Missing file or wrong directory. | Check file name and location. |
| `JSONDecodeError` | Invalid JSON data. | Empty or corrupted `books.json`. | Check JSON format. |
| `.env` Password Not Loading | Password cannot be read. | Missing `.env` or wrong variable name. | Check `.env` and variable name. |
| `ModuleNotFoundError: dotenv` | Python cannot find the module. | `python-dotenv` is not installed. | Run `pip show python-dotenv`. |


## Requirements
- Python
- Python-dotenv

## Installation
Install the required packages with:

```bash
python -m pip install -r requirements.txt
```

## Envoirment setup
1. Create a `.env` file in the project folder,

2. Use `.env.example` as a template,

3. And add your admin password.

```env
BOOK_MANAGER_ADMIN_PASSWORD=put_your_password_here
```
> Replace `put_your_password_here` with your own admin password.

## Run the program
Run the main file with:

```bash
python main.py
```

## Screenshot
![personal_book_manager_screenshot](images\screenshot_main.png)

## Demo
![personal_book_manager_demo](images\demo.gif)