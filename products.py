# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續
		name, price = line.strip().split(',') # strip 清除空格 \n # split 分割 # 直接存入name與price變數中
		products.append([name, price])
print(products)

# 使用者輸入
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

# 印出資料
for p in products:
	print(p[0], '的價格是: ', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # r-讀取  w-寫入 # utf-8編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')