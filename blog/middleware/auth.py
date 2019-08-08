from errors import UnauthorizedError
from log import get_logger
from utils.auth import decrypt_token


LOG = get_logger()


class AuthMiddleware(object):
    def process_request(self, req, res, resource=None):
        LOG.debug("Authorization: %s", req.auth)
        if req.auth is not None:
            token = decrypt_token(req.auth)
            if token is None:
                raise UnauthorizedError("Invalid auth token: %s" % req.auth)
            else:
                req.context["auth_user"] = token.decode("utf-8")
        else:
            req.context["auth_user"] = None
