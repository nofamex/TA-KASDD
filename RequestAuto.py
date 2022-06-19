import requests
import json

filename = "real_estate" 

f = open(f"/home/dzikri/CSUI/KASDD/Scraping/ID_Youtube/{filename}.txt", "r").read().splitlines() # List of ID based on category

simpenRes = []

begin = 0
end = 50
for i in range(0, 400): ## Scrape from youtube API V3
  response_API = requests.get(f'https://www.googleapis.com/youtube/v3/videos?id={",".join(f[begin:end])}&key=AIzaSyD_G2pQ8XHbk_nJK7JN1fNCQNPd1xv8emA&fields=items(id,snippet(publishedAt,channelTitle,title,categoryId),statistics,contentDetails(duration,definition,caption,licensedContent))&part=snippet,statistics,contentDetails')
  data = response_API.text
  for item in json.loads(data)['items']:
    simpenRes.append(item)
  begin += 50
  end += 50

## Create JSON
construct_json = {"items":simpenRes}
print(json.dumps(construct_json))

f2 = open(f"/home/dzikri/CSUI/KASDD/Scraping/Result_JSON/res_{filename}.txt", "w") # Write the output
f2.write(json.dumps(construct_json))
f2.close()