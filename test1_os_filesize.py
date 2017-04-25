import os

all_file=os.listdir(os.curdir)
file_dict=dict()

for each in all_file:
    if os.path.isfile(each):
        each_size=os.path.getsize(each)
        file_dict[each]=each_size

for each in file_dict:
    print("[%s]  [%d B]" % (each,file_dict[each]))

