import datetime
import os


class Schedule:

    def __init__(self, directory):
        self.directory = directory
        self.mem_sched = {}

    def add(self, uid, date):
        try:
            ids = self.mem_sched[date]
        except KeyError:
            # load in from disc
            filename = self.directory + date + ".txt"

            with open(filename) as f:
                lines = f.readlines()

            ids = self.mem_sched[date] = lines
            if uid not in ids:
                self.mem_sched[date].append(uid)

    def remove(self, uid, date):
        try:
            ids = self.mem_sched[date]
        except KeyError:
            # load in from disc
            filename = self.directory + date + ".txt"

            with open(filename) as f:
                lines = f.readlines()

            ids = self.mem_sched[date] = lines
            if uid in ids:
                self.mem_sched[date].remove(uid)

    def get(self, date) -> list:
        try:
            ids = self[date]
        except KeyError:
            ids = self[date] = []
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
    def _update_date(self, date):
        pass

    # appends just 1 item
    def _append_to_date(self, uid, date):
        f = open("demofile2.txt", "a")
        f.write("Now the file has more content!")
        f.close()

        # open and read the file after the appending:
        f = open("demofile2.txt", "r")
        print(f.read())

    def _find_files(self, directory):
        result = []

        # Walking top-down from the root
        for root, dire, files in os.walk(directory):
            if self.directory in files:
                result.append(os.path.join(root, self.directory))

        if not result:
             # create new file
        return result
