BOOTSTRAP=4.1.3
JQUERY=3.3.1
POPPER=1.14.4
FONTAWESOME=5.3.1
FONTS=fa-solid-900.ttf fa-solid-900.woff fa-solid-900.woff2

.PHONY: all clean bootstrap jquery popper fontawesome webfonts

all: bootstrap jquery popper fontawesome

bootstrap: static/include/css/bootstrap.min.css static/include/js/bootstrap.min.js
jquery: static/include/js/jquery.min.js
popper: static/include/js/popper.min.js
webfonts: $(addprefix static/include/webfonts/,$(FONTS))
fontawesome: static/include/css/fontawesome.css webfonts

static/include/js:
	mkdir -p static/include/js

static/include/css:
	mkdir -p static/include/css

static/include/webfonts:
	mkdir -p static/include/webfonts


static/include/css/bootstrap.min.css: static/include/css
	curl https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/$(BOOTSTRAP)/css/bootstrap.min.css -o $@

static/include/js/bootstrap.min.js: static/include/js
	curl https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/$(BOOTSTRAP)/js/bootstrap.min.js -o $@

static/include/js/jquery.min.js: static/include/js
	curl https://cdnjs.cloudflare.com/ajax/libs/jquery/$(JQUERY)/jquery.min.js -o $@

static/include/js/popper.min.js: static/include/js
	curl https://cdnjs.cloudflare.com/ajax/libs/popper.js/$(POPPER)/umd/popper.min.js -o $@

static/include/css/fontawesome.css: static/include/css
	curl https://use.fontawesome.com/releases/v$(FONTAWESOME)/css/all.css -o $@

static/include/webfonts/%: static/include/webfonts
	curl https://use.fontawesome.com/releases/v$(FONTAWESOME)/webfonts/$* -o $@


clean:
	rm -rf static/include
