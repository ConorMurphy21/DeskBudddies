from datetime import datetime
import os


class Schedule:

    def __init__(self, directory):
        self.directory = directory
        self.mem_sched = {}

    def add(self, uid, date):
        timestamp = datetime.timestamp(date)

        try:
            ids = self.mem_sched[timestamp]
        except KeyError:
            ids = self.mem_sched[timestamp] = self._read_file(timestamp)
        if uid not in ids:
            self.mem_sched[timestamp].append(uid)
            self._append_to_date(uid, timestamp)

    def remove(self, uid, date):
        timestamp = datetime.timestamp(date)

        try:
            ids = self.mem_sched[timestamp]
        except KeyError:
            ids = self.mem_sched[timestamp] = self._read_file(timestamp)

        if uid in ids:
            self.mem_sched[timestamp].remove(uid)
            self._update_date(timestamp)

    def get(self, date) -> list:
        timestamp = datetime.timestamp(date)

        try:
            ids = self.mem_sched[timestamp]
        except KeyError:
            ids = self.mem_sched[timestamp] = self._read_file(timestamp)
        return ids

    def get_week(self, date) -> list:
        dt_object = datetime.fromtimestamp(date)
        week_num = dt_object.strftime("%V")
        return

    def _load(self):
        pass

    # stores everything that's in memory
    def _store(self):
        pass

    # stores everything on given date
    def _update_date(self, timestamp):
        f = open(self.directory + str(timestamp) + ".txt", "w")
        f.writelines(self.mem_sched[timestamp])
        f.close()

    # appends just 1 item
    def _append_to_date(self, uid, timestamp):
        f = open(self.directory + str(timestamp) + ".txt", "a")
        f.write(uid + '\n')
        f.close()

    def _read_file(self, timestamp) -> list:
        # load in from disc
        filename = self.directory + str(timestamp) + ".txt"
        # create file if doesn't exist (a+)
        with open(filename, "a+") as f:
            f.seek(0)
            ids = f.readlines()

        return ids
