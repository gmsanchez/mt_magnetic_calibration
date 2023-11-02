#!/usr/bin/python3

"""
hex_from_mfm.py

This script converts the output binary file obtained from Magnetig Field Mapper (MFM)
into a string of hex, making it ready to upload to the MTi device.

The MFM results file contains a single Xbus message that contains the calibration results.
If this message is sent to the MT, it will update the non-volatile memory which holds the
calibration values. Follow the next instructions to update the calibration parameters:

1. Copy the MFM results file to the system that has a direct connection to the MT.
2. Ensure that the MT is powered on.
3. Make sure that the MT is in Config mode.
4. Write the binary data message in the MFM results file to the sensor as a single XBus
message, using binary communication. In MT Manager, you can test this procedure
by opening the Device Data View and pasting the MFM results message into the
message field
5. Upon receiving the message, the MT will update its non-volatile memory with the
new calibration values. In MT Manager, you can verify this by comparing the
calibration parameters in the MT Settings window, before and after writing the
calibration results. Disconnecting and reconnecting the device is necessary for MT
Manager to update the calibration parameters.

"""

import binascii
import sys

if len(sys.argv) != 2:
    print("Usage: python3 hex_from_mfm.py <binary_file>")
    sys.exit(1)

binary_file_path = sys.argv[1]

try:
    # Open the binary file for reading in binary mode
    with open(binary_file_path, 'rb') as binary_file:
        # Read the binary data
        binary_data = binary_file.read()

    # Convert binary data to hexadecimal representation without spaces
    hex_data = binascii.hexlify(binary_data).decode('utf-8')

    # Convert binary data to hexadecimal representation with spaces
    hex_data_with_spaces = ' '.join([binascii.hexlify(binary_data[i:i+1]).decode('utf-8') for i in range(len(binary_data))])

    # Output the hexadecimal data with spaces
    print(hex_data_with_spaces)

except FileNotFoundError:
    print(f"File '{binary_file_path}' not found.")
    sys.exit(1)