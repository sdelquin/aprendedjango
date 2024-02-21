runserver port='9000':
    sphinx-autobuild --port {{ port }} . _build/html

cleanrun port='9000': clean
    just runserver {{ port }}

clean:
    make clean

html:
    make dirhtml

ideas:
    open ideas.pdf
