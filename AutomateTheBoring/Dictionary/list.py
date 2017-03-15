from operator import itemgetter, attrgetter, methodcaller

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(student_tuples)
print(sorted(student_tuples, key=itemgetter(1)))
