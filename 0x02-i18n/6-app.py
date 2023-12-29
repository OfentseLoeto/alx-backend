#!/usr/bin/env python3
"""
Determine the user's preferred locale based on priority.
"""
from flask import g, request


def get_locale():
    """
    Determine the user's preferred locale based on priority.

    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The determined locale code.
    """
    # Priority 1: Locale from URL parameters
    user_locale = request.args.get('locale')
    if user_locale:
        return user_locale

    # Priority 2: Locale from user settings
    if g.user and 'locale' in g.user:
        return g.user['locale']

    # Priority 3: Locale from request header
    request_locale = request.headers.get('Accept-Language')
    if request_locale:
        # Extract the first language code from the Accept-Language header
        return request_locale.split(',')[0].split(';')[0]

    # Priority 4: Default locale
    return 'UTC'
