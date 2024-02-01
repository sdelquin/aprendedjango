runserver:
    make livehtml

html:
    make dirhtml

pdf:
    make latexpdf

deploy:
    rsync -avzr --delete _build/ aprendedjango.es:~/code/aprendedjango/
