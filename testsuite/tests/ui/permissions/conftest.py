import pytest
from threescale_api.resources import ProviderAccountUser

from testsuite.ui.permissions import Sections
from testsuite.ui.views.admin.settings.user import UserDetailView


class UserPermissions:
    def __init__(self,
                 user: ProviderAccountUser,
                 admin=None,
                 sections: [Sections] = None,
                 products: [int] = None):
        self.user = user
        self.admin = admin
        self.sections = sections
        self.products = products


@pytest.fixture(scope='module')
def admin_user(custom_admin_login, navigator, provider_account_user):
    custom_admin_login()
    provider_account_user.activate()
    user_view = navigator.open(UserDetailView, user=provider_account_user)
    user_view.set_admin_role()
    user_view.update()
    return provider_account_user


@pytest.fixture(scope='module')
def looser_member_user(custom_admin_login, navigator, provider_account_user):
    provider_account_user.activate()
    return provider_account_user
