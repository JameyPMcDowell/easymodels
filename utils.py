def get_param_strings_from_pipe(pipe):
    return [k for k in pipe.get_params().keys() if '__' in k]


def create_column_selector_options(list_of_list_of_cols):
    return [[('selector', 'passthrough', l)] for l in list_of_list_of_cols]
