import logging

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

app_logger = logging.getLogger("weather_info")
app_logger.addHandler(console_handler)
app_logger.setLevel(logging.DEBUG)

logging.getLogger('werkzeug').setLevel(logging.ERROR)

