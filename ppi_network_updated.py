def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def vote1(searchstring):
    confidence = file('confidence.ppi').readlines()
    relations = file('MIPSFirstLevel.anno3').readlines()
    con_list = []
    con_filtered = []
    con_percents = []
    rel_list = []
    votes = [0]*50

    for line in confidence:
        for word in line.split():
            if(word == searchstring):
                con_list.append(line)

    for i in con_list:
        for word in i.split():
            if(not is_number(word) and word !=searchstring):
                con_filtered.append(word)

    for i in con_filtered:
        for line in relations:
            for word in line.split():
                if (word == i):
                    rel_list.append(line)

    index = 0
    val = 0
    for i in rel_list:
        for word in i.split():
            if(is_number(word)):
                votes[int(word)]+=1

    max_votes = max(votes)
    max_index = votes.index(max_votes)
    return max_index


def vote2(searchstring):
    confidence = file('confidence.ppi').readlines()
    relations = file('MIPSFirstLevel.anno3').readlines()
    con_list = []
    con_filtered = []
    con_percents = []
    rel_list = []
    votes_new = [0]*50

    for line in confidence:
        for word in line.split():
            if(word == searchstring):
                con_list.append(line)

    for i in con_list:
        for word in i.split():
            if(word !=searchstring):
                con_percents.append(word)
            if(not is_number(word) and word !=searchstring):
                con_filtered.append(word)

    for i in con_filtered:
        for line in relations:
            for word in line.split():
                if (word == i):
                    rel_list.append(line)

    index = 0
    val = 0
    for i in rel_list:
        for word in i.split():
            if(not is_number(word)):
                index = con_percents.index(word)
                val = con_percents[con_percents.index(word)+1]
            if(is_number(word)):
                votes_new[int(word)]+=float(val)

    max_new_votes = max(votes_new)
    max_new_index = votes_new.index(max_new_votes)
    return max_new_index


def leave_one_out1():
    relations = file('MIPSFirstLevel.anno3').readlines()
    total = 0
    correct = 0
    for line in relations:
        for word in line.split():
            if(not is_number(word)): 
                tag = vote1(word)
                total+=1
            if(is_number(word)):
                if(int(word) == int(tag)):
                    correct+=1
    print "total: ", total
    print "correct: ", correct
    print "frac: ", float(correct)/total*100

def leave_one_out2():
    relations = file('MIPSFirstLevel.anno3').readlines()
    total = 0
    correct = 0
    for line in relations:
        for word in line.split():
            if(not is_number(word)): 
                tag = vote2(word)
                total+=1
            if(is_number(word)):
                if(int(word) == int(tag)):
                    correct+=1
    print "total: ", total
    print "correct: ", correct
    print "frac: ", float(correct)/total*100

leave_one_out1()
leave_one_out2()

