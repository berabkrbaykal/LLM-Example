def word_count(str, sen):
    a = input("Enter a sentence: ")
    a = a.upper()

    count = 0
    sen = a.split(" ")

for i in range(len(sen)):
        if sen[0] == sen[i]:
            count = count + 1

print(f"{sen[i].lower()} kelimesinin tekrar sayısı = {count}")

count2 = 0

for j in range(len(sen)):
    if sen[j+1] == sen[j+1]:
        count2 = count2 + 1

print(f"{sen[j+1].lower()} kelimesinin tekrar sayısı = {count2}")