import argparse

from config import Settings


def make_parser() -> argparse.ArgumentParser:
    default_settings = Settings()
    parser = argparse.ArgumentParser(
        description="Example description", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    for field, info in default_settings.model_fields.items():
        arg_name = f"--{field}"
        kwargs = {"help": info.description, "default": eval(f"default_settings.{field}"), "type": info.annotation}
        if kwargs["type"] is bool:
            kwargs["action"] = "store_true"
            kwargs.pop("type")
        parser.add_argument(arg_name, **kwargs)
    return parser
