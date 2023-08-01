from app import App
from config import Config


def main():
    config = Config()
    App().run(config)


if __name__ == '__main__':
    main()
