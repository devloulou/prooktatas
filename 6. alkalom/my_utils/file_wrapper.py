import os

def read_txt(file_loc):
    data = None
    try:
        with open(file_loc, 'r', encoding="utf-8") as f:
            data = f.read()
    except Exception as e:
        return False, str(e)

    return data    

def write_to_txt(file_loc, message):
    try:
        with open(file_loc, "a", encoding='utf-8') as f:
            #f.writelines(message)
            if isinstance(message, str):
                f.write(message)            
            elif isinstance(message, (list, tuple)):
                for item in message:
                    f.write(f"{item}\n")
                    # print(os.path.getsize(file_loc))
            elif isinstance(message, dict):
                for key, value in message.items():
                    f.write(f"{key} - {value}\n")
            else:
                raise Exception(f"Nem iterálható típust adtál meg: {type(message)}")

    except Exception as e:
        return False, str(e)
    
    return True

def delete_file(file_loc):
    if os.path.exists(file_loc):
        try:
            os.remove(file_loc)
        except Exception as e:
            return False, str(e)
    else:
        return False, "Nem létezik a megadott file"
    
    return True

def remove_line_in_txt(file_loc, line_num):
    try:
        with open(file_loc, 'r+', encoding="utf-8") as f:
            file = f.readlines()
            f.seek(0)
            for idx, item in enumerate(file):
                if idx != line_num - 1:
                    f.write(item)
    except Exception as e:
        return False, str(e)

    return True

# write_to_txt
def remove_line_in_txt_2(file_loc, line_num):
    file = None
    try:
        with open(file_loc, 'r+', encoding="utf-8") as f:
            file = f.readlines()            
            file.pop(line_num - 1)
            f.truncate(0)
        write_to_txt(file_loc, file)                
    except Exception as e:
        return False, str(e)

    return True 

if __name__ == '__main__':
    file_loc = "C:\WORK\Prooktatás/1. lesson/teszt_allomany.txt"
    #file_loc = "C:\WORK\Prooktatás/1. lesson/teszt_allomay.txt"
    data = read_txt(file_loc)
    print(type(data))
    #print(data)
    message = ("Alma", "Körte", "Dió", "Cseresznye")
    message = "Megszentségteleníthetelenségeskedéseitekért"
    message = print
    message = "Menj haza magadnak"
    message = ["Alma", "Körte", "Dió", "Cseresznye"]
    ret_val = write_to_txt('write_test_file.txt',message)

    #print(ret_val)

    #ret_val = delete_file('almafa.txt')
    ret_val = delete_file(file_loc)

    print(ret_val)

    #ret_val = remove_line_in_txt("C:\WORK\Prooktatás/1. lesson\write_test_file.txt", 3)

    #print(ret_val)

    ret_val = remove_line_in_txt_2("C:\WORK\Prooktatás/1. lesson\write_test_file.txt", 3)

    print(ret_val)