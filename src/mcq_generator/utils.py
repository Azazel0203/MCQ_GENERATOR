import os
import PyPDF2
import json

import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            return "".join(page.extract_text() for page in pdf_reader.pages)
        except Exception as e:
            print (e)
            raise Exception ("error reading PDF file") from e
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "unsupported file format, only pdf and txt are supported"
        )

def get_table_data(quiz_str):
    try:
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]
        for key, value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option} -> {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct=value["correct"]
            quiz_table_data.append({"Question": mcq,
                                    "Options": options,
                                    "Correct": correct})
        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False