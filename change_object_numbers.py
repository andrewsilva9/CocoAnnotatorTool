import os

# Move this file above the labels directory and run it
old_object_ids = [0, 39, 41, 45, 62, 63, 67, 73]
new_object_ids = [0, 1, 2, 3, 4, 5, 6, 7]
for iter_file in os.listdir(os.path.join(os.getcwd(), 'labels')):
    print iter_file
    contents = []
    if iter_file.startswith('.'):
        continue
    for line in open(os.path.join(os.getcwd(), 'labels', iter_file), 'r'):
        object_num = int(line.split(' ')[0])
        left = float(line.split(' ')[1])
        top = float(line.split(' ')[2])
        w = float(line.split(' ')[3])
        h = float(line.split(' ')[4])
        new_object_num = new_object_ids[old_object_ids.index(object_num)]
        contents.append([new_object_num, left, top, w, h])
    new_file = open(os.path.join(os.getcwd(), 'labels', iter_file), 'w')
    for line in contents:
        new_file.write('{:d} {:f} {:f} {:f} {:f} \n'.format(line[0], line[1], line[2], line[3], line[4]))
    #
    #
