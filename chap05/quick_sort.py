data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
	if len(data) <= 1:
		return data

	pivot = data[0] # ピポットとしてリストの先頭を使用
	left, right, same = [], [], 0

	for i in data:
		if i < pivot:
			# ピポットより小さい場合は左に
			left.append(i)
		elif i > pivot:
			# ピポットより大きい場合は右に
			right.append(i)
		else:
			same += 1

	left = quick_sort(left)
	right = quick_sort(right)
	# ソートされたものとピポットの値を合わせて返す
	return left + [pivot] * same + right

print(quick_sort(data))
