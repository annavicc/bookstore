from flask_restx import abort


class BookReservedError(Exception):
    def __init__(self, *args):
        self.message = 'This book has been already reserved.'

    def _str(self):
        return 'BookReservedError: {0} '.format(self.message)

    def abort_message(self, code=400):
        abort(code, message=self._str())


class NotFoundError(Exception):
    def __init__(self, *args):
        self.message = 'This {0} has not been found.'.format(args[0])

    def _str(self):
        return 'NotFoundError: {0} '.format(self.message)

    def abort_message(self, code=404):
        abort(code, message=self._str())
