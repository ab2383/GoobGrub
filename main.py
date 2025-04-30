import smtplib
import ssl
from email.message import EmailMessage
from recipes import recipe_book, quick_recipes
import random
import copy

#######################################################
####### Choose the options for meals this week #######

meal_num = 3
quick_options_only = False

#######################################################
#######################################################


def recipe_setup():
    global email_string
    # Populate the recipe book copy
    if(quick_options_only):
        book_copy = copy.deepcopy(quick_recipes)
    else:
        book_copy = copy.deepcopy(recipe_book)
    # Shuffle the recipe book once to randomize the order
    random.shuffle(book_copy)

    # Declare a new list to hold the recipes for the week
    weekly_recipes = []

    for i in range(meal_num):
        weekly_recipes.append(book_copy.pop())

    email_string = ""

    # Loop through the weekly recipes and create the email body
    for currRecipe in weekly_recipes:
        email_string = email_string + currRecipe.title + "\n\n"
        for ingredient in currRecipe.ingredients:
            email_string = email_string + ingredient + "\n"
        email_string = email_string + "_________________________________________\n\n"


# Function to send the desired email
def email(toMails):
    # Define email sender and receiver
    email_sender = "austinharrietwedding@gmail.com" # Your Mail
    app_password = "jvyu hgmv xldq rywb" # Get Google App Password from your mail
    
    # to get app_password visit and create
    # https://myaccount.google.com/apppasswords

    email_receivers = ", ".join(
        toMails
    )  # Join the list of emails into a comma-separated string

    # Set the subject and body of the email
    subject = "GoobGrub Weekly Recipes"
    body = email_string

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receivers
    em["Subject"] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, app_password)
        smtp.sendmail(
            email_sender, toMails, em.as_string()
        )  # Send to the list of emails


# List of email addresses to send the email to
email_list = [
    "abarlow848@gmail.com",
    #"hharriet28@gmail.com"
]
#recipe_setup()
#email(email_list)
#print("Mail has been sent")
