"""
File: main.py
-------------------
Send a WhatsApp Message with a joke, a short story or a personalized message and define sending time using twilio api
"""
from datetime import datetime

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

import jokesGenerator
import shortStoryGenerator


def main():

    # sender data
    account_sid_string = input("Enter the account SID: ")
    auth_token_string = input("Enter the author token: ")

    account_sid = os.environ[account_sid_string]
    auth_token = os.environ[auth_token_string]

    client = Client(account_sid, auth_token)

    # sender number
    twilio_number = input("Enter your Twilio number (with international prefix): ")
    whatsapp_twilio_number = 'whatsapp:' + twilio_number

    # receiver number
    target_number = input("To which number do you want to communicate? ")
    whatsapp_target_number = 'whatsapp:' + target_number

    # Select the text of the message
    if input("Do you want to send a short story: ").lower() == 'yes':
        message_text = shortStoryGenerator.generate()
    elif input("Do you want to send a joke: ").lower() == 'yes':
        message_text = jokesGenerator.generate()
    else:
        message_text = input("Enter the message that you want to send: ")

    # Extract today date
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = input("At what hour do you want to send it?: ")

    message = client.messages \
        .create(
        body=message_text,
        from_=whatsapp_twilio_number,
        to=whatsapp_target_number,
        send_at=datetime(year, month, day, hour, 00, 00),
    )

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
