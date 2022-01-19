The script is one possible solution of the following exercise: 

7. Articles
Create a class Article. The __init__ method should accept 3 arguments: title, content, author. The class
should also have 4 methods:
 edit(new_content) - changes the old content to the new one
 change_author(new_author) - changes the old author to with the new one
 rename(new_title) - changes the old title with the new one
 __repr__() - returns the following string "{title} - {content}: {author}"
Example

Test Code 					Output

article = Article("some title", "some 		new title - new content: new
content", "some author")			author
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)



