from functools import wraps

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


def feature_required(feature):
    def decorator(view):
        @wraps(view)
        def require_feature(request, *args, **kwargs):
            if request.user.features[feature]:
                return view(request, *args, **kwargs)
            messages.warning(request, _("Feature not available"))
            return HttpResponseRedirect("/")

        return require_feature

    return decorator


class FEATURES:
    BOOKKEEPING = "bookkeeping"
    CONTROLLING = "controlling"
    DEALS = "deals"
    FOREIGN_CURRENCIES = "foreign_currencies"
    GLASSFROG = "glassfrog"
    LABOR_COSTS = "labor_costs"
    SKIP_BREAKS = "skip_breaks"


bookkeeping_only = feature_required(FEATURES.BOOKKEEPING)
controlling_only = feature_required(FEATURES.CONTROLLING)
deals_only = feature_required(FEATURES.DEALS)
labor_costs_only = feature_required(FEATURES.LABOR_COSTS)


KNOWN_FEATURES = {getattr(FEATURES, attr) for attr in dir(FEATURES) if attr.isupper()}


class UnknownFeature(Exception):
    pass
