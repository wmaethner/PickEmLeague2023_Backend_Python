from datetime import datetime, timedelta

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
            jobs = scheduler.get_jobs()
            print(jobs)
        except Exception as e:
            print(e)
        return jobs


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
