#!/usr/bin/env python3

import re


class Panda:

    def __init__(self, name, email, gender):

        self._name = name
        if gender is not ('male' or 'female'):
            print("panda's can't be genderfluid...")
        else:
            self._gender = gender
        # Let's not get overly complicated here.
        if re.fullmatch('\w+@\w+\.\w+', email):
            self._email = email
        else:
            print('pandamail not valid')

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        if self._gender == 'male':
            return True
        else:
            return False

    def isFemale(self):
        return not self.isMale()

    def __str__(self):
        return "{} is a {} panda, email: {}".format(self._name, self._gender, self._email)

    def __eq__(self, other):
        if isinstance(other, Panda):
            return str(self) == str(other)
        else:
            return False

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return self.__str__()


class SocialNetwork:

    def __init__(self):
        pass
