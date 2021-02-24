data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Read Completed, There are total: ', len(data), 'data')

sun_len = 0
for d in data:
	sun_len += len(d)

print(sun_len/len(data))