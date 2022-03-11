import random
import time

names = ['Ganesh', 'Priyanka', 'Ankita', 'Amol', 'Pinkita']
majors = ['Maths', 'physics', 'Chemistry', 'Biology', 'English']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.clock()
people = people_list(1000000) # 1 Million
t2 = time.clock()

print "Iterator Took {} Seconds".format(t2-t1)

t1 = time.clock()
people = people_generator(1000000) # 1 Million
t2 = time.clock()
print "Generator Took {} Seconds".format(t2-t1)