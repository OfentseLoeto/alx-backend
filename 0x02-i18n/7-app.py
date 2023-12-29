#!/usr/bin/env python3
"""
Determine the users preferred time zone based on priority.
"""
from flask_babel import timezone_selector
import pytz


@babel.timezone_selector
def get_timezone():
    """
    Determine the user's preferred time zone based on priority.

    The order of priority is:
    1. Time zone from URL parameters
    2. Time zone from user settings
    3. Default to UTC

    Returns:
        str: The determined time zone.
    """
    # Priority 1: Time zone from URL parameters
    user_timezone = request.args.get('timezone')
    if user_timezone:
        try:
            # Validate if it's a valid time zone
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass  # Invalid time zone, proceed to the next priority

    # Priority 2: Time zone from user settings
    if g.user and 'timezone' in g.user:
        try:
            # Validate if it's a valid time zone
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass  # Invalid time zone, proceed to the next priority

    # Priority 3: Default to UTC
    return 'UTC'
