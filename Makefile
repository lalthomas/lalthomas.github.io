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
	pandoc --standalone \
	       --from markdown \
	       --to html \
	       --css https://unpkg.com/sakura.css/css/sakura.css \
	       --metadata title="$<" \
	       $< -o $@

tar: $(MARKDOWN)
	tar --exclude=notes.tar.gz --exclude=.git/ -czvf notes.tar.gz ./

clean:
	rm $(HTML)
