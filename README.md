# openai-eeng201-solution-generator

Experimenting with using OpenAI to generate solution to homework, quiz, lab, and exam questions in EENG 201.

# Installation Instrucitons

python3 -m pip install openai

# Generate Solutions for a Set of Questions

Given a set of questions in a JSON file, you can call OpenAI to generate a solutions file using
the **generate-solutions.py** script. The solutions will be stored as JSON file as well, with
one text entry for each question.

python3 generate-solutions.py -s ~/settings-openai.txt -q questions/homeworks/assignment-01-questions.json -o solutions-openai-generated/homeworks/assignment-01-solutions.json

# Convert Solutions JSON File to Human-friendly PDF File

You can use the **generate-latex-pdf-from-json-solution-files.py** script to convert
solutions stored in JSON file into a PDF file. Internally the script uses LaTeX to
generate simple article document where it inserts the questions and the corresponding
OpenAI generated answers found in the provided JSON file.

python3 utils/generate-latex-pdf-from-json-solution-files.py -i solutions/homeworks/assignment-01-solutions.json -o solutions-openai-generated/homeworks/assignment-01-solutions.pdf

