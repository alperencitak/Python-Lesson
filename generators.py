
numbers = (x for x in range(10))
# for i in numbers:
#     print(i)

def generate_generator():
    for i in range(10):
        yield i # return generator

numbers2 = generate_generator()
for i in numbers2:
    print(i)
print(type(numbers2))