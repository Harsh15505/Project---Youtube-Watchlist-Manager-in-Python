import csv
import datetime as dt
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("Google_API_key")

config_file_path = os.path.join(os.path.dirname(__file__), 'config.txt')
watchlist_file_path = os.path.join(os.path.dirname(__file__), 'YoutubeWatchList.csv')

def load_data():
        
        content = []
      

        try :
            with open(config_file_path, 'r') as config_file:
                days_limit = int(config_file.read().strip())   
                
        except FileNotFoundError:
            days_limit = 30
            
        
        try :
            with open(watchlist_file_path, 'r') as file:
                reader = csv.reader(file)      
                for row in reader:
                    video = {'Title': row[0] , 'Duration': row[1], 'Speed': row[2], 'link': row[3], 'time required': row[4],'Date added': row[5]}
                    content.append(video)
                
        except FileNotFoundError:
            pass

        return days_limit,content

def save_data(video):
       
        with open(watchlist_file_path, 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            for data in video:
                writer.writerow([data['Title'], data['Duration'], data['Speed'], data['link'], data['time required'],data['Date added']])
        
def fetch_youtube_data(url):
   
    video_id = url.split('v=')[-1]
    data = requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails")
    youtube_details = data.json()
    video_title = youtube_details['items'][0]['snippet']['title']
    
    raw_duration_hours = youtube_details['items'][0]['contentDetails']['duration'].split('PT')[-1].split('H')

    if len(raw_duration_hours) == 2:    
        raw_duration = raw_duration_hours[1].split('M')
        video_hours=raw_duration_hours[0]
        
        if len(raw_duration) == 2:    
            video_min = raw_duration[0]
            video_seconds = raw_duration[1][:int(len(raw_duration[1])-1)]
        
        elif len(raw_duration) == 1:
            video_min = 0
            video_seconds = raw_duration[0][:int(len(raw_duration[0])-1)]
        
    elif len(raw_duration_hours) == 1:    
        raw_duration = raw_duration_hours[0].split('M')
        video_hours=0
        
        if len(raw_duration) == 2:    
            video_min = raw_duration[0]
            video_seconds = raw_duration[1][:int(len(raw_duration[1])-1)]
        
        elif len(raw_duration) == 1:
            video_min = 0
            video_seconds = raw_duration[0][:int(len(raw_duration[0])-1)]
            
    return [video_title,video_min,video_seconds,video_hours]


def convert_time_format(n):
    n = int(n)
    return str(dt.timedelta(seconds = n))
     

def list_videos(content,days_limit):
    
    print('\n ** List of all videos in Your watchlist ** \n')
    print("*"*70)
    for index , video in enumerate(content, start = 1):
        Days_Ago = (dt.datetime.now().date() - dt.datetime.strptime(video['Date added'], '%d/%m/%Y').date()).days
        if Days_Ago > days_limit:
            remove_video(content,index)
            continue
        print(f"\n{index}. Title : {video['Title']} , Total Duration : {convert_time_format(video['Duration'])} , Speed : {video['Speed']}x , URL : {video['link']} , Time required to watch : {convert_time_format(video['time required'])} , Video added {Days_Ago} days ago. \n")
        
    print("\n")
    print("*"*70)


def add_video(video):
    
    link = input("Enter link: ")
    video_details = fetch_youtube_data(link)
    Title = video_details[0]
    Duration = (int(video_details[3]) * 3600) + (int(video_details[1]) * 60) + int(video_details[2])
    Speed = input("Enter Speed: ")


    video.append({'Title': Title , 'Duration': Duration, 'Speed': Speed, 'link': link, 'time required': int(Duration/float(Speed)) , 'Date added': dt.datetime.now().strftime("%d/%m/%Y")})
    
    save_data(video)
    

def remove_video(content,index):
    if index > 0 and index <= len(content):
        del content[index - 1]
        save_data(content)
        print("Video removed successfully!")
    else :
        print("Invalid index.")


def total_time_counter(content):
    total_time = 0
    for video in content:
        total_time += float(video['time required'])
    print("Total time required to watch all videos with desired speed is : ",convert_time_format(total_time))

def Change_Config(days_limit):
    with open(config_file_path, 'w') as file:
        file.write(str(days_limit))




def main():
    while True:
        days_limit,content=load_data()

        print(" \t \n || Youtube Manager || \n")
        print("** Choose an option from below **")
        print("1.List all videos in watchlist.")
        print("2.Add a video to watchlist.")
        print("3.Remove a video from watchlist.")
        print("4.Total 0f time required to watch all videos.")
        print(f"5.Change date limit (current date limit is {days_limit} days) ")
        print("6.Exit.")
        print(f"\nNote that : If a video is not removed from watchlist in {days_limit} days it will automatically be removed from the list \n")
        
        
        choice = input("\nEnter your choice: ")

        match choice:
            
            case "1":
                list_videos(content,days_limit)

            
            case "2":
                add_video(content)
                print("Video added successfully!")

            case "3":            
                list_videos(content,days_limit)
                index = int(input("Enter the index of the video you want to remove: "))
                remove_video(content,index,)
            
            case "4":
                total_time_counter(content)

            case "5":
                days_limit = int(input("Enter new date limit in days: "))
                Change_Config(days_limit)
                print("Date limit changed successfully!")
            
            case "6":
                break
            case _:
                print("Invalid choice. Please try again.")
            


if __name__ == "__main__" :
    main()