import os
import sys
import json
import openai
import argparse
import requests

# Setup argument parser
parser = argparse.ArgumentParser(description='Generate solutions to a quiz, input is JSON file with quiz questions.',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-s', '--settings', dest='settings', type=str, required=True,
          help='Path to JSON settings file with OpenAI API key.')
parser.add_argument('-q', '--questions', dest='questions', type=str, required=True,
          help='Path to JSON settings file with questions.')
args = parser.parse_args()

# Read API key from JSON file
with open(args.settings, "r") as settings_file:
    data = json.load(settings_file)

apikey = data['apikey']
organization = data['organization']

# Connect to OpenAI
openai.organization = organization
openai.api_key = apikey

# Load questions
with open(args.questions, "r") as questions_file:
    data = json.load(questions_file)

# Generate answers
answers = dict()

for question in data:
    print("")
    print(question)
    print(data[question])

    prompt = data[question]

    text = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        temperature=1,
        n=1
    )

    for choice in text['choices']:
        print(choice['text'])

    answers[ question ] = choice['text']

# Write answers to JSON file
with open('data.json', 'w') as outfile:
  json.dump(answers, outfile, indent=4)

# Done
print("Finished.")
