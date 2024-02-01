runserver:
    make livehtml

html:
    make dirhtml

pdf:
    make latexpdf

deploy:
    make dirhtml
    rsync -avzr --delete _build/ aprendedjango.es:~/code/aprendedjango/
