import xmlrpc.client
client=xmlrpc.client.ServerProxy("http://localhost:6789")
num=7
print("calling function double through proxy")
result=client.double(num)
print(result)