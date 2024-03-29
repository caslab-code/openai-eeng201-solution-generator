
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
import json
import argparse
import subprocess

# Setup argument parser
parser = argparse.ArgumentParser(description='Generate a PDF document with solutions, based on input JSON file with solutions.',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--input', dest='input', type=str, required=True,
          help='Name of the input JSON file with the solutions.')
parser.add_argument('-o', '--output', dest='output', type=str, required=True,
          help='Name of the output PDF file.')
args = parser.parse_args()

# Read in JSON solutions file
with open(args.input, "r") as json_file:
    solutions = json.load(json_file)

# Generate *.tex document based on the JSON file contents
tex_file_name = os.path.splitext( args.output )[0] + '.tex'

with open(tex_file_name, "w") as tex_file:
   tex_file.write('\\documentclass{article}\n')
   tex_file.write('\\usepackage[letterpaper, margin=1in]{geometry}\n')
   tex_file.write('''
\\usepackage{listings}
\\lstset{
basicstyle=\small\\ttfamily,
columns=flexible,
breaklines=true
}\n''')
   tex_file.write('\\begin{document}\n')
   tex_file.write('\\title{\\textbf{Solutions PDF Generated from:\\\\ ' + args.input + '}}\n')
   tex_file.write('\\date{}\n')
   tex_file.write('\\maketitle')
   tex_file.write('\n')

   for question in solutions:

       if isinstance(solutions[question], dict):

           question_text = solutions[question]['question']
           print(question_text)
           answer_text = solutions[question]['answer'].lstrip()
           print(answer_text)

           tex_file.write('\\section*{' + question + '}\n')
           tex_file.write('\n')
           tex_file.write(question_text + '\n')
           tex_file.write('\n')
           tex_file.write('\\begin{lstlisting}\n')
           tex_file.write(answer_text + '\n')
           tex_file.write('\\end{lstlisting}\n')
           tex_file.write('\n')

       else:

           tex_file.write('\\section*{' + question + '}\n')
           tex_file.write('\n')
           tex_file.write('\\begin{verbatim}\n')
           tex_file.write(str(solutions[question]) + '\n')
           tex_file.write('\\end{verbatim}\n')
           tex_file.write('\n')

   tex_file.write('\end{document}\n')

# Generate PDF form tex document
directory = os.path.dirname(tex_file_name)
subprocess.run(["pdflatex", "-output-directory="+directory, tex_file_name])

# Do some cleanup
aux_file = os.path.splitext( args.output )[0] + '.aux'
subprocess.run(["rm", aux_file])
log_file = os.path.splitext( args.output )[0] + '.log'
subprocess.run(["rm", log_file])
tex_file = os.path.splitext( args.output )[0] + '.tex'
subprocess.run(["rm", tex_file])

# Done
print("Finished.")
