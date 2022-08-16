import pytest

from testsuite.ui.permissions import Sections, assert_perm
from testsuite.ui.views.admin.product import ProductsView
from testsuite.ui.views.admin.product.product import ProductNewView, ProductEditView, ProductDetailView


@pytest.mark.parametrize("view", [
    pytest.param(ProductsView),
    pytest.param(ProductNewView),
    pytest.param(ProductDetailView),
    pytest.param(ProductEditView),
])
def test_member_role(custom_admin_login, navigator, looser_member_user, account_password, view):
    print(Sections.POLICY)
    custom_admin_login(looser_member_user["username"], account_password)
    nav = navigator.open(view)
    # assert
    assert_perm(nav, looser_member_user)
    print("Aaa")
