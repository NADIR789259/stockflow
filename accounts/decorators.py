from django.contrib.auth.decorators import user_passes_test


def is_owner(user):
    """
    Returns True for the Owner role: superusers, or any user in the
    'Owner' group. Safe to call with an AnonymousUser (checks
    is_authenticated first).
    """
    if not user.is_authenticated:
        return False
    return user.is_superuser or user.groups.filter(name="Owner").exists()


# Use this decorator on any view that only the Owner should be able to
# reach (e.g. adding/editing products, viewing reports). Staff users who
# try to access it are redirected to the login page (same behaviour as
# @login_required), preserving `?next=` so they land back here after
# logging in as an Owner.
owner_required = user_passes_test(is_owner, login_url="/login/")
