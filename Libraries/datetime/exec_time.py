from datetime import datetime
import time

start = datetime.now()

# simulate a task
time.sleep(2.0004576)

end = datetime.now()
print("Execution Time:", end - start)