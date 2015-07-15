import glob
import markdown

template = None
with open('template.html') as f:
  template = f.read()

posts = []
for post in glob.glob("posts/*"):
  with open(post) as p:
    posts.append(p.read())

rendered_html = ''
for post in posts:
  rendered_html = rendered_html + markdown.markdown(post) 

blog = template.format(content=rendered_html)

with open('site.html', 'w') as out:
  out.write(blog)