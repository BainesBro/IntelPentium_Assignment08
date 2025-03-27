# File Name : Image.py
# Student Name: Collin Baines / Cole Crooks
# email:  bainesct@mail.uc.edu / crookscl@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring/2025
# Brief Description of the assignment:  This assignment has us display an image that is related to our team name, and create some sort of visulization

# Brief Description of what this module does. This module allows an image to be shown.
# Citations: ChatGPT

# Anything else that's relevant:

import os

def display_image(image_path):
    """Open the image in the default viewer."""
    if os.path.exists(image_path):  # Check if the file exists
        os.startfile(image_path)  # Open the image with the default viewer
    else:
        print(f"Error: The file {image_path} was not found.")