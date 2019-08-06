import json
import falcon

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class AppError(Exception):
    status = falcon.HTTP_500
    title = 'Unknown Error'

    def __init__(self, message=None):
        self.message = message

    @staticmethod
    def handle(exception, req, res):
        res.status = exception.status
        meta = OrderedDict()
        meta["message"] = exception.title

        if exception.message:
            meta["message"] = exception.message

        res.body = json.dumps({"meta": meta})


class BadRequestError(AppError):
    status = falcon.HTTP_400
    title = 'Bad Request'


class DatabaseError(AppError):
    status = falcon.HTTP_500
    title = 'Database Error'


class NotSupportedError(AppError):
    def __init__(self, message=None, method=None, url=None):
        if method and url:
            self.message = "method: %s, url: %s" % (method, url)
        else:
            self.message = message


class NotFoundError(AppError):
    status = falcon.HTTP_404
    title = 'Not Found'


class UnauthorizedError(AppError):
    status = falcon.HTTP_401
    title = 'Unauthorized'


class ServerError(AppError):
    status = falcon.HTTP_500
    title = 'Server Error'
