import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui
import PyQt5.QtCore as util


class ViewToggle(qt.QWidget):
    def __init__(self, frame, ctrls, start_values=None):
        # initialise
        qt.QWidget.__init__(self, frame)
        self.frame = frame
        # setup layout
        self.setMaximumHeight(44)
        self.setMinimumHeight(44)
        self.sizer = qt.QHBoxLayout(self)

        # store ctrls
        self.ctrls = ctrls
        # array for buttons
        self.btns = {}

        for name in self.ctrls:
            # make button
            btn = qt.QPushButton("", self)
            self.btns[name] = btn
            # make icon
            icon = gui.QIcon(f"markmoji_editor/assets/icons/{name}.svg")
            # try to set icon, set label if null
            if not icon.isNull():
                btn.setIcon(icon)
            else:
                btn.setText(name)
            # set size
            btn.setIconSize(util.QSize(16, 16))
            btn.setMaximumSize(48, 32)
            # make into a toggle button
            btn.setCheckable(True)
            # link function
            btn.clicked.connect(self.refresh_view)
            # add to sizer
            self.sizer.addWidget(btn)

        # apply start layout
        if start_values is None:
            start_values = {name: True for name in self.btns}
        for name, val in start_values.items():
            if name in self.btns:
                self.btns[name].setChecked(val)
        self.refresh_view()
    
    def refresh_view(self, evt=None):
        for name, btn in self.btns.items():
            # show/hide ctrl according to button state
            if btn.isChecked():
                self.ctrls[name].show()
            else:
                self.ctrls[name].hide()
