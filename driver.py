from pytube import YouTube

url = input('Enter Video URL: ')
yt = YouTube(url)
videos = yt.streams.all()
video = list(enumerate(videos))

for i in video:
    print(i)

print('Enter the desired option to download')
option = int(input('Eneter the option: '))
res = videos[option]
res.download()
print('Download Sucessful.')