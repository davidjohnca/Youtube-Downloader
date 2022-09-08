''' Import the necessary libraries, in this case 
YouTube from the library pytube, and ssl '''

from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

''' Create a link variable for the user to input 
the url where they want to download the video from '''

link = str(input('Enter your link: '))
print('Please wait...')

yt = YouTube(link)

''' With the following method you are able to
get the highest resolution available and then 
download the video '''

stream = yt.streams.get_highest_resolution()
stream.download()

print('Download succesful!')
