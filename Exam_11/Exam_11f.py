def build_query_string(params):
    return '&'.join(sorted([str(key)+'='+str(value) for key,value in params.items()]))
