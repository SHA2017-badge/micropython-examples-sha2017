#import qrcode
#qr = qrcode.QRCode(
    #version=1,
    #error_correction=qrcode.constants.ERROR_CORRECT_L,
    #box_size=10,
    #border=0,
#)
#qr.add_data('SHA2017 test data')
#qr.make(fit=True)

#matrix = qr.get_matrix()

import ugfx
import pyqrnative
qr = pyqrnative.QRCode(3, pyqrnative.QRErrorCorrectLevel.L)
qr.addData("test")
qr.make()
k = qr.getModuleCount()

matrix = qr.modules

max_x = len(matrix)
max_y = len(matrix[0])

disp_x, disp_y = (296, 128)
block_x = int(disp_x/max_x)
block_y = int(disp_y/max_y)

block_size = min(block_x, block_y)
offset_x = int(disp_x/2) - int(block_size*max_y/2)
offset_y = int(disp_y/2) - int(block_size*max_x/2)

ugfx.init()
ugfx.clear(ugfx.WHITE)
for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        if qr.isDark(x, y):
            ugfx.area(offset_x+x*block_size, offset_y+y*block_size, block_size, block_size, ugfx.BLACK)
ugfx.flush()
