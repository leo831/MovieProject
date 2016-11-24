import media
import fresh_tomatoes

"""
Author: Leobardo Lara
Title: Movie Trailer Websire
Created: 22-Nov-2016
"""


# Warcraft movie instance
warcraft_movie = media.Movie("Warcraft",
                             "looking to escape from his dying world.",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcTCzditN2MtHjUM51mMbNspnJ_NHPWYz3J8zQMoXPRtAeBTpTrf",
                             "https://www.youtube.com/watch?v=7p43xwId1eE")
# Suicide movie instance
suicide_movie = media.Movie("Suicide Squade",
                            "Figuring they're all expendable, a U.S. intelligence officer decides to assemble a team of dangerous, incarcerated supervillains for a top-secret mission. ",
                            "http://www.gstatic.com/tv/thumb/movieposters/11319046/p11319046_p_v8_ai.jpg",
                            "https://www.youtube.com/watch?v=fyJH39ZbPAg")

# Captain America movie instance
captain_america = media.Movie("Captain America: Civil War",
                              "Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage. The new status quo deeply divides members of the team.",
                              "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRhP_sl7z7Pr71xPOHE2RYcedgW3JvhUEVMrkWrIyMdZnLisgJUG_Y7hw",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us")
# Batman vs Superman movie instance
batman_superman = media.Movie("Batman v Superman: Dawn of Justice",
                              "It's been nearly two years since Superman's (Henry Cavill) colossal battle with Zod (Michael Shannon) devastated the city of Metropolis.",
                              "http://t1.gstatic.com/images?q=tbn:ANd9GcS61fdKkVcQIKtObjNGAELqVwyzhwFoIfNGZVbC-rqta12xBfLa",
                              "https://www.youtube.com/watch?v=_H0Ppo41_2k")
# The purge movie instance
purge_movie = media.Movie("The Purge: Election Year",
                          "As a young woman, Sen. Charlie Roan survived the annual night of lawlessness that took the lives of her family members. As a presidential candidate, Roan is determined to end the yearly tradition of blood lust once and for all. ",
                          "https://www.uphe.com/sites/default/files/styles/scale__344w_/public/Purge3_PosterArt.jpg?itok=w3988nSV",
                          "https://www.youtube.com/watch?v=7WlUVTTervg")
# Xmen movie instance
xmen_movie = media.Movie("X-Men: Apocalypse",
                         "X-Men: Apocalypse is a 2016 American superhero film based on the fictional X-Men characters that appear in Marvel Comics. It is the ninth installment in the X-Men film series and a sequel to X-Men: Days of Future Past.",
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGGUCnZUo21NneIsqAXG1-BpyiXiZvVovv8ju4jBtPjPY18iDFOQrFEA",
                         "https://www.youtube.com/watch?v=kFXV-9jftLk")

# create an array to store movies instances.
movies = [warcraft_movie, suicide_movie, captain_america, batman_superman, purge_movie, xmen_movie]
# send movie array information to the open_movie_page method from fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
