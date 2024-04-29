kata1 = input("Kata pertama : ")
kata2 = input("Kata Kedua :")
true = 0
for i in range(len(kata1)):
    if(kata1[i] == kata1[len(kata2)-1-1]):
        true = 1
if (true !=0):
    print("Kalimat anagram")
else:
    print(f"{kata1} dan {kata2} bukan anagram")
