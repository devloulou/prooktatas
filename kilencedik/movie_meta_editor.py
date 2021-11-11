import os
from utils import file_handler

# a statisztikát tároljuk le egy json file-ba
# minimális statisztika:
# legnagyobb bevétel
# legjobb értékelés
# legtöbb szereplő
# legnagyobb budget
# leghosszabb film

# json_data['details']['revenue'] -> ez az érték lesz az, amire szükségem van

def get_json_for_loop(folder_location):
    ret_val = []
    for json_file in os.listdir(folder_location):
        # if '.json' in json_file:
        #     ret_val.append(json_file)
        if json_file.endswith('.json'):
            ret_val.append(os.path.join(folder_location, json_file))
    return ret_val


def get_json_list(folder_location):
    return [os.path.join(folder_location, json_file) for json_file in os.listdir(folder_location)\
                if json_file.endswith('.json')]

# legnagyobb bevétel
def max_revenue(folder_location):
    # lekérni a jsonöket tartalmazó listát
    file_list = get_json_list(folder_location)
    
    # a file-ok megnyitása
    max_value = 0
    for json_file in file_list:
        data = file_handler.open_json(json_file)
        # json_data['details']['revenue'] -> ez az érték lesz az, amire szükségem van
        # max_value = data['details']['revenue']
        # print(data.get('details').get('original_title'))
        # print(data.get('details').get('revenue'))
        # print()
        if max_value < data.get('details').get('revenue'):
            max_value = data.get('details').get('revenue')

    return max_value

# legjobb értékelés
def best_imdb_score(folder_location):
    file_list = get_json_list(folder_location)

    max_value = 0
    for json_file in file_list:
        data = file_handler.open_json(json_file)
        # print(data.get('details').get('original_title'))
        # print(data.get('details').get('vote_average'))
        # print()
        #lekérni a megfelelő kulcshoz tartozó értéket: kulcs : vote_average
        if max_value < data.get('details').get('vote_average'):
            max_value = data.get('details').get('vote_average')
    
    return max_value


# legtöbb szereplő: json_file['cast']['crew'] -> ez egy lista -> len(json_file['cast']['crew'])
# mérőszámok -

# megnyitjuk a file-okat
# megfelelő kulcsok mentén lekérjük az adatokat
# és letéroljuk az adatok valamilyen adatstruktúrába
# írjuk ki a statisztika eredményét egy movie_statistic nevű file-ba 
def movie_statistics(folder_location):
    file_list = get_json_list(folder_location)

    max_revenue = 0
    best_score = 0
    cnt_actors = 0
    biggest_budget = 0
    longest_runtime = 0

    max_rev_movie = None
    best_score_movie = None
    cnt_actors_movie = None
    biggest_budget_movie = None
    longest_runtime_movie = None

    for json_file in file_list:
        data = file_handler.open_json(json_file)

        if max_revenue < data.get('details').get('revenue'):
            max_revenue = data.get('details').get('revenue')
            max_rev_movie = data.get('details').get('original_title')
        
        if best_score < data.get('details').get('vote_average'):
            best_score = data.get('details').get('vote_average')
            best_score_movie = data.get('details').get('original_title')

        # if cnt_actors < len(data.get('cast').get('crew')):
        #     cnt_actors = len(data.get('cast').get('crew'))

        # temp_list = len(list(set([item['cast_id'] for item in data.get('cast').get('crew')])))
        # temp_list = len(set([item['cast_id'] for item in data.get('cast').get('crew')]))

        if cnt_actors < len(set([item['cast_id'] for item in data.get('credits').get('cast')])):
            cnt_actors = len(set([item['cast_id'] for item in data.get('credits').get('cast')]))
            cnt_actors_movie = data.get('details').get('original_title')

        if biggest_budget < data.get('details').get('budget'):
            biggest_budget = data.get('details').get('budget')
            biggest_budget_movie = data.get('details').get('original_title')
        
        if longest_runtime < data.get('details').get('runtime'):
            longest_runtime = data.get('details').get('runtime')
            longest_runtime_movie = data.get('details').get('original_title')

    return {
        'max_revenue': {'value': max_revenue, 'title': max_rev_movie},
        'best_score': {'value': best_score, 'title': best_score_movie},
        'cnt_actors': {'value': cnt_actors, 'title': cnt_actors_movie},
        'biggest_budget': {'value': biggest_budget, 'title': biggest_budget_movie},
        'longest_runtime': {'value': longest_runtime, 'title': longest_runtime_movie}
    }
    

