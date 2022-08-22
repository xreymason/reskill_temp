

class INST:
    def __init__(self, visa_resource:str):
        self.visa_resource = visa_resource
        self._command = ""

    @property
    def Freq(self) -> float:
        """Gets the currently set frequency in Hz

        :return: Frequency in Hz
        :rtype: float
        """
        self._command = "SOUR:FREQ?"
        return float()
    @Freq.setter
    def Freq(self, Hz:float):
        """Sets the frequency in Hz

        :param Hz: Frequency in Hz
        :type Hz: float
        """
        self._command = "SOUR:FREQ " + str(Hz)