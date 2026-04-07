import os

import pytest
from pytestarch import DiagramRule, get_evaluable_architecture, LayeredArchitecture, LayerRule, Rule

TESTS_PATH = os.path.abspath(os.path.dirname(__file__))
SRC_PATH = os.path.abspath(os.path.join(TESTS_PATH, '..', 'src'))
APP_PATH = os.path.join(SRC_PATH, 'app')
PUML_PATH = os.path.join(TESTS_PATH, 'architecture.puml')


@pytest.fixture(scope='session')
def evaluable():
    return get_evaluable_architecture(
        root_path=SRC_PATH,
        module_path=APP_PATH,
        exclusions=('*test*', '*__pycache__*'),
    )


def test_models_should_not_import_any_internal_module(evaluable):
    rule = (
        Rule()
        .modules_that()
        .are_named('src.app.models')
        .should_not()
        .import_modules_that()
        .are_sub_modules_of('src.app')
    )
    rule.assert_applies(evaluable)


def test_service_should_not_import_routes(evaluable):
    rule = (
        Rule()
        .modules_that()
        .are_named('src.app.service')
        .should_not()
        .import_modules_that()
        .are_named('src.app.routes')
    )
    rule.assert_applies(evaluable)


def test_service_should_not_import_main(evaluable):
    rule = (
        Rule()
        .modules_that()
        .are_named('src.app.service')
        .should_not()
        .import_modules_that()
        .are_named('src.app.main')
    )
    rule.assert_applies(evaluable)


def test_routes_should_not_import_main(evaluable):
    rule = (
        Rule()
        .modules_that()
        .are_named('src.app.routes')
        .should_not()
        .import_modules_that()
        .are_named('src.app.main')
    )
    rule.assert_applies(evaluable)


def test_layered_architecture(evaluable):
    arch = (
        LayeredArchitecture()
        .layer('routes')
        .containing_modules(['src.app.routes'])
        .layer('service')
        .containing_modules(['src.app.service'])
        .layer('models')
        .containing_modules(['src.app.models'])
    )

    routes_only_access_service_and_models = (
        LayerRule()
        .based_on(arch)
        .layers_that()
        .are_named('routes')
        .should_only()
        .access_layers_that()
        .are_named(['service', 'models'])
    )
    routes_only_access_service_and_models.assert_applies(evaluable)

    service_should_not_access_routes = (
        LayerRule()
        .based_on(arch)
        .layers_that()
        .are_named('service')
        .should_not()
        .access_layers_that()
        .are_named('routes')
    )
    service_should_not_access_routes.assert_applies(evaluable)

    models_should_not_access_any_layer = (
        LayerRule()
        .based_on(arch)
        .layers_that()
        .are_named('models')
        .should_not()
        .access_layers_that()
        .are_named(['routes', 'service'])
    )
    models_should_not_access_any_layer.assert_applies(evaluable)


def test_diagram_matches_actual_architecture(evaluable):
    DiagramRule(should_only_rule=True).from_file(PUML_PATH).assert_applies(evaluable)
