from app.extensions import db


class ResourceMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.remove(self)
        db.session.commit()
