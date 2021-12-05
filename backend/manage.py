#!/usr/bin/env python
# Imports from Third Party Modules
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local")


    # Imports from Django
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
