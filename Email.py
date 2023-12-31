import streamlit as st 

import pickle
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
nltk.download('PorterStemmer')

ps=PorterStemmer()


tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.title("Email Classifier")


def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text=y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    
    text=y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
    
    return " ".join(y)


email=st.text_area("Enter the mail")
#st.write(email)



if st.button("Predict"):


    #st.write(email)

    email_transform=transform_text(email)
    email_vectorized=tfidf.transform([email_transform]).toarray()

    result=model.predict(email_vectorized)[0]

    if(result==1):
        st.header("Spam")
    else:
        st.header("Not Spam")

