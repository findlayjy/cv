from scholarly import scholarly, ProxyGenerator
import re
import datetime

# Google doesn't like bots and will block you, so scholarly lets you use proxies to get around this

# This first option uses the pip free-proxy library, but it didn't solve the issue for me
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

# This option uses Tor, but requires you to have a local install of Tor on your system
pg = ProxyGenerator()
pg.Tor_Internal(tor_cmd = "tor")
scholarly.use_proxy(pg)

# Load my profile using my unique ID (the part after 'user=' in your profile URL)
my_profile = scholarly.fill(scholarly.search_author_id('Q2v46FwAAAAJ'))

# A case-insensitive regular expression to capture variations on my name
name_regex = re.compile('J(\.|amie)? ?Y?(\.|ates)? ?Findlay', re.IGNORECASE)

publications_list = []
for publication in my_profile['publications']:
    others_cite_count = 0
    if 'citedby_url' in scholarly.fill(publication): # Entries with no citations have no citedby_url key(?) and this will cause the script to fails
        citers = scholarly.citedby(publication)
        for pub in citers:
            if not [x for x in pub['bib']['author'] if re.match(name_regex, x)]: # Check that I'm not the author
                others_cite_count += 1
    publication['others cite count'] = others_cite_count
    # publications_list.append((publication['bib']['title'], others_cite_count, publication['num_citations']))

# Print a list of publications in descending order of number of non-self-citations, with the total number of citations including self-citations in square brackets
[print(f"{pub['bib']['title']}: {pub['others cite count']} [{pub['num_citations']}]") for pub in sorted(my_profile['publications'], key = lambda x: x['others cite count'], reverse = True)]

# Print a list of publications in date order, most recent first, with non-self-citations, and total citations in square brackets
# [print(f"{pub['bib']['title']}: {pub['others cite count']} [{pub['num_citations']}]") for pub in sorted(my_profile['publications'], key = lambda x: x['bib']['pub_year'], reverse = True)]
