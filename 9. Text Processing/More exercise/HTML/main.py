def put_tags (text, body):
    print(f"<{body}>\n    {text}\n</{body}>")


put_tags(input(), body= "h1")
put_tags(input(), body= "article")
comment = input()
while not comment == "end of comments":
    put_tags(comment, body="div")
    comment = input()