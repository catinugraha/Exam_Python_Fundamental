# # JAWABAN UJIAN 1 -- NO. 1 # #
def hashtag(string):
    splt = string.split()
    hasil = []
    kalimatbaru = ''
    result = False
    for i in splt:
        hasil.append(i.capitalize())
    for j in hasil:
        kalimatbaru += j
    if len(kalimatbaru) > 140:
        print(result)
    elif len(kalimatbaru) == 0:
        print(result)
    else:
        print('#{}'.format(kalimatbaru))

hashtag("Hello there how are you doing")
hashtag("   Hello  World   ")
hashtag("")


# # JAWABAN UJIAN 1 -- NO. 2 # #
def create_phone_number(number):
    x = number[:3]
    depan = ''
    for i in x:
        depan += str(i)
    y = number[3:6]
    tengah = ''
    for j in y:
        tengah += str(j)
    z = number[6:]
    belakang = ''
    for k in z:
        belakang += str(k)
    print('"({}) {}-{}"'.format(depan,tengah,belakang))
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# # JAWABAN UJIAN 1 -- NO. 3 # #
def sort_odd_even(number):
    odd_numbers = []
    even_numbers = []
    hasil = []
    for i in number:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    even_numbers.sort(reverse=True) #Even number descending
    odd_numbers.sort() # Odd number ascending
    hasil.insert(0,odd_numbers[0]) #1
    hasil.insert(1,odd_numbers[1]) #3
    hasil.insert(3,even_numbers[0]) #8
    hasil.insert(4,even_numbers[1]) #4
    hasil.insert(5,odd_numbers[2]) #5
    hasil.insert(6,even_numbers[2]) #2
    print(hasil)

sort_odd_even([5,3,2,8,1,4])
sort_odd_even([1,2,3,4,5,6])


# # JAWABAN UJIAN 1 -- NO. 4 # #
def hollowtriangle(n):
    for row in range(1, n+1):
        for col in range(1, 2*n):
            if row == n or row+col==n+1 or col-row==n-1:
                print('#',end="")
            else:
                print(end='_')
        print()

hollowtriangle(1)
hollowtriangle(2)
hollowtriangle(3)
hollowtriangle(4)
hollowtriangle(5)
hollowtriangle(6)