import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def test_task():
    logger.info("Adding two numbers******************")
