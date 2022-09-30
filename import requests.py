import requests
from bs4 import BeautifulSoupenter 

html_content = requests.get('https://www.timeshighereducation.com/world-university-rankings/2018/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats')
soup = bs4.BeautifulSoup(html_content, 'lxml')