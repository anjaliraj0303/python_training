#testing
import array as arr

intArray = arr.array('i',[11,12,13,14,15,15,16])
print(f"Array before inserting the element: {intArray}")
intArray.insert(3,10)
print(f"Array after inserting the element: {intArray}")
print(f"Count of 15 in array: {intArray.count(15)}")
intArray.reverse()
print(f"Array after reversing: {intArray}")

print(intArray[0])
print(intArray[1])