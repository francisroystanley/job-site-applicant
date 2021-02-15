from flask_login import current_user


def require_permission(required_permission):
    def wrapper(function):
        def ret_fn(self, *args, **kwargs):
            __userdata = current_user.info
            allowed = False
            for definition in __userdata['policy'].values():
                permissions = definition['action'].split(',')
                match = list(set(permissions) & set(required_permission))
                if len(match) > 0:
                    allowed = True

            if not allowed:
                http_stat = 403
                retval = {'message': 'No Permission'}
                return retval, http_stat
            else:
                return function(self, *args, **kwargs)
        return ret_fn
    return wrapper
