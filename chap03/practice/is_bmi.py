# 身長と体重からBMI(肥満度を示す体格指数)を求める関数
def bmi(height, wight):
	# 身長(cm)の単位をmに変換
	h = height / 100
	return wight / (h * h)
