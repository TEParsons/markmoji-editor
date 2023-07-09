import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui
import PyQt5.QtCore as util


class ViewToggle(qt.QWidget):

    class ViewToggleButton(qt.QPushButton):
        def __init__(self, parent, ctrl, tooltip=None, icon_name=None, label=""):
            # initialise
            qt.QPushButton.__init__(self, "", parent)
            self.parent = parent
            
            # link ctrl
            self.ctrl = ctrl
            # set icon
            if icon_name is not None:
                icon = gui.QIcon(f"markmoji_editor/assets/icons/{icon_name}.svg")
                self.setIcon(icon)
            # set label
            self.setText(label)
            # set tooltip
            if tooltip is None:
                # if none given, use label
                tooltip = label
            self.setToolTip(tooltip)
            # set size
            self.setIconSize(util.QSize(16, 16))
            self.setMaximumSize(48, 32)
            # make into a toggle button
            self.setCheckable(True)
            # link function
            self.clicked.connect(self.parent.refresh_view)

    def __init__(self, frame):
        # initialise
        qt.QWidget.__init__(self, frame)
        self.frame = frame
        # setup layout
        self.setMaximumHeight(44)
        self.setMinimumHeight(44)
        self.sizer = qt.QHBoxLayout(self)
        # array for buttons
        self.btns = []
    
    def add_button(self, ctrl, tooltip=None, icon_name=None, label=""):
        # make button
        btn = self.ViewToggleButton(self, ctrl, tooltip=tooltip, icon_name=icon_name, label=label)
        self.btns.append(btn)
        # add to sizer
        self.sizer.addWidget(btn)
    
    def set_values(self, values):
        assert len(values) == len(self.btns), "When setting values for ViewToggle, there must be the same number of values as there are buttons."
        # set each button in order
        for btn, val in zip(self.btns, values):
            btn.setChecked(val)
        # refresh
        self.refresh_view()
    
    def refresh_view(self, evt=None):
        for btn in self.btns:
            # show/hide ctrl according to button state
            if btn.isChecked():
                btn.ctrl.show()
            else:
                btn.ctrl.hide()
