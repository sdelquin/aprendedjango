runserver:
    make livehtml

clean:
    make clean

html:
    make dirhtml

pdf:
    make latexpdf

deploy:
    make dirhtml
    rsync -avzr --delete _build/ aprendedjango.es:~/code/aprendedjango/
