"""Minimal example for DictBot."""

from dictbot import dictbot


def main():
 runner = dictbot({"name": "DictBot", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()