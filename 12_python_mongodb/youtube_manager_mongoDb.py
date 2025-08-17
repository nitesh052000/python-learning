from pymongo import MongoClient
from bson import ObjectId

uri = "mongodb+srv://mongodb:FSbp50kVGcomBKyU@cluster0.ldbebyh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client["youtube_manager"] 
video_collection = db["videos"]
print("✅ Connected to MongoDB!",video_collection)

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def list_videos():
    for video in video_collection.find():
       print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(video_id,name,time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":name,"time":time}})

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name")
            time = input("Enter the video time")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video ID to update:")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter video Id to delete")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
