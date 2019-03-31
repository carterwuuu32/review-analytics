
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print(len(data))  #統計data清單裡的留言則數有多少
print(data[0])  #印出第一則留言

sum_len = 0  #統計每則留言有多少字數
for d in data:  #for loop 處理每則留言，代號d
	sum_len = sum_len + len(d)  #len(d)計算每則留言的長度，並加總

print(sum_len / len(data))


