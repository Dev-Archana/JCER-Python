'''1.Shopping bill printing
 a.Product_id
 b.Product_price
 c.GST'''

product_id1=int(input("Enter Product id :"))
product_price1=float(input("Enter Product price :"))

product_id2=int(input("Enter Product id :"))
product_price2=float(input("Enter Product price :"))

product_id3=int(input("Enter Product id :"))
product_price3=float(input("Enter Product price :"))
GST=18/100
total=product_price1+product_price2+product_price3+GST

print("Product 1 details\n")
print("Product_id",product_id1)
print("Product_price",product_price1)
print("Product 2 details\n ")
print("Product_id",product_id2)
print("Product_price",product_price2)
print("Product 3 details \n")
print("Product_id",product_id3)
print("Product_price",product_price3)
print("GST :",GST)
print("total :",total)

