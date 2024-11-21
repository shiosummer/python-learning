def all():
   x=0
   for i in range(101):
      if i%2 == 0:
          x += i
   return x
print(all())