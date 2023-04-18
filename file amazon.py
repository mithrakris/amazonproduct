def product():
    customer_one_mani=int(input("enter the amount purchased by mani"))
    customer_two_logendran=int(input("enter the amount purchased by logendran"))            
    customer_three_satheesh=int(input("enter the amount purchased by satheesh"))
    total=customer_one_mani+customer_three_satheesh+customer_two_logendran
    print(total)

    productlist=open("amazon.txt","a")
    productlist.write(str(customer_one_mani)+"|")
    productlist.write(str(customer_two_logendran)+"|")
    productlist.write(str(customer_three_satheesh)+"|")
    productlist.write(str(total))
    productlist.write("\n")
    productlist.close()
def amzproduct():
    readproductlist=open("amazon.txt","r")
    product=readproductlist.read()
    seperatelist=product.split("\n")
    mani_total=0
    logendran_total=0
    satheesh_total=0

    for everyline in seperatelist:
        if len(everyline)>0:
            customer_list=everyline.split("|")
            mani_total=mani_total+int(customer_list[0])
            logendran_total=logendran_total+int(customer_list[1])
            satheesh_total=satheesh_total+int(customer_list[2])
    print(mani_total)
    print("mani total bill value")
    print(logendran_total)
    print("logendran total bill value")
    print(satheesh_total)
    print("satheesh_total bill value")
product()
amzproduct() 




    





