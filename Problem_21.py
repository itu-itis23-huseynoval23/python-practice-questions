# Take the code from the How To Decode A Website exercise,
# and instead of printing the results to a screen, write the results to a txt file.

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

filename = input("File to save to: ")

with open(filename, 'w') as f:
  for story_heading in soup.find_all(class_="story-heading"): 
      if story_heading.a: 
          f.write(story_heading.a.text.replace("\n", " ").strip())
      else: 
          f.write(story_heading.contents[0].strip())