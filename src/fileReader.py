import os

# path_ = "/home/amaur1/a1/PAA-trb/src/Test-list/cont-test"

path_ = "/home/amaur1/a1/PAA-trb/src/Test-list/cont"

os.chdir(path_)


def read_text_file(file_path):
    with open(file_path, 'r') as f:

        for cont in f.readlines():
            conts = cont.split()
            nms_int = list(map(int, conts))
            return nms_int


def file_read(name_arquivo):

    for file in os.listdir():
        if file.endswith(".txt"):

            if(file == name_arquivo):

                file_path = f"{path_}/{file}"

                return read_text_file(file_path)
        # print("\n")


# a = file_read("cem.txt")

# print(a)
