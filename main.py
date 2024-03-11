from flask import Flask, render_template, redirect
from data import db_session, news_api, jobs_api
from data.jobs import Jobs, Category
from data.add_job import AddJobForm
from flask_restful import reqparse, abort, Api, Resource
from data.news_resources import NewsResource, NewsListResource
from data.user_resources import UsersResource, UsersListResource



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
# для списка объектов
api.add_resource(NewsListResource, '/api/v2/news')
# для одного объекта
api.add_resource(NewsResource, '/api/v2/news/<int:news_id>')

# для списка объектов
api.add_resource(UsersResource, '/api/v2/users')
# для одного объекта
api.add_resource(UsersListResource, '/api/v2/users/<int:users_id>')



def main():
    # db_session.global_init("db/mars_explorer.sqlite")
    # session = db_session.create_session()

    db_session.global_init("db/mars_explorer.sqlite")
    # app.register_blueprint(news_api.blueprint)
    # app.register_blueprint(jobs_api.blueprint)
    app.run()







if __name__ == '__main__':
    main()
