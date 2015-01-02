# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('consulting', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE FUNCTION insert_client_id() RETURNS trigger
            LANGUAGE plpgsql
            AS $$
            BEGIN
              new.client_id = client_id
                                FROM consulting_clientwork AS cw
                                WHERE cw.id = new.clientwork_id;
            RETURN new;
            END; $$;
            """
        ),
        migrations.RunSQL(
            """
              ALTER TABLE consulting_client ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_client ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_client ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_client ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_client ALTER position SET DEFAULT 99;

              ALTER TABLE consulting_clientreference ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_clientreference ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_clientreference ALTER position SET DEFAULT 1;

              ALTER TABLE consulting_clientwork ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_clientwork ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_clientwork ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_clientwork ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_clientwork ALTER position SET DEFAULT 1;

              ALTER TABLE consulting_consultant ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_consultant ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_consultant ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_consultant ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_consultant ALTER position SET DEFAULT 100;

              ALTER TABLE consulting_practicearea ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_practicearea ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_practicearea ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_practicearea ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_practicearea ALTER position SET DEFAULT 100;

              ALTER TABLE consulting_qanda ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_qanda ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_qanda ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_qanda ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_qanda ALTER position SET DEFAULT 100;

              ALTER TABLE consulting_quote ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_quote ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_quote ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_quote ALTER status SET DEFAULT 'published';

              ALTER TABLE consulting_libraryfile ALTER created SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_libraryfile ALTER modified SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_libraryfile ALTER status_changed SET DEFAULT CURRENT_TIMESTAMP;
              ALTER TABLE consulting_libraryfile ALTER status SET DEFAULT 'published';
              ALTER TABLE consulting_libraryfile ALTER position SET DEFAULT 100;
          """
        ),
        migrations.RunSQL(
            """
            ALTER TABLE consulting_client ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_client ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_clientwork ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_consultant ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_consultant ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_practicearea ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_practicearea ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_qanda ADD CHECK (slug ~ '^[a-z\d-]+$');
            ALTER TABLE consulting_qanda ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_quote ADD CHECK (status IN ('published', 'private'));

            ALTER TABLE consulting_libraryfile ADD CHECK (status IN ('published', 'private'));
          """
        ),
        migrations.RunSQL(
            """
            ALTER TABLE consulting_clientwork_references ADD client_id INTEGER NOT NULL;

            CREATE UNIQUE INDEX clientreference_match ON consulting_clientreference USING btree (id, client_id);

            CREATE UNIQUE INDEX clientwork_match ON consulting_clientwork USING btree (id, client_id);

            CREATE TRIGGER insert_client_id BEFORE INSERT OR UPDATE ON consulting_clientwork_references FOR EACH ROW EXECUTE PROCEDURE insert_client_id();

            ALTER TABLE ONLY consulting_clientwork_references
             ADD CONSTRAINT consulting_clientwork_references_client_id_fkey
             FOREIGN KEY (client_id) REFERENCES consulting_client(id);

            ALTER TABLE ONLY consulting_clientwork_references
              ADD CONSTRAINT consulting_clientwork_references_clientreference_id_fkey
              FOREIGN KEY (clientreference_id, client_id) REFERENCES consulting_clientreference(id, client_id);

            ALTER TABLE ONLY consulting_clientwork_references
              ADD CONSTRAINT consulting_clientwork_references_clientwork_id_fkey
              FOREIGN KEY (clientwork_id, client_id) REFERENCES consulting_clientwork(id, client_id);
              """
        )
    ]
