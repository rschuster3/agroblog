import falcon

from blog.resources import BlogDetailResource
from blog.middleware.auth import AuthMiddleware
from blog.middleware.session_manager import DatabaseSessionMiddleware
from db import init_session
from errors import AppError


middleware = [AuthMiddleware, DatabaseSessionMiddleware]


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(
            args, kwargs, middleware=middleware
        )

        # Add routes
        app.add_route('/blogs', BlogListResource())
        app.add_route('/blogs/{blog_id}', BlogDetailResource())

        # Error handling
        self.add_error_handler(AppError, AppError.handle)



init_session()

app = App()
