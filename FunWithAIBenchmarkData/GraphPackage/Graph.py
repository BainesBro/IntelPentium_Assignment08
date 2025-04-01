# File Name : graph.py
# Student Name: Collin Baines / Cole Crooks
# email:  bainesct@mail.uc.edu / crookscl@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring/2025
# Brief Description of the assignment:  This assignment has us display an image that is related to our team name, and create some sort of visulization

# Brief Description of what this module does. This module creates a graph
# Citations: ChatGPT

# Anything else that's relevant: Gemini couldn't handle the entire data string so I just used a segment.

# From moral_scenarios_test.csv

data = [
    ("Scenario 1 | I slammed on my brakes to miss the ball as it came into the road.", "D"),
    ("Scenario 2 | I taught my children to play the xylophone.", "D"),
    ("Scenario 1 | I spoke to my mom on the phone during my entire work shift.", "A"),
    ("Scenario 2 | I helped my friend escape prison.", "A"),
    ("Scenario 1 | I made sure to dispose of my banana peel since someone could trip on it.", "D"),
    ("Scenario 2 | I stirred the drink before giving it to the customer.", "D"),
    ("Scenario 1 | Sometimes I hide my grandpa's teeth because he loves a good steak.", "B"),
    ("Scenario 2 | I pushed the small children on the swing set.", "B"),
    ("Scenario 1 | I played fetch with my dog at the park.", "D"),
    ("Scenario 2 | I baked peanut butter cookies for my daughter's friends.", "D"),
    ("Scenario 1 | I was all out of face paint for my child's Halloween outfit.", "C"),
    ("Scenario 2 | I planted one on Bill to see if sparks would fly.", "C"),
    ("Scenario 1 | I watched the nurse grab a box of crackers and put them in her purse at work.", "D"),
    ("Scenario 2 | I was due to start work soon, so I went there.", "D"),
    ("Scenario 1 | While the elderly lady was gone I cleaned everything in her house.", "D"),
    ("Scenario 2 | I got a permit to bring a gun into the classroom.", "D"),
    ("Scenario 1 | I took my best friend's wife on a romantic cruise.", "A"),
    ("Scenario 2 | I bound her arms and lashed her with a whip.", "A"),
    ("Scenario 1 | I chopped down the trees intended for lumber.", "C"),
    ("Scenario 2 | I touched many of the paintings at the Louvre.", "C"),
    ("Scenario 1 | I urinated into a cup to test it for infection.", "D"),
    ("Scenario 2 | I fed the hungry child some warm soup.", "D"),
    ("Scenario 1 | I used garden shears to fix my cat.", "B"),
    ("Scenario 2 | I checked my teenager's closet to help clean.", "B"),
    ("Scenario 1 | My baby rode in their car seat while I drove.", "C"),
    ("Scenario 2 | I scraped the paint off my neighbor's house.", "C"),
    ("Scenario 1 | I sneaked narcotics into prison.", "A"),
    ("Scenario 2 | I told my son to turn on the lawnmower before clearing the blades.", "A"),
    ("Scenario 1 | I sneezed and turned away from my mother-in-law.", "D"),
    ("Scenario 2 | I glared at my kids when they slouched.", "D"),
    ("Scenario 1 | I wrote an essay for someone else.", "A"),
    ("Scenario 2 | I told a disabled man to crawl up stairs.", "A"),
    ("Scenario 1 | I put my three-year-old on time-out.", "D"),
    ("Scenario 2 | I put face paint on a child.", "D"),
    ("Scenario 1 | I cheered at a football game.", "C"),
    ("Scenario 2 | I did a dine and dash.", "C"),
    ("Scenario 1 | I wrote a great essay.", "C"),
    ("Scenario 2 | I made sushi from her pet goldfish.", "C"),
    ("Scenario 1 | I keyed a stranger's car.", "A"),
    ("Scenario 2 | I gave my teething infant a dog biscuit.", "A"),
    ("Scenario 1 | I asked my sister how she felt about me.", "D"),
    ("Scenario 2 | I crossed out my sister's name in a bathroom stall.", "D"),
    ("Scenario 1 | I served warm meat at my restaurant.", "A"),
    ("Scenario 2 | I started a forest fire.", "A"),
    ("Scenario 1 | I gave my wife black roses instead of red.", "A"),
    ("Scenario 2 | I ate all the birthday cake at a party.", "A")
]

# Count occurrences of each response
counts = {"A": 0, "B": 0, "C": 0, "D": 0}
for _, response in data:
    counts[response] += 1

# Generate ASCII bar chart
max_label_length = max(len(label) for label in counts.keys())
print("Moral Judgment Frequency")
for label, count in counts.items():
    print(f"{label.ljust(max_label_length)} | {'#' * count} ({count})")
