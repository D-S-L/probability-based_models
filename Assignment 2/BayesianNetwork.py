import numpy as np

def parse(data_add, child, parents,matrix):
    with open(data_add) as f:
        cur_l= f.readline()
        if not cur_l:
            return
        else:
            cur_l =  cur_l.split('\t')

            if cur_l[0]=='sample-id':
                cur_l = f.readline()           # skip the header

            s_matrix = np.zeros((matrix.shape[1],matrix.shape[2]))

            while cur_l:
                cur_l =  cur_l.split('\t')

                par = (int(cur_l[parents[0]])-1,int(cur_l[parents[1]])-1)
                chi = int(cur_l[child])-1
                matrix[chi][par[0]][par[1]]+=1

                cur_l = f.readline()

            for i in range(matrix.shape[0]):
                s_matrix +=matrix[i]
            # print(s_matrix)
            # print('---````-----')
            # print(matrix/s_matrix)
        return matrix/s_matrix



def get_p_b_cd():
    dic = {'a':1,'b':2,'c':3, 'd':4,'e':5}
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2),dtype = np.int)

    p_b_cd = parse(data_add,dic['b'],[dic['c'],dic['d']],p_b_cd)

    return p_b_cd

def get_p_a_be():
    # you need to implement this method.
    dic = {'a':1,'b':2,'c':3, 'd':4,'e':5}
    p_a_be = np.zeros((2,3,2),dtype = np.int)
    p_a_be = parse(data_add, dic['a'], [dic['b'], dic['e']], p_a_be)

    return p_a_be


# following lines are main function:
data_add = "data//assign2_BNdata.txt"

# probability distribution of b.
p_b_cd=get_p_b_cd()
for c in range(3):
    for d in range(2):
        for b in range(3):
            print("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]))


# probability distribution of a.
p_a_be=get_p_a_be()
for b in range(3):
    for e in range(2):
        for a in range(2):
            print("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]))

