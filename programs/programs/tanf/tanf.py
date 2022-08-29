from django.utils.translation import gettext as _
from decimal import Decimal
import math

def calculate_tanf(screen, data):
    value = 0
    child_age_limit = 19
    children = screen.num_children(age_max=child_age_limit)
    guardians = screen.num_guardians()

    eligibility = eligibility_tanf(screen, children, guardians)

    if eligibility['eligible']:
        value = value_tanf(screen, children, guardians)

    calculation = {
        'eligibility': eligibility,
        'value': value
    }

    return calculation


def eligibility_tanf(screen, children, guardians):
    eligibility = {
        "eligible": True,
        "passed": [],
        "failed": []
    }
    frequency = "monthly"
    earned_income_types = ["wages", "selfEmployment"]

    one_parent_income_bands = {
        1: 331,
        2: 421,
        3: 510,
        4: 605,
        5: 697,
        6: 770,
        7: 844,
        8: 920,
        9: 992,
        10: 1065
    }

    two_parent_income_bands = {
        1: 439,
        2: 533,
        3: 628,
        4: 716,
        5: 787,
        6: 861,
        7: 937,
        8: 1009,
        9: 1082,
        10: 1155
    }

    child_only_income_bands = {
        1: 117,
        2: 245,
        3: 368,
        4: 490,
        5: 587,
        6: 678,
        7: 755,
        8: 830,
        9: 904,
        10: 977
    }

    # CHILD TEST
    if children < 1:
        eligibility["failed"].append(_("Households must have at least one dependent child under the age of 18, ")\
                                     +_("and have primary (more than 50%) custody of that child."))
        eligibility["eligible"] = False
        return eligibility
    else:
        eligibility["passed"].append(_("Household has at least one dependent child under the age of 18"))

    # SET INCOME LIMIT DEPENDING ON HOUSEHOLD COMPOSITION
    if guardians == 0:
        income_bands = child_only_income_bands
    elif guardians == 1:
        income_bands = one_parent_income_bands
    elif guardians >= 2:
        income_bands = two_parent_income_bands

    income_limit = income_bands[children]
    earned_income = screen.calc_gross_income(frequency, earned_income_types)
    tanf_earned_income = Decimal(.33)*earned_income

    clabel = "children"
    glabel = "guardians"
    if guardians == 1:
        glabel = "guardian"
    if children == 1:
        clabel = "child"

    # INCOME TEST
    income_test_description = _("Households with ")\
        +str(guardians)+" "+glabel\
        +_(" and ")\
        +str(children)+" "+clabel\
        +_(" must have a monthly household income below ")\
        +str(income_limit)\
        +_(". Your TANF qualifying household income is ")\
        +str(math.trunc(tanf_earned_income))\
        +"."

    if tanf_earned_income <= income_limit:
        eligibility['passed'].append(income_test_description)
    else:
        eligibility['eligible'] = False
        eligibility['failed'].append(income_test_description)

    return eligibility


def value_tanf(screen, children, guardians):

    child_only_value_bands = {
        1: 141,
        2: 296,
        3: 444,
        4: 593,
        5: 711,
        6: 821,
        7: 915,
        8: 1004,
        9: 1095,
        10: 1195
    }

    one_parent_value_bands = {
        1: 400,
        2: 508,
        3: 617,
        4: 732,
        5: 844,
        6: 932,
        7: 1022,
        8: 1113,
        9: 1201,
        10: 1289
    }

    two_parent_value_bands = {
        1: 531,
        2: 645,
        3: 760,
        4: 866,
        5: 952,
        6: 1042,
        7: 1135,
        8: 1222,
        9: 1309,
        10: 1398
    }

    if guardians < 1:
        value_band = child_only_value_bands
    elif guardians == 1:
        value_band = one_parent_value_bands
    elif guardians >= 2:
        value_band = two_parent_value_bands

    value = value_band[children] * 12
    return value