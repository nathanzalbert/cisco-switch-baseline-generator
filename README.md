# Cisco Catalyst 9000 Baseline Generator

A Python script that generates a standardized baseline configuration for Cisco Catalyst 9000 Series switches.

## Features

* Generates a Cisco IOS XE baseline configuration
* Customizable variables for common deployment settings
* Prints the completed configuration directly to the terminal
* No external Python libraries required
* Easy to modify and expand

## Requirements

* Python 3.x

## Usage

1. Edit the variables at the top of the script.
2. Run the script:

```bash
python catalyst9000_baseline.py
```

3. Copy the generated configuration from the terminal and apply it to your Cisco Catalyst 9000 switch.

## Future Enhancements

* Interactive user input
* Jinja2 templates
* YAML/JSON configuration support
* Netmiko deployment
* Multi-switch configuration generation
* Additional Cisco platform support

## Disclaimer

This project is intended for learning and lab environments. Always review and test generated configurations before deploying them to production.

## Author

**Nathan Albert**
