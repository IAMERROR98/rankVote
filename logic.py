from PyQt6.QtWidgets import *
from gui import *
import csv

# sunday you need to fix this crap us before monday I AM SIEROUS!
# NOTE PROGRAME ONLY WORKS IF THERE IS 5 OR MORE VOTES
class Logic(QMainWindow, Ui_MainWindow):
    VOTING_VALUE = 10
    VOTING_INT = 1

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.__candidates = ['Elephant', 'Donkey', 'Fox', 'Turkey']
        self.__ElVotes = self.buttonGroupEl.checkedId()
        self.__DnVotes = self.buttonGroupDn.checkedId()
        self.__FxVotes = self.buttonGroupFx.checkedId()
        self.__TkyVotes = self.buttonGroupTky.checkedId()
        self.__ballots = []
        self.__elephant = 0
        self.__donkey = 0
        self.__fox = 0
        self.__turkey = 0
        #change this
        self.__totals = dict(elephant=self.__elephant, donkey=self.__donkey, fox=self.__fox, turkey=self.__turkey)
        self.__eliminated_animals = set()
        self.__vround = 2
        self.__max_vote = max(self.__totals, key=lambda key: self.__totals[key])
        self.__min_vote = min(self.__totals, key=lambda key: self.__totals[key])

        self.castVote.clicked.connect(lambda: self.grab_votes())
        self.compileVotes.clicked.connect(lambda: self.tally())


    def grab_votes(self) -> None:
        """
        This grabs the votes from the gui and collects the rankings from each
        voter
        :return:
        """
        elVotes = self.buttonGroupEl.checkedId()
        dnVotes = self.buttonGroupDn.checkedId()
        fxVotes = self.buttonGroupFx.checkedId()
        tkyVotes = self.buttonGroupTky.checkedId()
        user_value = elVotes + dnVotes + fxVotes + tkyVotes
        if user_value != Logic.VOTING_VALUE:
            print(user_value)
            print('no')

        else:
            ballot = dict(elephant=elVotes, donkey=dnVotes, fox=fxVotes, turkey=tkyVotes)
            print(len(ballot))
            self.__ballots.append(ballot)

            print('yes')
            print(self.__ballots)

        # add excel

    def tally(self) -> None:
        """
        This method tallies the votes together by finding the party with the least votes and distributing
        them to other parties.

        Note: method WILL assign votes to expired parties.

        DO NOT USE THIS PROGRAM IN REAL WORLD ELECTIONS!
        :return:
        """
        #field_names = ['Elephant', 'donkey', 'fox', 'turkey']
        #with open('votes.csv', 'w') as file:
            #writer = csv.DictWriter(file, fieldnames=field_names)
            #writer.writeheader()
            #writer.writerows(self.__ballots)

        f = False
#        eliminated_animals = set()
        for i in self.__ballots:
#           if i[self.__ballots] == 1:
            if i["elephant"] == 1:
                self.__elephant += 1
            elif i["donkey"] == 1:
                self.__donkey += 1
            elif i["fox"] == 1:
                self.__fox += 1
            elif i["turkey"] == 1:
                self.__turkey += 1
        self.setter()

        while f == False:

            if float(i[self.__max_vote]) > sum(self.__totals.values()) / 2:
                print(self.__max_vote)
                f = True
                break

            for i in self.__ballots:
                if i[self.__min_vote] == 1:
                    minList = list(i)



            for i in minList:
                if i['elephant'] == self.__vround:
                    self.__elephant += 1
                elif i["donkey"] == self.__vround:
                    self.__donkey += 1
                elif i["fox"] == self.__vround:
                    self.__fox += 1
                elif i["turkey"] == self.__vround:
                    self.__turkey += 1

                self.__vround += 1
            self.setter()


    def getter(self) -> dict:
        return self.__totals

    def setter(self) -> None:
        self.__totals = dict(elephant=self.__elephant, donkey=self.__donkey, fox=self.__fox, turkey=self.__turkey)

