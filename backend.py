from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import io 
import base64

app = FastAPI()
 
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

def home():
    return {"message":"Titanic chatbot Backend is running!"}

@app.get("/query")
def query_titanic(question: str):
    
    question = question.lower()

    if "percentage of passengers were male" in question:
        male_percentage = (df['Sex'].value_counts(normalize=True)['male']) * 100
        return {"response": f"{male_percentage:.2f}% of the passengers were male."}

    elif "histogram of passenger ages" in question:
        plt.figure(figsize=(8, 6))
        sns.histplot(df["Age"].dropna(), bins=20, kde=True)
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.title("Histogram of Passenger Ages")

        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        encoded_img = base64.b64encode(img.read()).decode()
        
        return {"image": encoded_img}

    elif "average ticket fare" in question:
        avg_fare = df["Fare"].mean()
        return {"response": f"The average ticket fare was ${avg_fare:.2f}."}

    elif "how many passengers embarked from each port" in question:
        embarked_counts = df["Embarked"].value_counts().to_dict()
        return {"response": embarked_counts}

    else:
        return {"response": "I can only answer Titanic-related questions. Try asking about passenger demographics, fares, or embarkation!"}


