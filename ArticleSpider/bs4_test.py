from bs4 import BeautifulSoup

text = "<p>MATRIX  is an open-source blockchain that supports smart contracts...</p>" \
       "<p><strong>What is the ticker?</strong></p>"
soup = BeautifulSoup(text, "html.parser")
print(soup.get_text())
