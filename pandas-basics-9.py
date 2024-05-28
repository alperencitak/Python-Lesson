import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'Name': ["Ahmet","Ali","Mehmet","Ayşe"],
#     'Age': [19,24,20,35]
# }
#
# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010','2019','2023','2020']
# }
#
# df_customers = pd.DataFrame(customers, columns=["CustomerId","Name","Age"])
# df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])
#
# print(df_customers)
# print(df_orders)
#
# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="left")
# result = pd.merge(df_customers,df_orders,how="right")
# result = pd.merge(df_customers,df_orders,how="outer")

customersA = {
    'CustomerId': [1,2,3,4],
    'Name': ["Ahmet","Ali","Mehmet","Ayşe"],
    'Age': [19,24,20,35]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'Name': ["Selim","Yağmur","Çınar","Can"],
    'Age': [42,25,32,21]
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerId","Name","Age"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerId","Name","Age"])

# result = pd.concat([df_customersA,df_customersB],axis=1)
result = pd.concat([df_customersA,df_customersB],axis=0)
result = pd.concat([df_customersA,df_customersB],axis=0, ignore_index=True)

print(result)
