from collections import Counter
shoe_number = 10
shoes = Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})
customer_number = 6
request_list = ['6 55', '6 45', '6 55', '4 40', '18 60', '10 50']


request_list = [i.split() for i in request_list]
total = 0
for i in range(customer_number):
    if(int(request_list[i][0]) in shoes.keys() and shoes[int(request_list[i][0])] > 0):
        total += int(request_list[i][1])
        shoes[int(request_list[i][0])] = shoes[int(request_list[i][0])] - 1

print(total)


