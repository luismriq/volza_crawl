from stores.santa_isabel_cl import fetch_product_data

print("Ejecutando script principal")

url = 'URL_DEL_PRODUCTO_EN_SANTA_ISABEL'
product_data = fetch_product_data(url)
if product_data:
    print(product_data)