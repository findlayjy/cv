from scholarly import scholarly, ProxyGenerator
import re, json
import os
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

### Testing efficiency ###
# Import time module
import time
 # record start time
start = time.time()
##########################

# Load the previous run's data from a JSON file
try:
    with open('previous_run.json', 'r') as file:
        previous_run_data = json.load(file)
except FileNotFoundError:
    previous_run_data = {}

# Collect data
# My profile
my_profile = scholarly.fill(scholarly.search_author_id('Q2v46FwAAAAJ'), sections = ['publications'])

# My publications
publications_list = [scholarly.fill(publication) for publication in my_profile['publications']]

# Regex for checking if I am an author
name_regex = re.compile('J(\.|amie)? ?Y?(\.|ates)? ?Findlay', re.IGNORECASE)

# List for storing relevant info
publication_cite_counts = []

# Process data, adding a field for the number of non-self-citations
for publication in publications_list:
    others_cite_count = 0
    if not publication['num_citations'] == 0:
        citers = scholarly.citedby(publication)
        for pub in citers:
            if not [x for x in pub['bib']['author'] if re.match(name_regex, x)]: # Check that I'm not the author
                others_cite_count += 1
    publication_cite_counts.append({"title": publication['bib']['title'], "total citations": publication['num_citations'], "non-self citations": others_cite_count})

# Save the current run's data to a JSON file
with open('current_run.json', 'w') as file:
    json.dump(publication_cite_counts, file)

# # Compare the current data to the previous data and print with appropriate colouring
new_pub = True # Assume it's a new publication until we run into it in the previous list
for pub in sorted(publication_cite_counts, key=lambda x: x["non-self citations"], reverse = True):
    print_string = f"{pub['title']}: {pub['non-self citations']} [{pub['total citations']} total]"
    # If there is previous data for this publication, compare the current citation count to the previous count
    for previous_pub in previous_run_data:
        if pub["title"] == previous_pub["title"]:
            new_pub = False
            if pub["non-self citations"] > previous_pub["non-self citations"]:
                print(Fore.GREEN + print_string+f" up from {previous_pub['non-self citations']}")  # increased citation count
            else:
                print(print_string)  # unchanged citation count
            # break
    if new_pub == True:
        print(Fore.CYAN + print_string)  # new publication

# update the previous_run.json file
os.replace('current_run.json', 'previous_run.json')


### Testing efficiency ###
# record end time
end = time.time()
# print the difference between start and end time 
print("Time:",
      (end-start),"s")
