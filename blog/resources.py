import json

import falcon

from errors import ServerError, NotFoundError, BadRequestError
from resources import BaseResource
from blog.models import BlogEntry


class BlogDetailResource(BaseResource):
    def on_get(self, req, resp, blog_id):
        session = self.get_session(req)

        try:
            blog_entry = BlogEntry.find_one(session, blog_id)
            self.on_success(res, blog_entry.to_dict())
        except NoResultFound:
            raise NotFoundError('Blog ID {} not found.'.format(blog_id))

    def on_put(self, req, resp, blog_id):
        session = self.get_session(req)

        try:
            blog_entry = BlogEntry.find_one(session, blog_id)
        except NoResultFound:
            raise NotFoundError('Blog ID: {} not found.'.format(blog_id))

        blog_data = req.context.get('data')
        if not blog_data:
            raise BadRequestError('No data received.')

        blog_entry.find_update(session, blog_id, blog_data)
        session.commit()

        self.on_success(res, None)

    def on_delete(self, req, resp, blog_id):
        session = self.get_session(req)

        try:
            blog_entry = BlogEntry.find_one(session, blog_id)
        except NoResultFound:
            raise NotFoundError('Blog ID: {} not found.'.format(blog_id))

        blog_entry.delete()
        session.commit()

        self.on_success(res, None)


class BlogListResource(BaseResource):
    def on_get(self, req, resp):
        session = self.get_session(req)

        blog_entries = session.query(BlogEntry).all()
        if blog_entries:
            obj = [blog_entry.to_dict() for blog_entry in blog_entries]
        else:
            obj = [{}]

        self.on_success(res, obj)

    def on_post(self, req, resp):
        session = self.get_session(req)

        blog_data = req.context.get('data')
        if not blog_data:
            raise BadRequestError('No data received.')

        blog_entry = BlogEntry(blog_data)
        session.add(blog_entry)
        session.commit()

        self.on_success(res, None)
