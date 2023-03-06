from datetime import date


def process_data(**kwargs):
    file = open("/home/repl/workspace/processed_data-" +
                kwargs['ds'] + ".tmp", "w")
    file.write(f"Data processed on {date.today()}")
    file.close()
