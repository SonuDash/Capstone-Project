from pynq import Overlay
from pynq import MMIO
import time

# Load the overlay (bitstream) onto the FPGA
overlay = Overlay("base.bit")

# Register addresses for HMC5883L
HMC5883L_ADDRESS = 0x1E
HMC5883L_REG_CONFIG_A = 0x00
HMC5883L_REG_CONFIG_B = 0x01
HMC5883L_REG_MODE = 0x02
HMC5883L_REG_DATA_X_MSB = 0x03
HMC5883L_REG_DATA_X_LSB = 0x04
HMC5883L_REG_DATA_Z_MSB = 0x05
HMC5883L_REG_DATA_Z_LSB = 0x06
HMC5883L_REG_DATA_Y_MSB = 0x07
HMC5883L_REG_DATA_Y_LSB = 0x08
HMC5883L_REG_STATUS = 0x09
HMC5883L_ID_REG_A = 0x10
HMC5883L_ID_REG_B = 0x11
HMC5883L_ID_REG_C = 0x12

# Configure I2C
i2c = overlay.iop_pmoda.mb_i2c_pmod
i2c.set_addr(HMC5883L_ADDRESS)

# Configure HMC5883L
i2c.write(HMC5883L_REG_CONFIG_A, 0x70)  # Configure average samples to 8 and output rate to 15Hz
i2c.write(HMC5883L_REG_MODE, 0x00)       # Set to continuous measurement mode

# Read and output data
while True:
    # Check if data is ready
    status = i2c.read(HMC5883L_REG_STATUS, 1)[0]
    if (status & 0x01) != 0:
        # Read data
        data = i2c.read(HMC5883L_REG_DATA_X_MSB, 6)
        x = (data[0] << 8) | data[1]
        y = (data[2] << 8) | data[3]
        z = (data[4] << 8) | data[5]
        
        # Output data
        print(f"X: {x}, Y: {y}, Z: {z}")
        
    time.sleep(0.1)  # Wait before reading next data
