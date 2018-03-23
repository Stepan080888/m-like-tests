# -*- coding: utf-8 -*-
import pytest
from model.postaldata import Postaldata
from fixture.application import Application

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_req_user_data(app):
    app.session.log_in(username="no_exp2", password="Keplercode344")
    app.fill_in_user_data_form(Postaldata(country="Ukraine", name="Ilyk Stepan", street="Lazarenka str", num_house="23", city="Lviv", state="Lviv reg", zip="82100", phone="0938211673"))
    app.session.log_out()

def test_add_all_user_data(app):
    app.session.log_in(username="no_exp2", password="Keplercode344")
    app.fill_in_user_data_form(Postaldata(country="Ukraine", name="Ilyk Stepan", street="Lazarenka str", num_house="23", city="Lviv", state="Lviv reg", zip="82100", phone="0938211673", sec_code="93317", address_det="lvivska"))
    app.session.log_out()







