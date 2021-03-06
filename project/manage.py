#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    try:
        # noinspection PyPackageRequirements,PyUnresolvedReferences
        import env
    except ImportError:
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "otessier.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
