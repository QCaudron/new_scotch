import json
import os

import numpy as np


class Model(object):
    """Scotch continuous-time Markov chain model."""

    def __init__(self, filename=None):

        if filename is None:
            self.variables = []
            self.initial_conditions = {}
            self.parameters = {}
            self.events = []
            self.default_algorithm = "gillespie"

        else:

            with open(filename, "r") as f:
                model = json.load(f)

            self.variables = model["variables"]
            self.initial_conditions = model["initial_conditions"]
            self.parameters = model["parameters"]
            self.events = model["events"]
            self.default_algorithm = model.get("default_algorithm", "gillespie")
            self.build()

    def build(self, silent=False):

        self._n_variables = len(self.variables)
        self._n_events = len(self.events)
        self._variables_map = {variable: idx for idx, variable in enumerate(self.variables)}
        #self.construct_transition_matrix()

    def _construct_transition_matrix(self):

        transition_matrix = np.zeros((self._n_variables, self._n_events))
        for idx, event in enumerate(self.events):
            pass
