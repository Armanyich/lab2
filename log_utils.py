from datetime import datetime
import logging

def generate_log_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"errors_{timestamp}.log"

log_filename = generate_log_filename()

logging.basicConfig(
    level=logging.ERROR,
    filename=log_filename,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
