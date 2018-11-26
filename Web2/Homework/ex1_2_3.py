import mlab 
from res import River 

mlab.connect()

# Ex2

# records = River.objects(continent="Africa")
# for r in records:
#     print(r.name, sep = "\n")

# Ex3

length_s = River.objects(continent="S. America", length__lt=1000)
for l in length_s:
    print(l.name, sep = "\n")
