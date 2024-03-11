# import flask
# from flask import jsonify, make_response
# from .import db_session
# from .jobs import Jobs
#
# blueprint = flask.Blueprint(
#     'jobs_api',
#     __name__,
#     template_folder='templates'
# )
#
#
# @blueprint.route('/api/jobs')
# def get_jobs():
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).all()
#     return jsonify(
#         {
#             'jobs':
#                 [item.to_dict(only=('id', 'job', 'work_size', 'collaborators',\
#                                     'start_date', 'end_date', 'is_finished', 'category', 'team_leader', 'categories'))
#                  for item in jobs]
#         }
#     )
#
#
#
# @blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
# def get_one_jobs(jobs_id):
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).get(jobs_id)
#     if not jobs:
#         return make_response(jsonify({'error': 'Not found'}), 404)
#     return jsonify(
#         {
#             'jobs': jobs.to_dict(only=('id', 'job', 'work_size', 'collaborators',\
#                                     'start_date', 'end_date', 'is_finished', 'category', 'team_leader', 'categories'))
#         }
#     )