import requests
from lxml import html

show_name = input("Enter Show Name: ")   # "bleach"
url = f'https://next-episode.net/{show_name}'

response = requests.get(url)

tree = html.fromstring(response.content)

episode_name = tree.xpath('//*[@id="next_episode"]/div[3]/div[2]')
time_value = tree.xpath('//*[@id="next_episode"]/span/text()')
air_date = tree.xpath('//*[@id="next_episode"]/text()[8]')
season = tree.xpath('//*[@id="next_episode"]/text()[10]')
episode = tree.xpath('//*[@id="next_episode"]/div[11]/div[2]')


print("Episode Name: ",episode_name[0].text_content().strip() if episode_name else 'No name found')
print("Time to Air: ",time_value[0] if time_value else 'No time value found')
print("Air Date: ",air_date[0].strip() if air_date else 'No date found')
print("Season/Episode: ", f"{season[0].strip()}/{ episode[0].text_content().strip()}")