import sys
import os

def main(argv) :   

    jpg_dir_path = './' + str(argv[1]) + "_RAW"
    json_dir_path = './VL_' + str(argv[1]) + "_0"
    jpg_files = os.listdir(jpg_dir_path)
    json_files = os.listdir(json_dir_path)

    for json_file in json_files : 
        jpg_file = json_file.replace(".json", ".jpg")
        if jpg_file not in jpg_files :
            remove_json = json_dir_path + "/" + json_file
            os.remove(remove_json)

    jpg_files = os.listdir(jpg_dir_path)
    json_files = os.listdir(json_dir_path)

if __name__ == "__main__" :
    main(sys.argv)