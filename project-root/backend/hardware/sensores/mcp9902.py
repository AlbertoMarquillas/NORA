"""
mcp9902.py – Lectura de temperatura mediante el sensor MCP9902 conectado por I²C.
Compatible con Raspberry Pi y la librería smbus2.
"""

from smbus2 import SMBus
from hardware.config_gpios import I2C_BUS, TEMP_SENSOR_I2C_ADDR

# Registro de temperatura local del MCP9902 según datasheet
TEMP_LOCAL_MSB = 0x00
TEMP_LOCAL_LSB = 0x29

def leer_temperatura_mcp9902():
    """
    Lee la temperatura del sensor MCP9902 a través del bus I²C.

    :return: Temperatura en grados Celsius (float)
    :raises RuntimeError: Si no se puede leer del sensor
    """
    try:
        with SMBus(I2C_BUS) as bus:
            msb = bus.read_byte_data(TEMP_SENSOR_I2C_ADDR, TEMP_LOCAL_MSB)
            lsb = bus.read_byte_data(TEMP_SENSOR_I2C_ADDR, TEMP_LOCAL_LSB)

            # Conversión según datasheet: temperatura = MSB + (LSB >> 6) * 0.25
            decimal = (lsb >> 6) * 0.25
            temperatura = msb + decimal

            return round(temperatura, 2)

    except Exception as e:
        raise RuntimeError(f"Error al leer MCP9902: {e}")
