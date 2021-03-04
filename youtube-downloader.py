from pytube import YouTube


link = ('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#link = input("please enter the video url: ")

video = YouTube(link)

print(f"the video title is:\n {video.title} \n ------------------")
print(f"the video description is:\n {video.description} \n ------------------")
