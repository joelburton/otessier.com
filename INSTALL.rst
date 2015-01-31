Dev environment::

    virtualenv env
    source env/bin/activate
    sudo env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/opt/local/lib" CFLAGS="-I/opt/local/include" pip install cryptography
    pip install -r requirements/local.txt


