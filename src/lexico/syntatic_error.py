from .analysis_error import AnalysisError

class SyntaticError(AnalysisError):

    def __init__(self, msg, position = None):

        super().__init__(msg, position)
