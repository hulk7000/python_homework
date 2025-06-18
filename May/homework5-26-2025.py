# dic = {"ip" : "172.16.31.10", "mask":"255.255.255.0","gw":"172.16.31.1","dns":"8.8.8.8"}
# for k,v in dic.items():
#     a = '{} : {}'.format(k,v)
#     print(a)
# output example ---->  ip : 172.16.31.10


# list1 = ["ip","mask","gw","dns"]
# list2 =["172.16.31.10", "255.255.255.0","172.16.31.1","8.8.8.8"]
# for k,v in zip(list1,list2):
#     a = '{} : {}'.format(k,v)
#     print(a)
# output example ---->  ip : 172.16.31.10

# list3 =["172.16.31.10", "255.255.255.0","172.16.31.1","8.8.8.8"]
# for k in list3:
#     a = '{} this is 2 ip address in the list!!!'.format(k)
#     print(a)

# output example ---->  255.255.255.0 this is 2 ip address in the list!!!

# list4 =["172.16.31.10", "255.255.255.0","172.16.31.1","8.8.8.8"]
# for i in range (len(list4)):
#     a = '{} this is {} ip address!!!'.format(list4[i],i+1)
#     print(a)
# output example ---->
# 172.16.31.10 this is 1 ip address in the list!!!
# 255.255.255.0 this is 2 ip address in the list!!!
# 172.16.31.1 this is 3 ip address in the list!!!
# 8.8.8.8 this is 4 ip address in the list!!!