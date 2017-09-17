import media
import fresh_tomatoes

spy = media.Movie("Spy",
                  "2015",
                  "A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster.",
                  "https://upload.wikimedia.org/wikipedia/en/5/5d/Spy2015_TeaserPoster.jpg",
                  "https://www.youtube.com/watch?v=ltijEmlyqlg")


guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "2014",
                                      "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                                      "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA")


fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "2016",
                               "The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school",
                               "https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                               "https://www.youtube.com/watch?v=Vso5o11LuGU")


the_secret_life_of_pets = media.Movie("The Secret Life of Pets",
                                      "2016",
                                      "The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.",
                                      "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                                      "https://www.youtube.com/watch?v=eWI_Jsw9qUs")

iron_Man_3 = media.Movie("Iron Man 3",
                         "2013",
                         "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.",
                         "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

transformer_3 = media.Movie("Transformers: Dark of the Moon",
                            "2011",
                            "The Autobots learn of a Cybertronian spacecraft hidden on the moon, and race against the Decepticons to reach it and to learn its secrets.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bf/Transformers_dark_of_the_moon_ver5.jpg",
                            "https://www.youtube.com/watch?v=E-Sg_zJrDxc")



movies = [guardians_of_the_galaxy, spy, fantastic_beasts, transformer_3, iron_Man_3, the_secret_life_of_pets]
# This function call uses above list of movie instances as input to generate a HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
