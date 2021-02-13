from pytube import YouTube


link = ('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#link = input("please enter the video url: ")

link = YouTube(link)

print("the video title is:{}".fomrat(link.title))
#print(f"the video description is:\n {video.description} \n ------------------")
