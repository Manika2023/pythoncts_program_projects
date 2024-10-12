mydict=[{"name":"monika","phone_number":"vkdnvfl"},
       {"name":"monikak","phone_number":"vkdnvfl"}
        ]

# print(mydict[0]['name'])
for i ,value in enumerate(mydict,start=1):
     print(f"{i}: name is {value['name']} and number is {value['phone_number']}") 

def search():
   search_term= input("Enter your name or number: ")
   if search_term:    
     for value in mydict:
          if value['name']==search_term or value['phone_number']== search_term:
                 print(f"{i}: name is {value['name']} and number is {value['phone_number']}") 
                 return
          else:
                print("No result found")
                return
   return
     
search()