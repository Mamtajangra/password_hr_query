# password_hr_query

A simple Python project that uses machine learning to categorize HR support tickets into categories such as "Login/Password Issue" and "Leave/HR Query".

## Features

- Uses scikit-learn's `Pipeline` to bundle text vectorization and classification.
- Classifies support tickets into predefined categories.
- Example tickets and categories included for demonstration.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn

Install dependencies with:

```sh
pip install pandas numpy scikit-learn# password_hr_query

Usage
Run the script:
python [password_hr.py](http://_vscodecontentref_/0)

Example Output  
                               ticket                 category
0  I forgot my password, how to reset it?          Login/Password Issue
1        I can’t log in, password incorrect        Login/Password Issue
2     Unable to login due to wrong password        Login/Password Issue
3         Reset my account password please         Login/Password Issue
4  Login page is not accepting my password         Login/Password Issue
5  I am unable to access my account, login issue   Login/Password Issue
6                How to see leave balance?         Leave/HR Query
7         Where can I check my leave status?        Leave/HR Query
8         Tell me about my available leaves         Leave/HR Query
9           How many leaves do I have left?         Leave/HR Query
10         Check remaining leaves in HR portal         Leave/HR Query
11                      Show my leave quota         Leave/HR Query



Ticket: I cannot login to my account --> Category: Login/Password Issue
Ticket: How many leaves do I have left? --> Category: Leave/HR Query
Ticket: Password reset is not working --> Category: Login/Password Issue