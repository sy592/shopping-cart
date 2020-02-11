# Shopping Cart Project

[Project Description](https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/shopping-cart.md) posted on course page.


## Installation

Clone or download from [Suning GitHub Repository Shopping Cart Project](https://github.com/sy592/shopping-cart), then navigate into the project repository:

```
sh
cd shopping-cart
```

## Packages Command-Line Installations (Additional Challenges)

**Configuring Sales Tax Rate**

>In this project, I used the tax rate of New York area, which is 8.75%; at the same time, I would like to share my code with stores in other locations as well. Since different municipalities use different sales tax rates, instead of hard-coding the sales tax rate, I allow the user to configure it via environment variable using a ".env" file approach.

```
pip install python-dotenv
```
**Sending Receipts via Email**

>Besides displaying a receipt at the end of the checkout process, this program can prompt the checkout clerk or the customer to indicate whether the customer would like to receive the receipt by email. It can prompt the checkout clerk or the customer to input the customer's email address and send the receipt information to the customer by email. The clerk's network-connected computer is able to send these emails.

```
pip install sendgrid==6.0.5
```
**Writing Receipts to File**
>The program can write the receipt information into a new ".txt" file saved in a new "receipts" directory inside the project repository. The clerk's printer-connected computer is able to actually print a paper receipt from the information contained in this file.
>
>Each text file is amed according to the date and time the checkout process started (e.g. "/receipts/2019-07-04-15-43-13-579531.txt", where the numbers represent the year, month, day, 24-hour-style hour, minute, second, and milliseconds/microseconds, respectively).


## Usage

Run the program

```py
python shopping_cart.py
```

## Source: 
[Professor Screencast on YouTube](https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be)

[Database Dictionary](https://www.w3schools.com/python/python_dictionaries.asp)

[Formatting Time](https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
)

Source links for writing receipt into .txt
>https://www.w3schools.com/python/python_file_write.asp
https://www.tutorialspoint.com/python3/time_strftime.htm
https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output


