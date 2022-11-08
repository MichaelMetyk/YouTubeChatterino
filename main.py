import pytchat
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import scrapetube
from google_apis import create_service 




login = False



def get_link():
 videos = scrapetube.get_search(input("Enter Streamer Name"))

 for video in videos:
    video_id = (video['videoId'])    
    return video_id 
    

def get_chat(video_id):
 chat = pytchat.create(video_id=video_id)

 if chat.is_alive():
  try:
   while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
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
		'videoId': get_link(),
		'topLevelComment': {
			'snippet': {
				'textOriginal': input()
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

def login_bool():
   print("Do you want to login into youtube ? Enter yes or no")
   run_bool = input(str)
   if run_bool.lower() == "yes": return True
   else: get_chat(video_id=get_link())
	
if login_bool():
	video_id = get_link()
	log(video_id = video_id)
	
	get_chat(video_id = video_id)
	


