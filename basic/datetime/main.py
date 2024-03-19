from datetime import datetime, timezone

current_utc_time = datetime.now(timezone.utc)

milliseconds = int(current_utc_time.timestamp() * 1000)

print(milliseconds)
