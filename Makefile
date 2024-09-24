all: serve

serve:
	hugo server --watch --verbose --disableFastRender --port 8080 --bind 0.0.0.0
