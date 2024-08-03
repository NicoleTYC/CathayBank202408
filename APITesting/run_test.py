import pytest
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"test_log_{timestamp}.log"
report_file = f"report_{timestamp}.html"

pytest.main([
    '--log-file', log_file,
    '--log-file-level', 'INFO',
    '--html', report_file,
    '--self-contained-html'
])
