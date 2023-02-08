
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

import base64
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(description='Convert image to base64 string.',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--image', dest='image', type=str, required=True,
          help='Name of the input image file.')
args = parser.parse_args()

# Convert image to base64 string
with open(args.image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

print(encoded_string)

