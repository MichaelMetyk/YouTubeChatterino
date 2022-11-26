import pytchat
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import scrapetube
from google_apis import create_service
from colorama import Fore
from colorama import Style



class main():
 def __init__(self, user):
  self.user = user

 def set_config():
     print("..setting config")


 def get_link(self):
  videos = scrapetube.get_search(self.user)

  for video in videos:
    video_id = (video['videoId'])
    return video_id


 def get_chat(video_id):
  file_name  = open("config.txt", "r+")



  chat = pytchat.create(video_id=video_id)
  if chat.is_alive():
   try:
    while chat.is_alive():
     for c in chat.get().sync_items():
        print ((f"{c.datetime} {file_name.readlines()[1:2]} [{c.author.name}]- {c.message}"))
   except:
    print("error has occured")

 def log(video_id):

  CLIENT_FILE = 'credientals.json'
  API_NAME = 'youtube'
  API_VERSION = 'v3'
  SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
  ]

  service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

  video_id = '<video id>'

  request_body = {
	 'snippet': {
		 'videoId': main.get_link(),
		 'topLevelComment': {
		 	'snippet': {
				'textOriginal': input("Reply")
			}
		}
	}
  }
  try:
   response = service.liveStreams().insert(
	part='snippet',
	body=request_body
 ).execute()
  except:
   print(response)



 def login(self):
   print(self.user)
   main.log(video_id=main.get_link(self))
   return True

 def login_bool(self):
  print(self.user)
  main.get_chat(video_id=main.get_link(self))
  if main.login():
   main.log(video_id = main.get_link(self))


