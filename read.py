# import json module
import json

# enter album number
num = int(input("photo-album "))

# converts file to dictionary
with open('photos.json') as f:
    data = json.load(f)

#checks if album number is in range
if num < 1 and num > 100:
    print("Album ID is out of range")

else:
    k = 0
    # store album id then compare it to values of the dictionary
    while k < len(data):
        aid = int(data[k].get('albumId'))
        if aid == num:
            print("[" + str(data[k].get('id')) + "]" + " " + str(data[k].get('title')))

        k += 1


