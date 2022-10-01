from logging import error
import os, sys

def prepare_data():
    
    datasets = ['data/combined_data_1.txt','data/combined_data_2.txt','data/combined_data_3.txt','data/combined_data_4.txt']
    for file in datasets:
        if not os.path.isfile(file):
            raise FileNotFoundError('Not all the required files exist. Please download them and move the to the data folder!')
         
    if not os.path.isfile('data/netflix_rating.csv'):
        with open("data/netflix_rating.csv", mode = "w") as w:
            review_counter = 0
            for file in datasets:
                print(file)
                with open(file) as f:
                    for line in f:
                        line = line.strip()
                        if line.endswith(":"):
                            movie_id = line.replace(":", "")
                            review_counter = 0
                        else:
                            if(review_counter < 250):
                                row_data = []
                                row_data = [item for item in line.split(",")]
                                row_data.insert(0, movie_id)
                                row_data.pop()
                                if(int(row_data[2]) >= 4):                                                                                          
                                    w.write(",".join(row_data))
                                    w.write('\n')
                                    review_counter += 1
    else:
        raise FileExistsError('File already exists. Please delete to try again!')

if __name__ == '__main__':
    args = sys.argv
    if(len(args) <= 1):
        error('No Parameters were set. No Function will be executed!')
    else:
        globals()[args[1]]()