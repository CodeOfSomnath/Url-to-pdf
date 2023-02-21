import requests
from bs4 import BeautifulSoup
import os

def convert(url):
  response = requests.post('https://api.pdfshift.io/v3/convert/pdf',
                           auth=('api', '36f08769dc7145f5938dc776708d0b77'),
                           json={'source': url},
                           stream=True)

  response.raise_for_status()
  n = ""
  b = ""
  for u in url.split('/')[2:]:
    n = n+ b + u
    b = '_'
  name = f"pdf/{n}.pdf"
  if os.path.isfile(name):
    pass
  else:
   print(name)
  with open(name, 'wb') as output:
     for chunk in response.iter_content(chunk_size=1024):
       output.write(chunk)


# specify the URL of the website
url = "https://pkg.go.dev/std"
findUrl = "https://pkg.go.dev"

# make a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.text

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# find all anchor tags in the HTML content
anchor_tags = soup.find_all('a')

# extract the href attribute from each anchor tag
urls = [tag.get('href') for tag in anchor_tags]

urlFiltered = []
# print the list of extracted URLs
for u in urls:
  if u.startswith('/') and (not u.startswith('/go')) and u != '/' and (
      "std" not in u) and ("about" not in u) and ("debug" not in u) and (
        "internal" not in u) and ("testing" not in u) and ("unsafe" not in u):
    urlFiltered.append(findUrl + u)

# pdf making


# covert pdf
for u in urlFiltered:
  convert(u)