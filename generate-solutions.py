
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import json
import openai
import argparse
import requests
import datetime

# Setup argument parser
parser = argparse.ArgumentParser(description='Generate solutions to questions input as JSON file.',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-s', '--settings', dest='settings', type=str, required=True,
          help='Path to JSON settings file with OpenAI API key.')
parser.add_argument('-q', '--questions', dest='questions', type=str, required=True,
          help='Path to JSON settings file with questions.')
parser.add_argument('-o', '--output', dest='output', type=str, required=True,
          help='Path to output JSON file for saving generated answers.')
args = parser.parse_args()

# Script start time
start_time = datetime.datetime.now()

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

# Set OpenAI parameters
model_param       = "text-davinci-003"
max_tokens_param  = 512
temperature_param = 1
n_param           = 1

for question in data:
    print("")
    print(question)
    print(data[question]['text'])

    prompt = data[question]['text']

    text = openai.Completion.create(
        model=model_param,
        prompt=prompt,
        max_tokens=max_tokens_param,
        temperature=temperature_param,
        n=n_param
    )

    for choice in text['choices']:
        print(choice['text'])

    answers[ question ] = dict()
    answers[ question ]['question'] = prompt
    answers[ question ]['answer'] = choice['text'].lstrip()

# Save script end time
end_time = datetime.datetime.now()
execution_time = end_time - start_time
answers['Execution Time'] = str(execution_time)

# Save parameters
answers['OpenAI Parameters'] = 'Model: ' + model_param + ', Max. Tokens: ' + str(max_tokens_param) + ', Temperature: ' + str(temperature_param) + ', N: ' + str(n_param) + ''

# Write answers to JSON file
with open(args.output, 'w') as outfile:
  json.dump(answers, outfile, indent=4)

# Done
print("Finished.")
