#!/usr/bin/env python3

import socket
import argparse


class KVMManager:
    def __init__(self, ip="192.168.1.10", port=5000):
        self.ip = ip
        self.port = port

    def send_command(self, command):
        """
        Send a hexadecimal command to the KVM.
        :param command: List of bytes or a hexadecimal string.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.sendall(bytes(command))
                response = s.recv(1024)
                return response
        except Exception as e:
            print(f"Error sending the command: {e}")
            return None

    def switch_input(self, pc_number):
        """
        Switch to the specified input port.
        :param pc_number: PC number (1-8).
        """
        if 1 <= pc_number <= 8:
            command = [0xAA, 0xBB, 0x03, 0x01, pc_number, 0xEE]
            response = self.send_command(command)
            print(f"Switched to PC{pc_number}, response: {response}")
        else:
            print("Invalid PC number. Must be between 1 and 8.")

    def set_led_timeout(self, timeout):
        """
        Set the LED timeout duration.
        :param timeout: '10s', '30s', or 'never'.
        """
        timeouts = {"10s": 0x0A, "30s": 0x1E, "never": 0x00}
        if timeout in timeouts:
            command = [0xAA, 0xBB, 0x03, 0x03, timeouts[timeout], 0xEE]
            response = self.send_command(command)
            print(f"LED timeout set to {timeout}, response: {response}")
        else:
            print("Invalid timeout. Options: '10s', '30s', 'never'.")

    def mute_buzzer(self):
        """Mute the buzzer."""
        command = [0xAA, 0xBB, 0x03, 0x02, 0x00, 0xEE]
        response = self.send_command(command)
        print(f"Buzzer muted, response: {response}")

    def unmute_buzzer(self):
        """Unmute the buzzer."""
        command = [0xAA, 0xBB, 0x03, 0x02, 0x01, 0xEE]
        response = self.send_command(command)
        print(f"Buzzer unmuted, response: {response}")

    def set_auto_input_detection(self, enable):
        """
        Enable or disable auto input detection.
        :param enable: True to enable, False to disable.
        """
        command = [0xAA, 0xBB, 0x03, 0x81, 0x01 if enable else 0x00, 0xEE]
        response = self.send_command(command)
        state = "enabled" if enable else "disabled"
        print(f"Auto input detection {state}, response: {response}")

    def get_active_input(self):
        """Read the active input port."""
        command = [0xAA, 0xBB, 0x03, 0x10, 0x00, 0xEE]
        response = self.send_command(command)
        if response:
            active_port = response[4] + 1  # Convert index to port (PC1=0x00 -> 1)
            print(f"Active input port: PC{active_port}")
        else:
            print("Failed to retrieve active input port.")


def main():
    parser = argparse.ArgumentParser(
        description="Manage a TESmart HKS801-E23-EUBK KVM switch."
    )
    parser.add_argument(
        "--ip",
        type=str,
        default="192.168.1.10",
        help="KVM IP address (default: 192.168.1.10)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="KVM port (default: 5000)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("mute_buzzer", help="Mute the buzzer")
    subparsers.add_parser("unmute_buzzer", help="Unmute the buzzer")
    subparsers.add_parser("get_active_input", help="Get the active input port")

    switch_input_parser = subparsers.add_parser(
        "switch_input", help="Switch to a specific input port"
    )
    switch_input_parser.add_argument(
        "pc_number", type=int, help="PC number (1-8)"
    )

    led_timeout_parser = subparsers.add_parser(
        "set_led_timeout", help="Set the LED timeout duration"
    )
    led_timeout_parser.add_argument(
        "timeout", choices=["10s", "30s", "never"], help="Timeout duration"
    )

    auto_input_parser = subparsers.add_parser(
        "set_auto_input_detection", help="Set auto input detection state"
    )
    auto_input_parser.add_argument(
        "state", choices=["enable", "disable"], help="Enable or disable"
    )

    args = parser.parse_args()

    kvm = KVMManager(ip=args.ip, port=args.port)

    if args.command == "mute_buzzer":
        kvm.mute_buzzer()
    elif args.command == "unmute_buzzer":
        kvm.unmute_buzzer()
    elif args.command == "get_active_input":
        kvm.get_active_input()
    elif args.command == "switch_input":
        kvm.switch_input(args.pc_number)
    elif args.command == "set_led_timeout":
        kvm.set_led_timeout(args.timeout)
    elif args.command == "set_auto_input_detection":
        kvm.set_auto_input_detection(args.state == "enable")


if __name__ == "__main__":
    main()

