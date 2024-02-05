#!/usr/bin/python3
class LockedClass:
    """a class LockedClass with no class or object attribute,
    that prevents the user from dynamically
     creating new instance attributes,"""
    __slots__ = ['first_name']
