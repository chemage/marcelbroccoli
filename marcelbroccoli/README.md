# Marcel Broccoli

Marcel's broccoli module for simplifying his coding.

## Functions

### `load_config_file(cfg_file:str)`

Load a JSON configuration and return a configuration object.

### `set_working_dir(folder:str) -> str`

Set working dir to folder and return `working_dir`.

### `write_json_file(data, fname:str)`

Write JSON to file.

### `starts_with(string:str, pattern:str, casesensitive:bool=True)`

Test if a string starts with pattern:

- string: string to search in.
- pattern: string to search for in source start.
- casesensitive: if set to false, set source and value to lower (default: True).

### `str2datetime(str:str, format:str='%Y-%m-%d %H:%M:%s.%f') -> datetime`

Convert from all date and date time sources to date object.

### `datetime2str(dt:datetime, format:str='%d-%m-%Y %H:%M:%s.%f') -> str`

Convert date to string in HomeBank format.

### `format_phone(tel:str, spaces:bool=True)`

Format telephone number to Swiss or French pattern.

- tel: string with a phone number.
- spaces: add spaces if true.

## Logger

The logger module is based on the `logging` module.

The `logger` object created in the module is based on `CustomLogger` which inherits `logging.Logger`.

Run `logger.logger.configure(...)` to setup logging as needed.
