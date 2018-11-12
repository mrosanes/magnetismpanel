import sys
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel.taurusdevicepanel import TaurusDevicePanel

"""Taurus Application showing some attributes and commands from
the device txmautoprocessing useful for parallel acquisition and
preprocessing for magnetism experiments."""


class MagnetismWidget(TaurusDevicePanel):

    def __init__(self, parent=None, model="bl09/ct/txmautopreprocessing"):
        attr_filters = ["select", "target", "txm_file"]
        self.setAttributeFilters({model: attr_filters})
        command_filters = [('start', ()), ('end', ())]
        self.setCommandFilters({model: command_filters})

        TaurusDevicePanel.__init__(self, parent, model)

def main():
    app = TaurusApplication(app_name="MagnetismDevicePanel")
    w = MagnetismWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    #command_filters = {"Commands": "Init"}
    #w.setCommandFilters({model: command_filters})









