import time
from django.utils.encoding import force_str
from contextlib import contextmanager
from django.db.backends.postgresql.base import DatabaseWrapper as DjangoDatabaseWrapper
from django.db.backends.utils import CursorWrapper as DjangoCursorWrapper
from shop.middleware import thread_locals


def make_safe(string):
    return string.replace("*", "").replace("\\", "").replace("%", "")


@contextmanager
def calc_sql_time(sql):
    timestamp = time.monotonic()

    yield

    if hasattr(thread_locals, "sql_count"):
        thread_locals.sql_count += 1
        thread_locals.sql_total += time.monotonic() - timestamp


class CursorWrapper(DjangoCursorWrapper):
    def execute(self, sql, params=None):
        path = getattr(thread_locals, "path", "")
        if path:
            path = make_safe(path)
            sql = f"/* {path} */\n{force_str(sql)}\n/* {path} */"

        with calc_sql_time(sql):
            return super().execute(sql, params)


class DatabaseWrapper(DjangoDatabaseWrapper):
    def create_cursor(self, name=None):
        cursor = super().create_cursor(name)
        return CursorWrapper(cursor, self)
