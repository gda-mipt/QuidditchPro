from PyQt5.QtGui import QFont

standart_font = 'Garamond'

H2 = QFont()
H2.setFamily(standart_font)
H2.setPointSize(16)
H2.setBold(True)

H3 = QFont()
H3.setFamily(standart_font)
H3.setPointSize(14)
H3.setBold(True)

TextFont = QFont()
TextFont.setFamily(standart_font)
TextFont.setPointSize(10)
TextFont.setBold(False)