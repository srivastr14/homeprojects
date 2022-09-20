import requests

word = str(input("Which word would you like to find rhymes for?").strip())

parameter = {"rel_rhy":word}
request = requests.get('https://api.datamuse.com/words',parameter)

rhyme_json = request.json()
print(rhyme_json)


for i in rhyme_json[0:5]:
    print(i['word'])
