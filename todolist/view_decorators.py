import functools
import logging


logger = logging.getLogger(__name__)


def check_schema(schema_name):
    def view_with_schema(func):
        @functools.wraps(func)
        def check_schema_and_run_view(*args, **kwargs):
            logger.info("Skipping schema check: not implemented yet")
            return func(*args, **kwargs)

        return check_schema_and_run_view

    return view_with_schema
