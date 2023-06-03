import graphviz
import random

cfn = 'color_list.txt'
def color_data(filename):
    color_dict = dict()
    color_list = list()
    with open(filename, 'r') as f:
        for line in f:
            if 'colors' in line:
                color = line
                color_list = list()
                color_dict[color] = color_list
                continue
            str = line.split('	')[0]
            color_list.append(str)
    print(color_dict.items())
    return color_dict


cd = color_data(cfn)

def random_color():
    color_list = list()
    for key, value in cd.items():
        if key == "Pink colors\n":
            color_list.extend(value[2:])
        if key == "Red colors\n":
            color_list.extend(value[-2:])
        if key == "Orange colors\n":
            color_list.extend(value[-3:])
        if key == "Green color\n":
            color_list.extend(value[7:])
        if key == "Cyan colors\n":
            color_list.extend(value[8:])
        if key == "Yellow colors\n":
            color_list.extend(value[2:-2])
        if key == "Brown color\n":
            color_list.extend(value[-3:])
        if key == "Purple, violet, and magenta colors\n":
            color_list.extend(value[9:])
        if key == "Blue colors\n":
            color_list.extend(value[7:])
        if key == "White colors\n":
            color_list.extend(value[0:4])
        if key == "Gray and black colors\n":
            color_list.extend(value[3:])

    c1 = random.choice(color_list)
    c2 = random.choice(color_list)

    return c1 + ":" + c2


beginning = {
    'c' : 'begin',
    'n' : [
        'There are two kinds of people in this life:',
        'Those who walk into a room and say',
        'Well, here I am!',
        'And those who walk in and say,',
        'Ahh, there you are.'
    ]
}

data_struct = {
    'g': 'how to talk to anyone 92 little tricks',
    'sub': [
beginning
     ]

}

def alignment_questions_arr(arr):
    rst_arr = list()
    max_len = max(arr, key=len)
    print(len(max_len))
    for item in arr:
        rst_arr.append((len(max_len) - len(item)))
    return rst_arr

def get_node_label(node_name,arr):
    rst_arr_len= alignment_questions_arr(arr)
    label_str = '{'
    # '{<f0> Data|<f1> Next}'
    for rank, (item, item_len) in enumerate(zip(arr, rst_arr_len), 0):
        print(len(item))
        label_str += f'<f{rank}> {item}'
        label_str += '_' * item_len
        if rank != len(arr) - 1:
            label_str += '|'
        else:
            label_str += '}'
    return label_str



def sub_diagram(label_ds, graph, sub_name):

    with graph.subgraph(name=sub_name) as c:
        c.attr(rankdir='TB')
        c.attr(fontname='Comic Sans MS')
        c.attr(fillcolor=random_color(), label=label_ds['c'], fontcolor='black',
               style='filled', gradientangle='100',rankdir='TB')

        if 'n' in label_ds:
            lstr = get_node_label(label_ds['c'], label_ds['n'])

            c.node(label_ds['c'], shape='record',
                    label= lstr, fontname='Monaco', fontcolor='black')

        if 'sub' in label_ds:
            count = 0
            for sub_ds in label_ds['sub']:
                # print(f'{count} : {sub_ds}')
                sub_diagram(sub_ds, c, 'Cluster' + str(count))
                count += 1

def diagram(label_ds, file_name):
    g = graphviz.Graph('G', filename= file_name)
    g.attr(fontname='Comic Sans MS')
    g.attr(bgcolor=random_color(), label=label_ds['g'], fontcolor='black', style='filled',rankdir='TB')


    if 'sub' in label_ds:
        count = 0
        for sub_ds in label_ds['sub']:
            # print(f'{count} : {sub_ds.items()}')
            # print(sub_ds)
            sub_diagram(sub_ds, g, 'Cluster'+ str(count))
            count += 1

    g.view()

diagram(data_struct, 'g_c_n.gv')