print("Hesap Makinesine hoşgeldiniz.")

def calc(a,b,ops):

	if ops not in "+,-,/,*":
		print("Hatalı işlem bilgisi!!")



	if ops == "+":
		return(str(a) + "" + ops + str(b) + "" + "=" + str(a+b))

	if ops == "-":
		return(str(a) + "" + ops + str(b) + "" + "=" + str(a-b))

	if ops == "/":
		return(str(a) + "" + ops + str(b) + "" + "=" + str(a/b))

	if ops == "*":
		return(str(a) + "" + ops + str(b) + "" + "=" + str(a*b))

while True:

	a = float(input("İlk sayıyı giriniz: "))
	b = float(input("İkinci sayıyı giriniz: "))
	ops = input("İşlem bilgisini giriniz: ")
	print(calc(a,b,ops))