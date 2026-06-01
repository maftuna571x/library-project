#!/usr/bin/env python
"""Django administrative vazifalari uchun."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django'ni import qila olmadik. Virtual muhit faollashtirilganini "
            "va 'pip install django' bajarilganini tekshiring."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
