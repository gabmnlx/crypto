import apscheduler.schedulers.background
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_extract

def start():
    scheduler = apscheduler.schedulers.background.BackgroundScheduler({'apscheduler.job_defaults.max_instances': 2})
    scheduler.add_job(schedule_extract, 'interval', seconds=1)
    scheduler.start()