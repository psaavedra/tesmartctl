# KVM Switch Manager for TESmart HKS801-E23-EUBK

A Python script to control the TESmart HKS801-E23-EUBK KVM switch over LAN, enabling operations such as switching input sources, setting LED timeouts, and managing the buzzer.

## Features

- Switch between input sources (PC1 to PC8).
- Set LED timeout durations.
- Mute or unmute the buzzer.
- Enable or disable auto input detection.
- Retrieve the current active input port.

## Requirements

- Python 3.x
- Network access to the KVM switch.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/psaavedra/tesmartctl.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tesmartctl
   ```

3. Install the project:

   ```bash
   pip install -e .
   ```

## Usage

The script utilizes `argparse` for command-line argument parsing. You can specify the KVM's IP address and port, and execute various commands.

```bash
python tesmartctl.py --ip 192.168.1.10 --port 5000 <command> [options]
```

Replace `<command>` with one of the following:

- `switch_input`: Switch to a specific input port.
- `set_led_timeout`: Set the LED timeout duration.
- `mute_buzzer`: Mute the buzzer.
- `unmute_buzzer`: Unmute the buzzer.
- `set_auto_input_detection`: Enable or disable auto input detection.
- `get_active_input`: Retrieve the current active input port.

### Examples

1. **Switch to PC2:**

   ```bash
   python tesmartctl.py --ip 192.168.1.10 --port 5000 switch_input 2
   ```

2. **Set LED timeout to 30 seconds:**

   ```bash
   python tesmartctl.py --ip 192.168.1.10 --port 5000 set_led_timeout 30s
   ```

3. **Mute the buzzer:**

   ```bash
   python tesmartctl.py --ip 192.168.1.10 --port 5000 mute_buzzer
   ```

4. **Enable auto input detection:**

   ```bash
   python tesmartctl.py --ip 192.168.1.10 --port 5000 set_auto_input_detection enable
   ```

5. **Get the current active input port:**

   ```bash
   python tesmartctl.py --ip 192.168.1.10 --port 5000 get_active_input
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

