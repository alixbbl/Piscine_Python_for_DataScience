# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 1 *******************

from datetime import datetime

now = datetime.now()
old_date_str = "Jan 1 1970"
old_date = datetime.strptime(old_date_str, "%b %d %Y")
current_date = datetime.today()
time_since = current_date - old_date
time_since_seconds = (
    time_since.total_seconds()
)  # utiliser la methode de classe ici, pas dans les {}
formatted_date = current_date.strftime("%b %d %Y")

number = time_since_seconds
formatted_scientific = f"{number:.2e}"

print(
    f"Seconds since January 1, 1970: { time_since_seconds } or\
          { formatted_scientific } in scientific notation"
)

print(formatted_date)
