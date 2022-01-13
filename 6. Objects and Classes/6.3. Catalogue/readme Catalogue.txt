The script is one possible solution of the following exercise: 

3. Catalogue
Create a class Catalogue. The __init__ method should accept the name of the catalogue. Each catalogue should
also have an attribute called products and it should be a list. The class should also have three more methods:
 add_product(product) - add the product to the product list
 get_by_letter(first_letter) - returns a list containing only the products that start with the given
letter
 __repr__ - returns the catalogue info in the following format:
"Items in the {name} catalogue:
{item1}
{item2}
…"
The items should be sorted alphabetically (default sorting)
Example

Test Code Output

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror";)
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

['Chair', 'Carpet']
Items in the Furniture catalogue:
Carpet
Chair
Desk
Mirror
Sofa




