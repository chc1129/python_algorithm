data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
	if len(data) <= 1:
		return data

	pivot = data[0] # ピポットとしてリストの先頭を使用
	# ピポットより小さいものでリストを作る
	left = [i for i in data[1:] if i <= pivot]
	# ピポットより大きいものでリストを作る
	right = [i for i in data[1:] if i > pivot]

	left = quick_sort(left)
	right = quick_sort(right)
	# ソートされたものとピポットの値を合わせて返す
	return left + [pivot] + right

print(quick_sort(data))
