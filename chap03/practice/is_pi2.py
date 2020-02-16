# 円周率πの近似値を求める関数
# (πは4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... という式で求められる)
def pi(n):
	result = 4
	plus_minus = -1
	for i in range(1, n):
		result += plus_minus * 4 / (i * 2 - 1)
		# 符号を反転する
		plus_minus *= -1

	return result
