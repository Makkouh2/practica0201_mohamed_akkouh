x=(input("Escriba precio del producto en euros con dos decimales"))
print(x[:x.find(".")],"euros") 
print(x[x.find(".")+1:],"centimos")

