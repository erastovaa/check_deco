def takes(*types):
    def decorator(f):
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                if isinstance(a, t) is False:
                    raise TypeError()
            return f(*args, **kwds)
        return new_f
    return decorator
