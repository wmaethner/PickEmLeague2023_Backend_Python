from datetime import datetime, timedelta

from apscheduler.job import Job
from flask import jsonify
from flask_restx import Resource

from src.PickEmLeague import scheduler
from src.PickEmLeague.util.tasks import task

from ..core.base_namespace import BaseNamespace
from .business import send_push_message

scheduler_ns = BaseNamespace(name="scheduler", validate=True)
# scheduler_ns.add_models(
#     [summary_schema, summaries_model, pick_status_schema, pick_statuses_model]
# )


@scheduler_ns.route("/")
class AllJobs(Resource):
    # @scheduler_ns.marshal_with()
    def get(self):
        try:
            jobs: list[Job] = scheduler.get_jobs()
            # print(type(jobs[0]))
            # print(jobs)
            return jsonify([{"name": x.name, "next_run": x.next_run_time} for x in jobs])
        except Exception as e:
            print(e)


@scheduler_ns.route("/<string:id>")
class JobDetails(Resource):
    def post(self, id):
        scheduler.run_job(id)


@scheduler_ns.route("/<int:id>")
class Jobs(Resource):
    def get(self, id):
        job = scheduler.get_job(f"task-{id}")
        send_push_message("wQQNhQE2EIcoOJsMOUb_6j", "Push notification message")
        return job

    def post(self, id):
        try:
            scheduler.add_job(
                # f"task-{id}", task, args=[id], trigger="interval", seconds=10
                f"task-{id}",
                task,
                args=[id],
                trigger="date",
                run_date=(datetime.now() + timedelta(0, 5)),
            )
        except Exception as e:
            print(e)

        return True

    def delete(self, id):
        scheduler.remove_job(f"task-{id}")
        return True
