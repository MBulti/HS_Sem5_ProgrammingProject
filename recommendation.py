listOfMovies = {}
listOfRecommendations = []


def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            movie = line.split(',')
            movie_id = movie[0]
            movie_title = movie[1]
            movie = movie[2:-1]
            if(movie.count('') < len(movie)):
                movie_title += ','.join(movie)
            listOfMovies[movie_id] = movie_title               
        return listOfMovies


def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None


# def load_data():
#     with open("netflix_rating.csv", mode = "w") as nf:
#         rating_files = ['combined_data_4.txt'] 
#         for file in rating_files:
#             with open(file) as f:
#                 for line in f:
#                     line = line.strip()
#                     if line.endswith(":"):
#                         movie_id = line.replace(":", "")
#                     else:
#                         row_data = []
#                         row_data = [item for item in line.split(",")]
#                         row_data.insert(0, movie_id)
#                         nf.write(",".join(row_data))  
#                         nf.write('\n')

    