products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	## p = []
	## p.append(name)
	## p.append(price)
	# p = [name, price]
	# products.append(p)
	products.append([name, price])
print(products) # [[紅茶, 10], [奶茶, 15]]

for p in products:
	print(p[0], '的價格是: ', p[1])