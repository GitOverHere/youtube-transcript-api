from youtube_transcript_api import YouTubeTranscriptApi
import os
import sys
import time
import traceback
default_location = "transcripts/"

print("****YOUTUBE TRANSCRIBER****")

print("Hey There! Please enter the video id for the video you wish to transcribe.\n It can be found right next to ?v=[video_id_here]")

id = input()

print("******************************************")
print("Save to file or display on terminal?")
print("1. Save To File")
print("2. Display On Terminal (not recommended)")
print("******************************************")

option = input()

if(option == "1"):
 success = False
 while(~success):
  print("What is the file name? Leave blank for video id name.")
  filename = input()
  if(filename == ""):
   filename = id+".txt"  
  print("Where should I save the file? If blank it will save in default lcoation. Include one forward slash at the end.")
  location = input()
  if(location == ""):
   location = default_location
 
 
  try:
   if(os.path.exists(location+filename)):
    with open(location+filename+"-"+str(time.time()),"w") as file:
     file.write(str(YouTubeTranscriptApi.get_transcript(id)))
   else:
    with open(location+filename,"w") as file:
     file.write(str(YouTubeTranscriptApi.get_transcript(id)))
   success = True
  except Exception as e:
   print("Sorry! I could not save the file to that location")
   print("Error info down below.")
   print(e)
   traceback.print_exc()
  
  
elif(option == "2"):
 print("***begin transcirpt***")
 print(YouTubeTranscriptApi.get_transcript(id))
 print("***end transcirpt***")

