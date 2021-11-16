import os
import math
from utils.file_handler import read_txt, write_json, delete_file
from collections import Counter

# Plusz feladat: a Counter használatával -> ezt nem tanultuk, de egy kis googlizás után meglátjátok, hogy mennyire egyszerű
# az 5 leggyakrabban előforduló szót is keressétek meg

# 1. Szavak száma: minden 2-nél hosszabb karaktert szónak tekintek. 
# (Mivel angol az I, an, a is stb kifejezések nem érdekelnek)
# 2. Sorok száma
# 3. Oldalak száma: egy oldal kb. 3000 karakter
# 4. A könyv szerzőjét: a file-okban az Author: utáni rész (nem néztem meg, hogy minden egyes file-ban szerepel)
# 5. A könyv megjelenési dátuma: Release Date: utáni rész (nem néztem meg, hogy minden file-ban )

# Leghosszabb könyv
# Legrövidebb könyv
# Legrégebben kiadott könyv (dátumhasználatot nem tanultunk, így tökéletes megoldás, ha a megjelenés évét számként kezelitek)
# Legújabb könyv (dátumhasználatot nem tanultunk, így tökéletes megoldás, ha a megjelenés évét számként kezelitek)

# Töröljétek a legújabb könyvet, és a hozzá tartozó statisztikát is!

def create_statistic(folder_path):    
    # szükségem van a txt ket tartalmazó listára - elérési úttal
    book_list = [os.path.join(folder_path, book) for book in os.listdir(folder_path) if '.txt' in book]
    
    # egyenként meg kell nyitni a file-okat, hogy meg tudjuk vizsgálni a tartalmát

    book_statistic = {
        "words": 0,
        "lines": 0,
        "page_num": 0,
        "author": None,
        "release_date": 0,
        "most_common": None,
    }

    most_stats = {
        "longest_book": {"page_num": 0, "book": None},
        "shortest_book": {"page_num": 0, "book": None},
        "oldest_book": {"release": 0, "book": None},
        "youngest_book": {"release": 0, "book": None, "path": None},
    }

    for book in book_list:
        data = read_txt(book)
        print(book)
        # 1. Szavak száma: minden 2-nél hosszabb karaktert szónak tekintek. 
        
        # temp_list = []
        # for word in data.split():
        #     if len(word) > 2:
        #         temp_list.append(word)

        book_statistic["words"] = len([word for word in data.split() if len(word) > 2])
        #  2. Sorok száma        
        book_statistic["lines"] = len(data.splitlines())
        # # 3. Oldalak száma: egy oldal kb. 3000 karakter
        book_statistic["page_num"] = math.ceil(len(data)/3000)
        
        # 4. A könyv szerzőjét: a file-okban az Author:
        # utáni rész (nem néztem meg, hogy minden egyes file-ban szerepel)       
        # 5. A könyv megjelenési dátuma: Release Date: utáni rész (nem néztem meg, hogy minden file-ban )        
        for line in data[:3000].splitlines():
            if "Author:" in line:
                 book_statistic["author"]  = line.replace("Author: ", "")
            if "Release Date:" in line:
                book_statistic["release_date"] = line.replace("Release Date:", "")

        book_statistic['most_common'] = Counter([word for word in data.split() if len(word) > 2]).most_common(5)
        
        # overall statistics
        if most_stats['longest_book']["page_num"] < book_statistic['page_num']:
            most_stats['longest_book']["page_num"] = book_statistic['page_num']
            most_stats['longest_book']['book'] = book.split("\\")[-1][:-4]
        
        if most_stats['shortest_book']["page_num"] > book_statistic['page_num'] or most_stats['shortest_book']["page_num"] == 0:
            most_stats['shortest_book']["page_num"] = book_statistic['page_num']
            most_stats['shortest_book']['book'] = book.split("\\")[-1][:-4]

        if book_statistic['release_date']:
            if most_stats["oldest_book"]["release"] > int([datum for datum in book_statistic['release_date'].split() if len(datum) == 4 and datum.isdigit()][0])\
                or most_stats["oldest_book"]["release"] == 0:
                most_stats["oldest_book"]["release"] = \
                    int([datum for datum in book_statistic['release_date'].split() if len(datum) == 4 and datum.isdigit()][0])
                most_stats['oldest_book']['book'] = book.split("\\")[-1][:-4]

            if most_stats["youngest_book"]["release"] < int([datum for datum in book_statistic['release_date'].split() if len(datum) == 4 and datum.isdigit()][0])\
                or most_stats["youngest_book"]["release"] == 0:
                most_stats["youngest_book"]["release"] = \
                    int([datum for datum in book_statistic['release_date'].split() if len(datum) == 4 and datum.isdigit()][0])
                most_stats['youngest_book']['book'] = book.split("\\")[-1][:-4]
                most_stats['youngest_book']['path'] = book

        write_json(book.replace(".txt", ".json"), book_statistic)
    write_json("overall_statistic.json", most_stats)

    delete_file(most_stats['youngest_book']['path'])
    delete_file(most_stats['youngest_book']['path'].replace(".txt", ".json"))

if __name__ == '__main__':
    folder_path = r"C:\WORK\Prooktatás\1. lesson\prooktatas\tizedik\books"

    create_statistic(folder_path)