import json

import falcon

from resources import BaseResource
from blog.models import BlogEntry


class BlogDetailResource(BaseResource):
    def on_get(self, req, resp, blog_id):
        session = req.context.get('session')
        #if not session:
            # raise error

        blog_entry = BlogEntry.find_one(session, blog_id)
        self.on_success(res, blog_entry.to_dict())
        #except NoResultFound:
        #    raise UserNotExistsError("user id: %s" % user_id)

    def on_put(self, req, resp, blog_id):
        session = req.context.get('session')
        #if not session:
            # raise error

        blog_entry = BlogEntry.find_one(session, blog_id)
        #except NoResultFound:
        #    raise UserNotExistsError("user id: %s" % user_id)

        blog_data = req.context.get('data')
        # if not blog_data:
        #    raise error

        blog_entry.find_update(session, blog_id, blog_data)
        session.commit()

        self.on_success(res, None)

    def on_delete(self, req, resp, blog_id):
        session = req.context.get('session')
        #if not session:
        #    raise error

        blog_entry = BlogEntry.find_one(session, blog_id)

        blog_entry.delete()
        session.commit()

        self.on_success(res, None)


class BlogListResource(BaseResource):
    def on_get(self, req, resp):
        session = req.context.get('session')
        blog_entries = session.query(BlogEntry).all()
        if blog_entries:
            obj = [blog_entry.to_dict() for blog_entry in blog_entries]
            self.on_success(res, obj)
        #else:
        #    raise AppError()

    def on_post(self, req, resp):
        session = req.context.get('session')
        #if not session:
            # raise error

        blog_data = req.context.get('data')
        #if not blog_data:
            # raise error

        blog_entry = BlogEntry(blog_data)
        session.add(blog_entry)
        session.commit()

        self.on_success(res, None)
