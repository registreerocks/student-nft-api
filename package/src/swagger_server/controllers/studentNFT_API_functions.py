from registree_auth import requires_auth, requires_scope
from .transaction_functions import (_get_identifying_id, _get_identifying_ids,
                                    _get_nft_id, _register_student)
from .health import _health_check


@requires_auth
@requires_scope('admin')
def register_student(body):
    return _register_student(body.get('ident_id'), body.get('ident_url'))

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_nft_id(**kwargs):
    if 'student_address' in kwargs:
        return {"ERROR": "Blockchain not supported."}, 409
    elif all (k in kwargs for k in ('ident_id','ident_url')):
        return _get_nft_id(kwargs['ident_id'])
    else:
        return {"ERROR": "Input parameters wrong"}, 409

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_identifying_id(nft_id):
    return _get_identifying_id(nft_id)

@requires_auth
@requires_scope('admin', 'lecturer', 'registree')
def get_identifying_ids(body):
    return _get_identifying_ids(body.get('nft_ids'))

def health_check():
    return _health_check()