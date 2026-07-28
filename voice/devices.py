"""
Audio Device Manager
"""

import sounddevice as sd


def list_devices():

    devices = sd.query_devices()

    print("\n========== AUDIO DEVICES ==========\n")

    for index, device in enumerate(devices):

        print(
            f"[{index}] "
            f"{device['name']} "
            f"(Inputs: {device['max_input_channels']}, "
            f"Outputs: {device['max_output_channels']})"
        )


def default_input():

    device = sd.default.device

    return device[0]