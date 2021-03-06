#!/usr/bin/env python


def hack_dict(*tpls, **as_kw):
    if as_kw != {}:
        return {key: value for key, value in as_kw.items()}
    else:
        return {tpls[0][i][0]: tpls[0][i][1] for i in range(0, len(tpls[0]))}


def birthday_ranges(birthdays, ranges):
    result = []
    aux = []
    for tpl in ranges:
        aux.append([day for day in birthdays if tpl[0] <= day <= tpl[1]])
    result.extend([len(aux[i]) for i in range(0, len(aux))])
    return result
