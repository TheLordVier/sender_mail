# Sender Mail Project

## Technology Stack

* Python 3.10
* Smtplib
* Logging
* Unittest
* Flake8
* JSON


## Brief Description

This project allows you to send emails to multiple recipients using the smtplib library in Python.


## Installation Guide

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/TheLordVier/sender_mail.git
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   On Windows: 

   ```bash
   venv\Scripts\activate
   ```
   
   On macOS and Linux: 

   ```bash
   source venv/bin/activate
   ```

4. Install the project dependencies::

   ```bash
    pip install -r requirements.txt
   ```


## Usage

1. Modify the list_mail.json file in the data folder to contain the email addresses you want to send emails to.

2. Update mail_config.py with your SMTP server, port, username, and password.

3. Run the script to send emails:

   ```bash
    python main.py
   ```
   
This will send test emails to the recipients listed in list_mail.json.


## Configuration

- mail_config.py: Contains SMTP server, port, username, and password configurations.
- data/list_mail.json: JSON file with email addresses to send emails to.
