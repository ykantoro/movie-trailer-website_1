import media
import fresh_tomatoes


# dictionary of movie titles with movie properties
films = {
    "Garfield: The Movie": ["Based on the popular comic \
strip, this live-action\ comedy follows the exploits \
of Garfield (Bill Murray), \
the large, lazy and wisecracking cat \
owned by hapless Jon \
Arbuckle (Breckin Meyer). Jon's other \
housemate, Odie, is a dim \
but sweet dog who frequently annoys Garfield. \
When the conniving \
orange feline gets fed up with Odie, he devises \
a way to get rid of \
the pooch. However, after Garfield has a change \
of heart about \
Odie, he must find a way to get his fellow pet back.",
                            "http://www.gstatic.com/tv/thumb/movie\
posters/34575/p34575_p_v7_aa.jpg",
                            "https://www.youtube.com/watch?\
v=4UlzK3X9ddQ",
                            "June 6, 2004",
                            media.Movie.VALID_RATINGS[2]],
    "Cats & Dogs": ["Cats and Dogs uncovers the truth about\
the high-tech, secret \
war being waged in neighborhoods everywhere \
that humans aren't even \
aware of: an eternal struggle between the two \
great armies of Cats and \
Dogs. The story follows a Cat plan to destroy a \
new vaccine that, if \
developed, would destroy all human allergies to \
Dogs, and the Dogs' \
efforts to stop the Cats from executing their plan.",
                    "http://www.gstatic.com/tv/thumb/movieposters/\
27959/p27959_p_v7_aa.jpg",
                    "https://www.youtube.com/watch?v=qzBD_8zOGVA",
                    "July 4, 2001",
                    media.Movie.VALID_RATINGS[2]],
    "The Aristocats": ["When a retired opera singer leaves her \
inheritance to her cat, \
Duchess (Eva Gabor), and three kittens, \
the woman's butler drugs the \
cats and abandons them in the countryside in \
order to inherit the \
fortune himself. Lost in unfamiliar territory, \
Duchess and the kittens \
meet Thomas O'Malley (Phil Harris), an alley cat \
willing to help them \
return to their home in Paris. They meet several \
kooky characters along \
the way, including two English geese and an alley \
cat jazz band.",
                       "http://www.gstatic.com/tv/thumb/movieposters/\
19375/p19375_p_v7_aa.jpg",
                       "https://www.youtube.com/watch?v=wjA5LWNUPDY",
                       "December 24, 1970",
                       media.Movie.VALID_RATINGS[1]],
    "The Cat In The Hat": ["In this live-action film based \
on the favorite children's tale, \
the trouble-making Cat in the Hat (Mike Myers) \
arrives at the home \
of bored young Sally Walden (Dakota Fanning) \
and her brother, \
Conrad (Spencer Breslin), while their mother \
(Kelly Preston) is out. \
The family's pet fish (Sean Hayes) objects to the \
Cat's presence, but \
that doesn't stop the hat-wearing giant feline \
from trying to have fun, \
no matter how much destruction is left in his wake.",
                           "http://upload.wikimedia.org/wikipedia\
/en/d/db/Cat_in_the_hat.jpg",
                           "https://www.youtube.com/watch?v=4KNKiFud9oM",
                           "November 8, 2003",
                           media.Movie.VALID_RATINGS[2]],
    "Puss in Boots": ["Long before meeting Shrek, \
Puss in Boots (Antonio Banderas) -- just \
named a hero for saving a woman from a charging \
bull -- is run out of \
town on suspicion of bank robbery, even though the \
real villain is \
Puss' friend, Humpty Dumpty (Zach Galifianakis). \
Though there is \
still animosity between them, Puss and Humpty reunite \
to steal a goose \
that lays golden eggs. Joining them for the adventure \
of nine lifetimes \
is notorious cat burglar, Kitty Softpaws (Salma Hayek).",
                      "https://lh4.ggpht.com/u4AuPkrABNY25-HkH-s1J\
GK1gks6LHK8U5FkENxmInJ3pE3-Na4TIsrCvOVN5xjLQCHs=w300",
                      "https://www.youtube.com/watch?v=LKHwaWZdXZU",
                      "October 28, 2011",
                      media.Movie.VALID_RATINGS[2]],
    "The Lion King": ["This Disney animated feature follows \
the adventures of the young \
lion Simba (Jonathan Taylor Thomas), the heir of \
his father, Mufasa \
(James Earl Jones). Simba's wicked uncle, Scar (Jeremy Irons), \
plots to usurp \
Mufasa's throne by luring father and son into a stampede of \
wildebeests. But \
Simba escapes, and only Mufasa is killed. Simba returns \
as an adult (Matthew Broderick) \
to take back his homeland from Scar with the help of his friends \
Timon (Nathan Lane) and Pumbaa (Ernie Sabella)",
                      "http://ia.media-imdb.com/images/M/MV5BMjEyMzg\
wNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_SX640_SY720_.jpg",
                      "https://www.youtube.com/watch?v=MPugv1k7r-s",
                      "June 15, 1994",
                      media.Movie.VALID_RATINGS[1]]
    }

# array to hold media.Movie class instances
movies = []

# Loop to create instances from dictionary items
for title, properties in films.iteritems():

    globals()[title] = media.Movie(title,
                                   properties[0],
                                   properties[1],
                                   properties[2],
                                   properties[3],
                                   properties[4])

    # addes movie instances to movies array
    movies.append(globals()[title])

# sends movie instances to fresh_tomatoes.py to create webpage
fresh_tomatoes.open_movies_page(movies)
