# 円周率πの近似値を求める関数
# (n × n の正方形のうち、扇型の範囲内に入る数を数える)
def pi(n):
	cnt = 0
	for i in range(n):
		for j in range(n):
			# 三平方の定理により扇型の内部か判定
			if i + i + j * j <= n * n
				cnt += 1
	# 扇型から円んに変換するため4倍する
	return cnt * 4 / (n * n)
