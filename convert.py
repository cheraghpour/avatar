import json

with open('transcript.json') as f:
    data = json.load(f)

textfile = open("transcript.txt", "w")

for d in data:
    if (d['character'] != "Scene Description" ):
        textfile.write(d['character'] + "\n" + d['character_words'] + "\n")

textfile.close()