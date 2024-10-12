Contacts=[]

# function for adding contact

def add_contact():
     name=input("Enter name: ")
     phone_number=input("Enter Phone number: ")
     email=input("Enter Email: ")
     address=input("Enter address")

     Contacts.append({"name":name,"phone_number":phone_number,"email":email,"address":address})
     print(f"Contact {name} addes successfully")


# function to view contact
def view_contact():
     if not Contacts:
          print("No contact availbale to view")
          return
     print("\n Contact List")
     # value : Contact[index]
     # value : Contact[index][name]
     for index , value in enumerate(Contacts,start=1):
          print(f"{index} ->Name: {value['name']},Phone Number: {value['phone_number']} ")



# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter name or phone number to search: ")

    # Find contacts that match the search term
    for contact in Contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Found Contact - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

        else:
         print("No contact found.")

# function for update Contact-> take index-> and take new information and store in dictionary with same key
def update_contact():
    view_contact()
    index=int(input("Enter index number to update"))-1
    if 0 <= index > len(Contacts):
        name=input("Enter new Name (leave blank to keep unchanged):")
        phone_number = input("Enter new Phone (leave blank to keep unchanged): ")
        email = input("Enter new Email (leave blank to keep unchanged): ")
        address = input("Enter new Address (leave blank to keep unchanged): ")
        if name:
            Contacts[index]['name']=name
        if phone_number:
          Contacts[index]['phone_number']=phone_number
        if email:
          Contacts[index]['email']=email
        if address:
           Contacts[index]['address']=address
        print("updated successfully")   
    else:
        print("enter valid index")   
    
 
# Function to delete a contact
def delete_contact():
    view_contact()
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(Contacts):
        deleted_contact = Contacts.pop(index)
        print(f"Deleted contact: {deleted_contact['name']}")
    else:
        print("Invalid contact number.")       
    
# Main function to display the menu and handle user inputs:

def contact_manager():
    while True:
        print("\n--- Contact Management System ---")
        print("1. View Contact List")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice=int(input("enter your choice: "))  
        if choice == 1:
            view_contact()
        if choice == 2:
            add_contact()    
        if  choice == 3:
            search_contact()  
        if choice== 4:
            update_contact()
        if choice==5:
            delete_contact()        
        if choice==6:
            print("Exiting contact manager.")
            break
        else:
            print("Enter correct choice ")        
if __name__ == "__main__":
    contact_manager()