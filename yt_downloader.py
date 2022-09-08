from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

link = str(input('Enter your link: '))
print('Please wait...')
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()

print('Download succesful!')
