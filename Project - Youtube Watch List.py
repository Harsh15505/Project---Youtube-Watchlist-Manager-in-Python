import csv
import datetime as dt
import os

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
        with open(watchlist_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for data in video:
                writer.writerow([data['Title'], data['Duration'], data['Speed'], data['link'], data['time required'],data['Date added']])
        
def list_videos(content,days_limit):
    print('\n ** List of all videos in Your watchlist ** \n')
    print("*"*70)
    for index , video in enumerate(content, start = 1):
        Days_Ago = (dt.datetime.now().date() - dt.datetime.strptime(video['Date added'], '%d/%m/%Y').date()).days
        if Days_Ago > days_limit:
            remove_video(content,index)
            continue
        print(f"\n{index}. Title : {video['Title']} , Total Duration : {video['Duration']} mins , Speed : {video['Speed']}x , URL : {video['link']} , Time required to watch : {video['time required']} mins , Video added {Days_Ago} days ago. \n")
        
    print("\n")
    print("*"*70)

def add_video(video):
   
    Title = input("Enter Title: ")
    Duration = input("Enter Duration (in rounded mins): ")
    Speed = input("Enter Speed: ")
    link = input("Enter link: ")
    video.append({'Title': Title , 'Duration': Duration, 'Speed': Speed, 'link': link, 'time required': round((float(Duration)/float(Speed)),2) , 'Date added': dt.datetime.now().strftime("%d/%m/%Y")})
    
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
    print("Total time required to watch all videos with desired speed is : ",total_time)

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