

while True:
    print("\n YouTube Manager | Enter your choice")
    print("1. List all youtube videos")
    print("2. Add a new youtube video")
    print("3. Delete a youtube video")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")


    if choice == '1':
        from youtube_manager import list_videos
        list_videos()
    elif choice == '2':
        from youtube_manager import add_video
        add_video()
    elif choice == '3':
        from youtube_manager import delete_video
        delete_video()
    elif choice == '4':
        print("Exiting YouTube Manager. Goodbye!")
        break

