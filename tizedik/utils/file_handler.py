import os
import json

def read_txt(file_path):
    data = None
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file_object:
            data = file_object.read()
    else:
        return False
    return data


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

if __name__ == '__main__':
    write_json("tizedik_test_feladat.json", {"test": "test"})