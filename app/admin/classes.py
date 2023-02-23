from flask import url_for
from app import db
from app.models import Storylet, Branch, Result

class PageResult():
    def __init__(self, data, page=1, number=20):
        self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, number]))
        self.full_listing = [self.data[i:i+number] for i in range(0, len(self.data), number)]

    def __iter__(self):
        for i in self.full_listing[self.page-1]:
            yield i

    def __repr__(self):
        return url_for('admin.users', pagenum=self.page+1)

class Tag():
    def __init__(self, name, user):
        if name == None:
            self.name = "Unorganized"
        else:
            self.name = name
        if user == 0:
            self.q_list = db.session.query(Storylet).filter(Storylet.tag == name).order_by(Storylet.title).all()
        else:
            self.q_list = db.session.query(Storylet).filter(Storylet.user_id == user).filter(Storylet.tag == name).order_by(Storylet.title).all()

    def __lt__(self, other):
        return self.name < other.name


def defaultStorylet():
    return Storylet(
        title="Untitled",
        image="black.png",
        description=None,
        deck="Always",
        area="All",
        urgency="Normal",
        order=0,
        notes=None,
        escapable=True,
        tag=None
    )
        
def defaultBranch():
    return Branch(
        title="Untitled",
        image="black.png",
        description=None,
        button_text="Go",
        notes=None,
        order=0,
        action_cost=0
    )

def defaultResult():
    return Result(
        title="Untitled",
        description=None,
        next_id=0,
        type="General",
        random_weight=0,
        area_change="Temp",
        notes=None
    )

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png'}