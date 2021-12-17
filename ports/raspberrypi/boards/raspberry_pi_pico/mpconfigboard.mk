USB_VID = 0x239A
USB_PID = 0x80F4
USB_PRODUCT = "Pico"
USB_MANUFACTURER = "Raspberry Pi"

CHIP_VARIANT = RP2040
CHIP_FAMILY = rp2

EXTERNAL_FLASH_DEVICES = "W25Q16JVxQ"

CIRCUITPY__EVE = 1

CIRCUITPY_USB_MIDI = 0
CIRCUITPY_USB_HID_MOUSE = 0

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BLE
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_HID
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BusDevice
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_SSD1306
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BLE

FROZEN_MPY_DIRS += $(TOP)/frozen/kmk