def movie_statistics_2(folder_location):
    file_list = get_json_list(folder_location)

    statistics = {
            'max_revenue': {'value': 0, 'title': None},
            'best_score': {'value': 0, 'title': None},
            'cnt_actors': {'value': 0, 'title': None},
            'biggest_budget': {'value': 0, 'title': None},
            'longest_runtime': {'value': 0, 'title': None}
            }

    for json_file in file_list:
        data = file_handler.open_json(json_file)

        if statistics['max_revenue']['value'] < data.get('details').get('revenue'):
            statistics['max_revenue']['value'] = data.get('details').get('revenue')
            statistics['max_revenue']['title'] = data.get('details').get('original_title')
        
        if statistics['best_score']['value']  < data.get('details').get('vote_average'):
            statistics['best_score']['value']  = data.get('details').get('vote_average')       
            statistics['best_score']['title'] = data.get('details').get('original_title')     

        if statistics['cnt_actors']['value']  < len(set([item['cast_id'] for item in data.get('credits').get('cast')])):
            statistics['cnt_actors']['value'] = len(set([item['cast_id'] for item in data.get('credits').get('cast')]))
            statistics['cnt_actors']['title'] = data.get('details').get('original_title')

        if statistics['biggest_budget']['value']  < data.get('details').get('budget'):
            statistics['biggest_budget']['value']  = data.get('details').get('budget')
            statistics['biggest_budget']['title'] = data.get('details').get('original_title')
        
        if statistics['longest_runtime']['value']  < data.get('details').get('runtime'):
            statistics['longest_runtime']['value']   = data.get('details').get('runtime')
            statistics['longest_runtime']['title'] = data.get('details').get('original_title')

    return statistics



def create_statistic(folder_location, file_path):
    # legenráljuk a statiszkákat
    # a package-el kiírjuk
    data = movie_statistics_2(folder_location)
    return file_handler.write_json(file_path, data)


################################################

# a meta adatból töröljük a crew-ra vonatkozó részeket
## a videos részből állítsunk elő youtbe embeded linkeket és csak a linket hagyjuk meg a fileban
# töröljük a belongs to collection-t
# töröljük a production_companies részt
# a bevételt alakítsuk át úgy, hogy állítsuk be a dollárt valutának


def delete_json_part(folder_location):
    file_list = get_json_list(folder_location)
    
    for json_file in file_list:
        data = file_handler.open_json(json_file)

        if data.get('credits').get('crew'):
            data.get('credits').pop('crew')

        if data.get('details').get('belongs_to_collection'):
            data.get('details').pop('belongs_to_collection')

        if data.get('details').get('production_companies'):
            data.get('details').pop('production_companies')

        if not isinstance(data.get('details').get('revenue'), dict):
            if data.get('details').get('revenue'):
               data['details']['revenue'] = {'value': data['details']['revenue'],\
                'currency': '$', 'currency_in_str': 'dollar'}
        #print(data.get('credits').keys())

        file_handler.write_json(json_file, data)

    return True
    
######################################################







if __name__ == '__main__':
    folder_path = r"C:\WORK\Prooktatás\1. lesson\kilencedik\movie_meta"
    #file_list = get_json_for_loop(folder_path)
    #print(folder_path)
    # file_list_2 = get_json_list(folder_path)

    # print(file_list_2)

    #max_value = max_revenue(folder_path)

    #print(max_value)

    #best_score = best_imdb_score(folder_path)

    #print(f"best_score : {best_score}")

    # statistic = movie_statistics(folder_path)

    # print(statistic)

    # statistics2 = movie_statistics_2(folder_path)

    # print(statistics2)


    #create_statistic(folder_path, 'statistics.json')

    delete_json_part(folder_path)