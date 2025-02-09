all: serve

serve:
	hugo server --watch -D --renderToMemory
