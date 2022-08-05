import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #Raises a confirmation message in our terminal when the bot has succesfully connected to the server and is online

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    inp = message.content
    new_inp2 = inp.replace(" ", "_")
    new_inp3 = new_inp2.title()

    headers = {'User-Agent': 'YOUR HEADERS HERE (SEE README){new_inp3}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    new_soup = soup.find('span', class_='text-flavor').parent
    soup_pr = new_soup.get_text(strip=True, separator="\n")

    print(soup_pr)
    #returns our search results to the terminal for debugging if needed.

    if soup_pr is None:
        await message.channel.send('Error! Your search input was incorrect or invalid. ')
    else:
        await message.channel.send(soup_pr)

        print(soup_pr)

client.run('YOUR TOKEN HERE (SEE README)')
