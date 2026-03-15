
import streamlit as st
import joblib

load_model=joblib.load(open('model.sav','rb'))

loder_vec=joblib.load(open('vectorizer.pkl','rb'))

def spam_detect(message):

  input_data = [message]
  input_count = loder_vec.transform(input_data)
  prediction = load_model.predict(input_count)

  if prediction[0] == 1:
    return 'Spam'
  else:
    return 'Not Spam'


def main():
    st.title('Spam Detection')
    message = st.text_input('Enter a message')
    if st.button('Predict'):
        result =spam_detect(message)
        if result == 'Not Spam':
           st.success(result)
        else:
           st.error(result)
if __name__ == '__main__':
  main()
