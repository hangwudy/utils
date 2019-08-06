import pandas as pd
import xlrd
import shutil
import os

def Excel_read_pandas(xls_path, sheet_name="Sheet1"):

    data_frame = pd.read_excel(xls_path, sheet_name=sheet_name)
    print(data_frame)


def Excel_read_xlrd(xls_path, row_num, col_num):
    workbook = xlrd.open_workbook(xls_path)
    worksheet = workbook.sheets()[0]
    file_name = worksheet.cell(row_num,col_num).value

    # print(file_name)
    return file_name

def loadim(image_path = 'images', ext='png', keyword='car_door'):
    image_list = []
    for filename in os.listdir(image_path):
        if filename.endswith(ext) and filename.find(keyword) != -1:
            current_path = os.path.abspath(image_path)
            image_abs_path = os.path.join(current_path,filename)
            image_list.append(image_abs_path)
    return image_list


def copy_and_rename(xls_path, original_path, destination_path):
    # Intial row number
    row = 8
    for group in range(1,6):
        longitude = -30
        # Intial col number
        col = 4
        for number in range(1,14):

            # Text files
            file_name_keyword = Excel_read_xlrd(xls_path, row, col)
            file_name = file_name_keyword+".txt"
            txt_file_path = os.path.join(original_path, file_name)

            # images
            image_name_keyword = file_name_keyword
            image_path = loadim(original_path, "png", image_name_keyword)[0]

            if longitude < 0:
                file_name_new = "{}_{}_{}.txt".format(group, number, longitude+360)
                image_path_new = "{}_{}_{}.png".format(group, number, longitude+360)
            else:
                file_name_new = "{}_{}_{}.txt".format(group, number, longitude)
                image_path_new = "{}_{}_{}.png".format(group, number, longitude)
            
            txt_file_dest_path = os.path.join(destination_path, file_name_new)
            image_dest_path = os.path.join(destination_path, image_path_new)
            shutil.copy2(txt_file_path, txt_file_dest_path)
            shutil.copy2(image_path, image_dest_path)

            # print(image_path)
            # print(image_dest_path)
            # print(txt_file_path)
            # print(txt_file_dest_path)

            # Update numbers
            longitude += 5
            col += 1
            
        # Update numbers
        row += 16
            



    return None

if __name__ == "__main__":
    xls_path = "C:\\Users\\magic\\Dropbox\\utils\\Messungen.xlsx"
    orig_path = "C:\\Users\\magic\\Documents\\Messungen"
    dest_path = "C:\\Users\\magic\\Documents\\Messungen_sortiert"

    # Excel_read_xlrd(xls_path, 8, 4)
    copy_and_rename(xls_path, orig_path, dest_path)
