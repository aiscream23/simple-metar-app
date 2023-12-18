from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui_2.ui", self)
        self.show()

        self.logbut.clicked.connect(self.login)
        self.generate.clicked.connect(lambda: self.report(self.inp_StationCode.text(), self.Tanggal.currentText(),
                                                          self.Jam.currentText(),self.Menit.currentText(),
                                                          self.inp_WindSpeed.text(),self.inp_WindDir.text(), self.inp_WindGust.text(),
                                                          self.inp_winvar1.text(), self.inp_winvar2.text(),
                                                          self.inp_Visibility.text(),self.inp_RVR_1.text(), self.inp_RVR_2.text(),
                                                          self.inp_PresentWeather.text(), self.inp_PresentWeather_1, self.inp_PresentWeather_2,
                                                          self.inp_CloudCoverage.currentText(), self.inp_CloudCoverage_2.text(),
                                                          self.inp_CloudCoverage_3, self.inp_CloudCoverage_4,
                                                          self.inp_CloudCoverage_5.currentText(), self.inp_CloudCoverage_6.text(),
                                                          self.inp_CloudCoverage_7, self.inp_CloudCoverage_8,
                                                          self.inp_CloudCoverage_9.currentText(), self.inp_CloudCoverage_10.text(),
                                                          self.inp_CloudCoverage_11, self.inp_CloudCoverage_12,
                                                          self.inp_Temperature.text(),self.inp_Dewpoint.text(),
                                                          self.inp_Pressure.text(),self.inp_SupplementaryInfo_2.text()
                                                          ))

        # Objek-objek yang akan diatur
        self.enabled_objects = [
            self.kiri, self.kanan, self.generate
        ]

    #Unlock password
    def set_objects_enabled(self, enabled=True):
        for obj in self.enabled_objects:
            obj.setEnabled(enabled)

    #Main run
    def login(self):
        if self.line_usr.text() == "test" and self.line_pass.text() =="pass":
            self.set_objects_enabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

    #Parameter input

    def report(self, inp_StationCode, Tanggal, Jam, Menit, inp_WindSpeed, inp_WindDir, inp_WindGust, inp_winvar1, inp_winvar2, inp_Visibility, inp_RVR_1, inp_RVR_2, inp_PresentWeather,inp_PresentWeather_1, inp_PresentWeather_2,inp_CloudCoverage, inp_CloudCoverage_2, inp_CloudCoverage_3, inp_CloudCoverage_4, inp_CloudCoverage_5, inp_CloudCoverage_6, inp_CloudCoverage_7, inp_CloudCoverage_8, inp_CloudCoverage_9, inp_CloudCoverage_10, inp_CloudCoverage_11, inp_CloudCoverage_12, inp_Temperature, inp_Dewpoint, inp_Pressure, inp_SupplementaryInfo):

        # inp_StationCode     = str(inp_StationCode)
        Tanggal             = int(Tanggal)
        Jam                 = int(Jam)
        Menit               = int(Menit)
        inp_WindSpeed       = int(inp_WindSpeed)
        inp_WindDir         = int(inp_WindDir)

        #Create Metar
        metar = f"METAR {inp_StationCode} {Tanggal:02d}{Jam:02d}{Menit:02d}Z"
        if inp_WindSpeed <= 3 and inp_WindDir >= 9000:
            metar += f"VRB {inp_WindSpeed: 02d}KT"
        elif inp_WindSpeed >= 3:
            try:
                inp_WindGust = int(inp_WindGust)
                metar += f" {inp_WindDir:03d}{inp_WindSpeed:02d}G{inp_WindGust}KT"
            except:
                pass
            metar += f" {inp_WindDir:03d}{inp_WindSpeed:02d}KT"
        elif inp_WindSpeed <=1 and inp_WindDir <= 9000:
            metar += " 00000KT "
        if inp_winvar1 and inp_winvar2:
            metar += f" {inp_winvar1}V{inp_winvar2}"
        else:
            pass
        if int(inp_Visibility) >= 10000:
            metar += f" 9999"
        else:
            metar += f" {inp_Visibility}"
        try:
            metar += f" {inp_RVR_1}/{inp_RVR_2}"
        except:
            pass
        try:
            if self.inp_PresentWeather_1.isChecked() :
                metar += f" -{inp_PresentWeather}"
            elif self.inp_PresentWeather_2.isChecked() :
                metar += f" +{inp_PresentWeather}"
            else:
                metar += f" {inp_PresentWeather}"
        except:
            pass
        try:
            metar += f" {inp_CloudCoverage}{inp_CloudCoverage_2}"
            if inp_CloudCoverage_3.isChecked():
                metar += f" {inp_CloudCoverage}{inp_CloudCoverage_2}CB"
            elif inp_CloudCoverage_4.isChecked():
                metar += f" {inp_CloudCoverage}{inp_CloudCoverage_2}TCU"
            else:
                pass
        except:
            pass
        try:
            metar += f" {inp_CloudCoverage_5}{inp_CloudCoverage_6}"
            if inp_CloudCoverage_7.isChecked():
                metar += f" {inp_CloudCoverage_5}{inp_CloudCoverage_6}CB"
            elif inp_CloudCoverage_8.isChecked():
                metar += f" {inp_CloudCoverage_5}{inp_CloudCoverage_6}TCU"
            else:
                pass
        except:
            pass
        try:
            metar += f" {inp_CloudCoverage_9}{inp_CloudCoverage_10}"
            if inp_CloudCoverage_11.isChecked():
                metar += f" {inp_CloudCoverage_9}{inp_CloudCoverage_10}CB"
            elif inp_CloudCoverage_12.isChecked():
                metar += f" {inp_CloudCoverage_9}{inp_CloudCoverage_10}TCU"
            else:
                pass
        except:
            pass
        metar += f" {inp_Temperature}/{inp_Dewpoint} Q{inp_Pressure}"
        try:
            metar += f" {inp_SupplementaryInfo}"
        except:
            pass

        message = QMessageBox()
        message.setDetailedText(metar)
        message.setInformativeText(metar)
        message.exec_()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()