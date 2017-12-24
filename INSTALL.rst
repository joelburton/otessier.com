Dev environment::

    virtualenv -p /path/to/python3 env
    source env/bin/activate
    sudo env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/opt/local/lib" CFLAGS="-I/opt/local/include" pip install cryptography
    pip install -r requirements/local.txt

    createdb otessier
    python project/manage.py migrate
    python project/maange.py loaddata initial
    python project/manage.py createsuperuser


