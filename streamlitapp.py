import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
# import langchain
from src.mcq_generator.utils import read_file, get_table_data
from src.mcq_generator.logger import logging
from langchain.globals import set_verbose
set_verbose(True)
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcq_generator.MCQGenerator import generate_and_evaluate_quiz


with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)
    

# STREAMLIT PART

st_key = os.getenv("ST_KEY")
# the title
st.title("MCQ Generator")

# the input form
with st.form("user_inputs"):
    # file
    uploaded_file=st.file_uploader("Upload a pdf or text file")
    # inputs
    mcq_count=st.number_input("No of Questions", min_value=3, max_value=50)
    subject = st.text_input("Insert the Subject", max_chars=20)
    tone=st.text_input("Complexity level of Questions", max_chars=20, placeholder="Simple")
    input_key = st.text_input("Enter the secret key", max_chars=50, placeholder="Password")
    button = st.form_submit_button("Create MCQs")
    
    # check for button click
    if button and uploaded_file is not None and mcq_count and subject and tone:
        if input_key == st_key:
            with st.spinner("Loading..."):
                try:
                    text = read_file(uploaded_file)
                    # call the llm while getting the token metrics
                    with get_openai_callback() as cb:
                        response=generate_and_evaluate_quiz(
                            {
                                "text": text,
                                "number": mcq_count,
                                "subject": subject,
                                "tone": tone,
                                "response_json": json.dumps(RESPONSE_JSON) 
                            }
                        )
                except Exception as e:
                    traceback.print_exception(type(e), e, e.__traceback__)
                    st.error("Error")

                else:
                    print (f"Total Tokens: {cb.total_tokens}")
                    print (f"Prompt Tokens: {cb.prompt_tokens}")    
                    print (f"Completion Tokens: {cb.completion_tokens}")
                    print (f"Total Cost: {cb.total_cost}")
                    if isinstance(response, dict):
                        # extract the quiz data from the response
                        quiz = response.get("quiz", None)
                        if quiz is not None:
                            table_data=get_table_data(quiz)
                            if table_data is not None:
                                df = pd.DataFrame(table_data)
                                df.index=df.index+1
                                st.table(df)
                                # for review
                                st.text_area(label="Review", value=response["review"])
                            else:
                                st.error("Error in the table data")
                    else:
                        st.write(response)
        else:
            st.error("Wrong Password")