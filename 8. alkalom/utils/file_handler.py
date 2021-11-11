import json
import os

# megnyitni egy json file-t és olvasni
def open_json(file_path):
    data = None
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        return False
    return data

# kiír egy file-t: w - feltételezzük, hogy van root jog - minden file műveletet el tudunk végezni.
# Oprendszer függő

def write_json(file_path, data):
    if data:
        # a data-t át tudjuk e alakítani json-é           
        try: 
            json.dumps(dict(data))
        except TypeError:
            return False, 'Nem jó adattípust adtál meg.'
        except Exception as e:
            return False, str(e)

        if isinstance(file_path, str):        
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file)
        else:
            return False, 'Nem string'
    else:
        return False, 'Nem adtál meg adatokat a kiíráshoz'

    return True


# törölni file-t
def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:        
        return False, 'File nem található!'
    except Exception as e:
        return False, str(e)

    return True

# megadott dolgot töröl a file-ból
def delete_from_json(file_path, data):
    pass


if __name__ == '__main__':
    test_file = r"C:\WORK\Prooktatás\1. lesson\prooktatas\8. alkalom\movie_meta\A Nightmare on Elm Street.json"
    opened_file = open_json(test_file)

    #writed_file = write_json('test_json_ricsi.json',{'alma': None,})

    #print(writed_file)

    #print(type(str(print)))

    deleted = delete_file('alma.txt')
    print(deleted)