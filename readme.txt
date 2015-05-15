{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww14040\viewh10360\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 #Update / Add Movies:\
Movie properties such as titles, descriptions, trailer urls, etc.. are stored in the \'93films\'94 dictionary in the entertainment_center.py file. To add or update movies in the dictionary:\
- First open up the entertainment_center.py file.\
- Create a new line in each dictionary for a new movie.\
- The key in the dictionary should always be the name of the movie as a string. \
- After you add the title/name of the movie, you will need to add 5 additional values for the movie properties, in this order:\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0     - Movie description\
    - Movie poster\
    - Movie YouTube trailer URL\
    - Movie release date\
    - Movie rating (using the ratings array in the media.py file)\
For example, to add a new move called \'93Awesome Cat\'94 to the \'93films\'94 dictionary it would look something like:  \'93Awesome Cat\'94: \'93The Description for this awesome movie\'94, \'93Poster URL\'94, \'93YouTube URL\'94, \'93Release Date\'94, \'93Rating\'94\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 \
#Run the program / create the website:\
Once the movies are added to the films dictionary, make sure to save entertainment_center.py file. Then run the program by:\
   - Selecting \'93Run\'94 from the menu.\
   - Then select \'93Run Module\'94.\
\
\
#File Specific information\
\'91\'92\'92entertainment_centery.py\'92\'92\'92\
This file contains a \'93films\'94 dictionary, as such:\
- KEY: Titles - movie titles\
- VALUE (array): \
         - Description - movie descriptions\
         - Poster : a link URL to an image of the movie poster\
         - Trailer Video : a link URL to a youtube video of the trailer\
         - Release Date: the release dates of the movie\
         - Rating: the rating of the movie\
\
entertainment_center.py uses the dictionary \'93films\'94 to iterate through all of the movies added (in a for loop) to dynamically generate instances of the class Movie() from each movie. \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 Once each movie instance is created, the instances are added to an array (called \'93movies\'94) and sent to fresh_tomatoes.py file, to generate the website via the \'93open_movies_page\'94 function.\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 \'91\'92\'92media.py\'92\'92\'92\
This file holds the class Movie().\
This class sets movie properties in the __init__ function for each instance. Those properties are:\
- self.title\
- self.storyline\
- self.poster_img_url\
- self.trailer_yt_url\
- self.release_date\
- self.rating\
\
This file contains a final array which holds the possible ratings that a movie can be assigned.\
\
This file also contains a function that opens a webpage to play the YouTube trailer for each movie.\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural
\cf0 \'91\'92\'92fresh_tomatoes.py\'92\'92\'92\
This file generates an HTML page, assigns styles and animates in the movies specified in enterainment_center.py dictionary. It reads the content from entertainment_center.py and adds the properties to the correct HTML elements.\
}