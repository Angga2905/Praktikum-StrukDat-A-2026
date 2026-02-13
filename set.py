#buat set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#akses set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#cek set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#add item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#add set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)