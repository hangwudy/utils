import json

def json_reader(json_file = "history_mobilenet.json"):

    jf = open(json_file)

    history = json.load(jf)
    jf.close()

    print(history.keys())
    # print(history['val_loss'])
    for key in history.keys():
        save_name = "{}.csv".format(key)
        data = []
        for i, val in enumerate(history[key]):

            # print(i+1,',', val, sep='')
            line = "{},{}".format(i,val)
            data.append(line+"\n")
        with open(save_name, "w") as outfile:
            outfile.writelines(data)



json_reader()


