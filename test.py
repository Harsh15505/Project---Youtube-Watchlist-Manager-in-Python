import requests
url = input("Enter a Url : ")
video_id = url.split('v=')[-1]
api_key="AIzaSyD6tbPV59RPi5or34m3mto3LqkWJwxub1Y"

data = requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails")
youtube_data = data.json()

video_title = youtube_data['items'][0]['snippet']['title']
video_duration = youtube_data['items'][0]['contentDetails']['duration']
time={}

print(video_title)
print(video_duration)

raw_duration = youtube_data['items'][0]['contentDetails']['duration'].split('PT')[-1].split('M')
video_min = raw_duration[0]
video_seconds = raw_duration[1][:int(len(raw_duration[1])-1)]
print(video_min , video_seconds)


#total_duration = video_duration.split('PT')[-1].split('M')
#min = total_duration[0]
#print(total_duration[1][:int(len(total_duration[1]))-1])



