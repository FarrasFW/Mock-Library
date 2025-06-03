# Mock-Library
Library Management System

Preface

The Library management system is a simple system potentially used in a library to help with the day to day operations of a typical library. This system was created to fulfill a requirement by the Purwadhika institute.
________________________________________
Introduction:

The Library management system, is a simple system that can be used to help with the daily operations of a typical library, where it has options to do numerous tasks including, showing the full book directory, automatically show availability of books when it is borrowed or returned, add or delete a book log in the directory, edit the tags(which shows a genre of the book) of a book, and to give recommendations based on a tag.
________________________________________
Features:

- Main Menu

- Show list of Books

- Search Books

- Add a new Book log

- Delete an Existing Book log

- Borrow a Book

- Return a Book

- Edit a Book tag

- Recommend a Book

- Exit

________________________________________
- Main Menu:

Upon starting the program, the user will be given nine options to choose from. The user will be asked to input a number which corresponds to certain actions. The actions the user can choose from will be mentioned in the next points.

- Show list of Books:

This option is associated with number 1, once the user chooses this option the full directory of books will be shown. The book directory will show information regarding the book ID, the Book Name, the Author of the book, Publishing Year of the book, the number of Copies available, and Tag which associates the books genre.

- Search Books:

This option is associated with number 2, once the user chooses this option, they will be asked to input the name of the book that they are looking for, if a book is not in the directory it will show "Book not found, try again.", if the book is in the directory it will show the book ID, the Book Name, the Author of the book, Publishing Year of the book, the number of Copies available, and Tag which associates the books genre.

- Add a new Book log:

The option is associated with number 3, once the user chooses this option they will be given prompts so that they can input the name of the book, the author, the publishing year, the number of copies, and the tags(which are comma separated). The book ID will automatically be updated based on the authors initials, the publishing year, and the number the order the book was added to the directory. Once confirmed it will give a prompt saying "Book 'Title' successfully added.")

- Delete an Existing Book log:

The option is associated with number 4, once the user chooses this option, they will be given a prompt to give the book name, once filling the name it will confirm that the book is deleted if the book is not in the directory it will mention that the book is not found.

- Borrow a Book:

The option is associated with number 5, once the user chooses this option they will be given a prompt to ask the name of the book they want to borrow, and how many copies they want to borrow, if they input a number greater than the available copies it will mention how many copies are left. If they give less than or equal to the number of copies, they will be given a prompt saying that they have successfully borrowed the book with the number of copies. There will then have another prompt asking if you would borrow another book, and if the answer is “yes” it will loop back until the answer given is “no”

- Return a Book:

The option is associated with number 6, once the user chooses this option they will be given a prompt to ask the name of the book they want to return, and how many copies they want to return. There will then have another prompt asking if you would borrow another book, and if the answer is “yes” it will loop back until the answer given is “no”

- Edit a Book tag:

The option is associated with number 7, once the user chooses this option they will be given a prompt asking if you want to add or remove a tag. Once an option is chosen, the user is asked the name of the book, and then another prompt will display where they can mention the tag that they want to add or remove, more than one can be chosen and they are comma separated. Depending on what the user have chosen there will then be a prompt saying “tag have been added” or “tag have been removed”. Typing anything other than add or remove in the first question will show "Please only choose 'add' or 'remove'." Mentioning a book not in the directory will result in a prompt saying “Book not found.”

- Recommend a Book:

The option is associated with number 8, once the user chooses this option they will be given a prompt asking what tags are they looking for, if there one associated, it will show the name of the book and whether the book is available or not. If there is no associating in the directory it will show a prompt "No recommendations found."

- Exit:

This option is associated with number 9, once the user chooses this option they will receive a prompt saying "Thank you for using the Library System!"
 
________________________________________
Technology
●	Python – The only technology used for this program.
________________________________________
Installation
1.	Ensure you have Python installed on your device.
2.	Clone this repository:
3.	git clone https://github.com/FarrasFW/Mock-Library
4.	Navigate to the project directory and run the program using:
5.	python Capstone Project 1.py
