class Schedule:

    def __init__(self):
        pass

    def add(self, uid, date):
        pass

    def remove(self, uid, date):
        pass

    def get(self, date) -> list:
        pass

    def get_week(self, date) -> list:
        pass

    def _load(self):
        pass

    # stores everything that's in memory
    def _store(self):
        pass

    # stores everything on given date
    def _update_date(self, date):
        pass

    # appends just 1 item
    def _append_to_date(self, uid, date):
        pass
