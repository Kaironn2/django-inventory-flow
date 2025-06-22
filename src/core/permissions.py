from typing import Literal, TypedDict, cast

from django.conf import settings

Action = Literal['view', 'add', 'change', 'delete']


class AppPermissions(TypedDict):
    view: str
    add: str
    change: str
    delete: str


class PermissionsDict(TypedDict):
    brands: AppPermissions
    categories: AppPermissions
    inflows: AppPermissions
    outflows: AppPermissions
    products: AppPermissions
    suppliers: AppPermissions


class ProjectAppsDict(TypedDict):
    brands: Literal['brand']
    categories: Literal['category']
    inflows: Literal['inflow']
    outflows: Literal['outflow']
    products: Literal['product']
    suppliers: Literal['supplier']


def get_crud_permissions() -> PermissionsDict:
    actions: list[Action] = ['view', 'add', 'change', 'delete']
    apps = cast(ProjectAppsDict, settings.PROJECT_APPS)

    permissions = {}
    for app, model in apps.items():
        permissions[app] = {
            action: f'{app}.{action}_{model}'
            for action in actions
        }
    return cast(PermissionsDict, permissions)


default_permissions: PermissionsDict = get_crud_permissions()
