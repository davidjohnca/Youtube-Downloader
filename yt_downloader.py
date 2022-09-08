''' Import the necessary libraries, in this case 
YouTube from the library pytube, and ssl '''

from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

''' Create a link variable where you can input 
the url of the video you want to download '''

link = str(input('Enter your link: '))
print('Please wait...')

yt = YouTube(link)

''' With the following methods you are able to
get the highest resolution available and then 
download the video '''

stream = yt.streams.get_highest_resolution()
stream.download()

print('Download succesful!')
