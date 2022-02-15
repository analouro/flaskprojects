from asyncio import tasks
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Task

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        test_task = Task(name_task="Test task")
        db.session.add(test_task)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    # def test_read_get(self):
    #     response = self.client.get(url_for('read'))
    #     self.assertEqual(response.status_code, 200)