from bs4 import BeautifulSoup
import requests

s = input("Insira o site a ser analisado: ")
# objeto site recebe conteúdo da requisição http
site = requests.get("https://www.facebook.com/").content

# objeto soup baixa o html do site
soup = BeautifulSoup(site, 'html.parser')

# pretify transforma html em string
print(soup.prettify())
