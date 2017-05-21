import pytest

from scotch import Model


class TestScotchModel(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_instantiate_empty_model(self):

        model = Model()

        # Models instantiated with no JSON model file should have
        # default ( mostly empty ) variables
        assert model.variables == []
        assert model.initial_conditions == {}
        assert model.parameters == {}
        assert model.events == []
        assert model.default_algorithm == "gillespie"

        # These models won't have their derived variables because
        # model.build() will never have been called
        with pytest.raises(AttributeError):
            model._n_variables
        with pytest.raises(AttributeError):
            model._n_events
        with pytest.raises(AttributeError):
            model._variables_map
