import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ dataset
data = pd.read_csv("faq.csv")

questions = data['question']
answers = data['answer']

# Convert text to vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

print("FAQ Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:
    user_query = input("You: ")

    if user_query.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_query])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    if similarity[0][best_match] > 0.2:
        print("Chatbot:", answers[best_match])
    else:
        print("Chatbot: Sorry, I don't understand that question.")