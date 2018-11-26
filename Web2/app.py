import mlab 
from resource import Resource  
from movie import Movie
from faker import Faker 

faker = Faker("en_US")
# for _ in range(5):
#     print(faker.name())

mlab.connect()

# ////delete
# m = Movie.objects().with_id("5bf7f9c068a3ff10c0ee9309")
# print(m.title)
# m.delete()

# r = Resource.objects()
# r[0].delete()

# r = Resource.objects().first()
# r.delete()

# ////Read
# movie_list = Movie.objects()

# for m in movie_list:
#     print(m.title)
#     print(m.image)
#     print(m.year)

# resource_list = Resource.objects()

# for r in resource_list:
#     print(r.name, r.city, r.yob, r.height, r.weight, sep = "\n")


# r1 = Resource(name="Huy", city="Ha Noi", yob = 20, height= 175, weight=60)
# r2 = Resource(name="Nam", city="Ha Nam", yob = 24, height= 170, weight=55)
# r3 = Resource(name="Hai", city="Cao Bang", yob = 19, height= 180, weight=70)
# r1.save()
# r2.save()
# r3.save()

# from random import randint

# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150, 200)
#     weight = randint(40, 100)
#     r = Resource(name=name, city=city, yob=yob, height=height, weight=weight)
#     r.save()

# records = Resource.objects(name="William Lloyd")
# for r in records:
#     print(r.city, r.weight, r.height)

# height_s = Resource.objects(height=172)
# for s in height_s:
#     print(s.name, s.city, sep = "\n")

# records = Resource.objects(height__in=range(155, 165))
# print(len(records))

# ////Update
# records = Resource.objects()

# for r in records:
#     r.update(set__available=False)

r = Resource.objects().with_id("5bf80ccb68a3ff22d06ba51f")
r.update(set__available=True)