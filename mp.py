from multiprocessing import Pool
from os import listdir


def mp(path_to_search):

    for file_name in listdir(path_to_search):

        print(file_name)


if __name__=='__main__':
    
    directory = [['/path/to/search'],['/path/to/search'],['/path/to/search']]

    with Pool() as pool:
        pool.starmap(mp, directory)