# read file script
# Created by Hang Wu
# Data: 2019.02.14


import os
import xlsxwriter


def read_lines(file_path):
    with open(file_path) as f:
        # counter = 0
        Robot_Coor = []
        output = []
        for line in f:
            # delete the space in the head & end of the line
            line = line.strip()
            # determine wether the line is space or comment
            if not len(line) or line.startswith("#"):
                continue
            if "Actual" in line:
                continue
            # if "EXTAXS" in line:
            #     counter += 1
            # if "EXTAXS" in line and counter > 1:
            #     continue
            if "EXTAXS" in line:
                door_longtitude = line.split(" ")[-1]
                continue
            if "TCP" in line:
                continue

            value = line.split(" ")[-1]
            Robot_Coor.append(value)
            
        output.append(door_longtitude)
        output = output + Robot_Coor

        # for i in output:
        #     print(i)
        return output


def get_file_path(file_dir, ext="txt", keyword="Robot"):
    file_list = []
    for filename in os.listdir(file_dir):
        if filename.endswith(ext) and filename.find(keyword) != -1:
            current_path = os.path.abspath(file_dir)
            file_abs_path = os.path.join(current_path, filename)
            file_list.append(file_abs_path)
    return file_list


if __name__ == "__main__":

    file_path = "C:\\Users\\magic\\Documents\\Messungen\\2019-02-13_14-40-26_Robot_Trafo.txt"
    file_dir = "C:\\Users\\magic\\Documents\\Messungen"
    file_output = "C:\\Users\\magic\\Dropbox\\Masterarbeit\\Messungen.txt"
    xlsx_file = "C:\\Users\\magic\\Dropbox\\Masterarbeit\\Messungen.xlsx"

    workbook = xlsxwriter.Workbook(xlsx_file)
    worksheet = workbook.add_worksheet()

    # out = read_lines(file_path)
    # print(out)

    file_list = get_file_path(file_dir)
    counter = 0
    with open(file_output, "w") as file_out:
        col = 10
        for file_txt in file_list:
            row = 10
            file_name = os.path.split(file_txt)[-1][:-4]
            Door_Robot_Coor = read_lines(file_txt)
            counter += 1
            file_out.write("======================== {} ========================\n".format(counter))
            # file_out.write(file_name+"\n")
            file_out.write("================ {} ================\n".format(file_name))
            file_out.write(file_name + "\n")
            # Excel
            worksheet.write(row, col, file_name)
            for i in Door_Robot_Coor:
                file_out.write(i + "\n")
                # Excel
                worksheet.write(row + 1, col, i)
                row += 1
            col += 1
            file_out.write("========================================================\n")
    workbook.close()
