import functools
from enum import Enum

from threescale_api.resources import ProviderAccountUser, ProviderAccountUsers
from widgetastic.widget import View


class Sections(Enum):
    PORTAL = "portal"
    BILLING = "finance"
    SETTINGS = "settings"
    PARTNERS = "partners"
    ANALYTICS = "monitoring"
    APP_PLANS = "plans"
    POLICY = "policy_registry"

    def __get__(self, obj, owner):
        return self.value


META_ATTR = 'meta_permissions'


class Permissions:
    role: str
    sections: [Sections]
    products: [int]


class ViewAccess:
    def __init__(self, obj, tag):
        self.obj = obj
        self.tag = tag
        self.meta_attr = META_ATTR
        setattr(obj, self.meta_attr, self.tag)
        functools.update_wrapper(self, obj)

    def __get__(self, obj, owner):
        widget_obj = self.obj.__get__(obj, owner)
        setattr(widget_obj, self.meta_attr, self.tag)
        return widget_obj

    def __call__(self, *args, **kwargs):
        widget_obj = self.obj.__call__(*args, **kwargs)
        return widget_obj


def admin():
    def _wrap(obj):
        return ViewAccess(obj, "admin")
    return _wrap


def dev_portal():
    def _wrap(obj):
        return ViewAccess(obj, Sections.PORTAL)
    return _wrap


def billing():
    def _wrap(obj):
        return ViewAccess(obj, Sections.BILLING)
    return _wrap


def settings():
    def _wrap(obj):
        return ViewAccess(obj, Sections.SETTINGS)
    return _wrap


def partners(services: [int]):
    def _wrap(obj):
        return ViewAccess(obj, Sections.PARTNERS)
    return _wrap


def analytics(services: [int]):
    def _wrap(obj):
        return ViewAccess(obj, Sections.ANALYTICS)
    return _wrap


def app_plans(services: [int]):
    def _wrap(obj):
        return ViewAccess(obj, Sections.APP_PLANS)
    return _wrap


def policy():
    def _wrap(obj):
        return ViewAccess(obj, Sections.POLICY)
    return _wrap


# class ViewAccessValidator:
#     def __init__(self, ):



def assert_perm(view: View, user: ProviderAccountUsers):
    permissions = user.permissions_read()['permissions']
    sections = permissions['allowed_sections']
    a = getattr(view, META_ATTR)
    if permissions['role'] in a:  # This applies only for admin role
        assert view.is_displayed
    if list(set(a).intersection([el.value for el in Sections])):
        assert view.is_displayed


# class Farts:
#     def __init__(self, obj, *args, **kwargs):
#         self.obj = obj
#
#     def __set_name__(self, owner, name):
#         setattr(owner, 'fartisimo', 'aaaaaaaa')
#         print("aaa")
#
#     def __get__(self, obj, owner):
#         return self.obj.__get__(obj, owner)
#
#     def __call__(self, method, *args, **kwargs):
#         return self.obj(*args, **kwargs)

# def plans(obj, *args, **kwargs):
#     # obj.fart = Permissions.PLAN
#
#     # return process_parameters(obj, fatr= "aaa")
#     # if WidgetDescriptor
#     obj.fart = "aaaa"
#     # obj.extra.fart = "a"
#     # obj.kwargs['chuj'] = "test"
#     yield obj
#     obj.fart = "aaaa"


