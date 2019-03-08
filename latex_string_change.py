import re

def change_str(str_input):
    match = re.findall(r'[{](.*?)[}]', str_input)
    start = 0
    position_left = []
    position_right = []
    while True:
        index = str_input.find('{', start)
        if index == -1:
            break
        position_left.append(index)
        start = index + 1
    start = 0
    while True:
        index = str_input.find('}', start)
        if index == -1:
            break
        position_right.append(index)
        start = index + 1
    str_fix = str_input[position_left[3]+1:position_right[-2]]
    match_1 = match[0]
    match_2 = match[1]
    match_3 = match[2]
    match_4 = str_fix
    match_5 = match[-1]
    print(match_1, match_2, match_3, match_4, match_5)

    line_1 = r"\begin{figure}[%s]" % match_1
    line_2 = r"\centering"
    line_3 = r"\includegraphics[width=%s\textwidth,]{03_Grafiken/%s}" % (match_2, match_3)
    line_4 = r"\caption[]{%s}" % match_4
    line_5 = r"\label{%s}" % match_5
    line_6 = r"\end{figure}"
    print("=====================================")
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)
    print("=====================================")



str_1 = r"\fig{!htbp}{0.7}{Model_ACNN_Training.pdf}{Flow chart for training the \acnn model}{fig:model acnn train:20190208}"


change_str(str_1)