import json






def load_data():
    try:
        with open('youtube.txt' , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)
        

    

def list_videos(videos):
    for index , value in enumerate(videos , start=1):
        print(f"{index}.")

    
def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time:")
    videos.append({'name' : name ,  'time ': time })

    save_data_helper( videos)


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option:")
        print("1. List all youtube Video")
        print("2. Add a youtube Video")
        print("3. Update a youtube Videos")
        print("4. Delete a youtube Video")
        print("5. Exit the app ")

        choice = input("Enter your choice (1-5): ")
        print(videos)
        match choice :
            case '1':   
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break 
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()