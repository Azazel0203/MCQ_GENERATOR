# MCQ Generator with Streamlit

MCQ Generator with Streamlit is a web application that allows users to upload PDF or text files, specify the number of questions, subject, and tone, and generate multiple-choice questions (MCQs) based on the provided input. The application utilizes OpenAI's language models for natural language processing and provides feedback on the complexity of the generated quiz.

## Features

- **File Upload**: Users can upload PDF or text files containing the text from which MCQs will be generated.
- **Dynamic Inputs**: Users can specify the number of questions, subject, and tone for the generated MCQs.
- **Real-time Feedback**: Provides real-time feedback on the complexity of the generated quiz and suggests improvements.
- **Tabular Display**: Displays the generated MCQs in a tabular format for easy readability.

## Prerequisites

- Python 3.x
- Streamlit library
- Langchain library
- OpenAI API Key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mcq-generator-streamlit.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add your OpenAI API key to the `.env` file:

        ```plaintext
        OPEN_AI_KEY=your-openai-api-key
        ```

4. Install the local package in the virtual environment:

    ```bash
    python setup.py install
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Access the application in your web browser.

3. Upload a PDF or text file, specify the number of questions, subject, and tone, and click the "Create MCQs" button.

4. View the generated MCQs and the review feedback provided.

## Logging

- All logs are stored in the `logs` directory.
- Each log file is named with a timestamp indicating when it was created.
