# Marcel Broccoli

Marcel's broccoli module for simplifying his coding.

## Functions

### `load_env()`

Load `.env` secret file.

### `load_config_file(cfg_file:str)`

Load a JSON configuration and return a configuration object.

## Logger

The logger module is based on the `logging` module.

The `logger` object created in the module is based on `CustomLogger` which inherits `logging.Logger`.

Run `logger.logger.configure(...)` to setup logging as needed.
