import re
from collections import Counter

class NationalPark:

    def __init__(self, name):
        self.name = name

    #national park property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name needs to be string")
        elif len(new_name) < 3:
            raise Exception("Name must be at least two characters")
        elif hasattr(self, 'name'):
            raise Exception("Name can't be reset")
        else:
            self._name = new_name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        if len(self.trips()):
            return len(self.trips())
        else:
            return 0

    def best_visitor(self):
        if len([trip.visitor for trip in self.trips()]):
            occurence_count = Counter([trip.visitor for trip in self.trips()])
            return occurence_count.most_common(1)[0][0]
        else:
            return 0



class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        type(self).all.append(self)

    #visitor property
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, vis_cls):
        if isinstance(vis_cls, Visitor):
            self._visitor = vis_cls

    #national park property
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, new_park):
        if isinstance(new_park, NationalPark):
            self._national_park = new_park

    #start date property
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, new_date):
        pattern = r"\w+\s+\d+(st|nd|rd|th)"
        if not isinstance(new_date, str):
            raise Exception("Date must be a string")
        elif len(new_date) < 7:
            raise Exception("Date length must be more than 7 characters")
        elif not re.match(pattern, new_date):
            raise Exception("Date must match 'September 1st' pattern")
        else:
            self._start_date = new_date

    #end date
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, new_date):
        pattern = r"\w+\s+\d+(st|nd|rd|th)"
        if not isinstance(new_date, str):
            raise Exception("Date must be a string")
        elif len(new_date) < 7:
            raise Exception("Date length must be more than 7 characters")
        elif not re.match(pattern, new_date):
            raise Exception("Date must match 'September 1st' pattern")
        else:
            self._end_date = new_date



class Visitor:

    def __init__(self, name):
        self.name = name

    #name property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        elif len(new_name) < 1 or len(new_name) > 15 :
            raise Exception("Name must be between 1 and 15 characters")
        else:
            self._name = new_name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        pass
