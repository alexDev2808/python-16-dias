
mi_set = {1, 2, 4, 56, 74,("esto", "es", "una", "tuple"), 3, 50, 2, ("otra", "tuple", 2, 2), 5, 3, 5, 2, 23, 59, 24}
print(type(mi_set))
print(mi_set)

s1 = {1,3,5,5}
s2 = {1,3,8,89,2}

s3 = s1.union(s2)
print(s3, type(s3))

s3.add(56)
s3.discard(6)

print(s3)

s3.pop()
s3.pop()
s3.pop()
print(s3)