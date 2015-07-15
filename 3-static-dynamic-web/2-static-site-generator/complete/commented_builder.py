# When we're finished, this script will find multiple markdown blog posts 
# and write them as one html file, which can be loaded in a browser or with 
# a web server.  

# First we'll import the libraries we need:
import glob       # To help us load multiple files
import markdown   # To convert markdown to html

# 1. We need to get the layout html from the template.html file
# How can you read in a file?
# Add to the code below ot read the template. 
template = None
with open('template.html') as f:
  template = f.read()

# 2. Now we need to get content from markdown files in the posts directory 
# into a list so we can work with them. Here's the empty list:
posts = []
# Put the strings from the md files into the posts list.
# Use glob to help: https://docs.python.org/2/library/glob.html
# Iterate over the results from glob and append them to the posts list 
for post in glob.glob("posts/*"):
  with open(post) as p:
    posts.append(p.read())


# 3. Now let's convert each markdown string to html and add it to a new string
rendered_html = ''
# Iterate over the posts array. 
# Convert each item to html and concatenate it to the main string
for post in posts:
  rendered_html = rendered_html + markdown.markdown(post)

# 4. Assemble the posts and template so we have a single page blog
blog_page = template.format(content=rendered_html)

# 5. Write the html we generated to a file called site.html
with open('site.html', 'w') as out:
  out.write(blog)