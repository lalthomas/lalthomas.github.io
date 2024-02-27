# 2022-11-30 
# This make is  file is used for generating html files for all markdown down file in the folder and convert the markdown file links to html

# Find all markdown files
MARKDOWN=$(shell find . -iname "*.md")

# Form all 'html' counterparts
HTML=$(MARKDOWN:.md=.html)

.PHONY = all tar clean
all: $(HTML)
	git add .
	git commit -m "update the website"
	git push

%.html: %.md
	pandoc --lua-filter links-to-html.lua \
	       --standalone \
	       --from markdown \
	       --to html \
	       --css https://unpkg.com/sakura.css/css/sakura.css \
	       $< -o $@

tar: $(MARKDOWN)
	tar --exclude=notes.tar.gz --exclude=.git/ -czvf notes.tar.gz ./

clean:
	rm $(HTML)
