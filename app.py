import falcon

from db import init_session
from blog.resources import BlogDetailResource


middleware = []


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(
            args, kwargs, middleware=middleware
        )

        # Add routes
        app.add_route('/blogs', BlogListResource())
        app.add_route('/blogs/{blog_id}', BlogDetailResource())


init_session()

app = App()
