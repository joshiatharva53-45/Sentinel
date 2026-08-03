from core.engine import Engine


def main():

    engine = Engine()

    engine.initialize()

    engine.start()

    print()

    print("===== SERVICES =====")

    print(engine.config)

    print(engine.logger)

    print(engine.event_bus)

    print()

    engine.stop()

    engine.shutdown()

    print("Sentinel Core Started Successfully")


if __name__ == "__main__":

    main()