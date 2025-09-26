import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline           ##  in pipeline we can bundle multiple step with each other

data = {"ticket": [
        # Login/Password Issues
        "I forgot my password, how to reset it?",
        "I can’t log in, password incorrect",
        "Unable to login due to wrong password",
        "Reset my account password please",
        "Login page is not accepting my password",
        "I am unable to access my account, login issue",

        # Leave/HR Queries
        "How to see leave balance?",
        "Where can I check my leave status?",
        "Tell me about my available leaves",
        "How many leaves do I have left?",
        "Check remaining leaves in HR portal",
        "Show my leave quota",],

    "category": [
        "Login/Password Issue",
        "Login/Password Issue",
        "Login/Password Issue",
        "Login/Password Issue",
        "Login/Password Issue",
        "Login/Password Issue",

        "Leave/HR Query",
        "Leave/HR Query",
        "Leave/HR Query",
        "Leave/HR Query",
        "Leave/HR Query",
        "Leave/HR Query"]}
df = pd.DataFrame(data)
print(df)
#  Build ML Pipeline

model = Pipeline([
    ("tfidf", TfidfVectorizer()),                 # Convert text to TF-IDF
    ("clf", LogisticRegression(max_iter=1000))    # Train classifier
])

model.fit(df["ticket"], df["category"])     ## train the model

# test model 
test_tickets = ["I cannot login to my account","How many leaves do I have left?","Password reset is not working"]

predictions = model.predict(test_tickets)
for i in range(len(test_tickets)):
    ticket = test_tickets[i]
    pred = predictions[i]
    print(f"Ticket: {ticket} --> Category: {pred}")
