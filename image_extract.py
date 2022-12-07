import sys
import os
import json
from PIL import Image

def main(argv) :   

    object = argv[1]
    jpg_dir_path = './raw/' + str(object) + "_RAW"
    json_dir_path = './raw/VL_' + str(object) + "_0"
    json_files = os.listdir(json_dir_path)

    for i in range(len(json_files)) : 
        f = open(json_dir_path + "/" + json_files[i], 'r', encoding='UTF-8')
        json_data = json.load(f)
        f.close()

        raw_file_name = json_files[i].replace('.json', '')

        annotations = list(json_data["annotations"])
        try :
            for idx, value in enumerate(annotations) : 
                image_raw = {}
                image_raw['id'] = value["category_id"]
                image_raw['bbox'] = value["bbox"]
                min_x, min_y, dis_x, dis_y = image_raw["bbox"][0], image_raw["bbox"][1], image_raw["bbox"][2], image_raw["bbox"][3]
                xy = (min_x, min_y, min_x + dis_x, min_y + dis_y)
                img = Image.open(jpg_dir_path + "/" + raw_file_name + '.jpg')
                crop_img = img.crop(xy)
                crop_img.save('./' + object + '_IMG/' + raw_file_name + '_' + str(idx) + '.jpg')
                # img_txt = open('./' + object + '_IMG/' + raw_file_name + '_' + str(idx) + '.txt', 'w')
                # img_txt.write("category_id : " + str(image_raw['id']) + "\n")
                # img_txt.write('border box\n')
                # for i in range(len(image_raw['bbox'])) :
                #     img_txt.write(str(image_raw['bbox'][i]) + "\n")
                # img_txt.close()
        except Exception as e:
            print(raw_file_name)
            print(e)
            continue


if __name__ == "__main__" :
    main(sys.argv)
    print("End of the program.")