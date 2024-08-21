from programs.models import Program
from programs.util import Dependencies
from screener.models import Screen
from programs.programs.calc import Eligibility, ProgramCalculator
from .dependencies.base import PolicyEngineScreenInput
from typing import List
from ..engines import Sim


class PolicyEngineCalulator(ProgramCalculator):
    """
    Base class for all Policy Engine programs
    """

    pe_inputs: List[type[PolicyEngineScreenInput]] = []
    pe_outputs: List[type[PolicyEngineScreenInput]] = []

    pe_name = ""
    pe_category = ""
    pe_sub_category = ""

    def __init__(self, screen: Screen, program: Program):
        self.screen = screen
        self.program = program
        self._sim = None

    def set_engine(self, sim: Sim):
        self._sim = sim

    def eligible(self) -> Eligibility:
        e = Eligibility()

        e.value = self.value()
        e.eligible = e.value > 0

        return e

    def value(self):
        return int(self.get_variable())

    @property
    def pe_period(self) -> str:
        if self.program.fpl is None:
            raise Exception(f"the period is not configured for: {self.pe_name}")

        return self.program.fpl.pe_period

    @property
    def sim(self) -> Sim:
        if self._sim is None:
            raise Exception("Engine is not configured")

        return self._sim

    def get_variable(self):
        """
        Return value of the default variable
        """
        return self.sim.value(self.pe_category, self.pe_sub_category, self.pe_name, self.pe_period)

    @classmethod
    def can_calc(cls, missing_dependencies: Dependencies):
        for input in cls.pe_inputs:
            if missing_dependencies.has(*input.dependencies):
                return False

        return True


class PolicyEngineSpmCalulator(PolicyEngineCalulator):
    pe_category = "spm_units"
    pe_sub_category = "spm_unit"


class PolicyEngineTaxUnitCalulator(PolicyEngineCalulator):
    pe_category = "tax_units"
    pe_sub_category = "tax_unit"
    tax_unit_dependent = True


class PolicyEngineMembersCalculator(PolicyEngineCalulator):
    tax_unit_dependent = True
    pe_category = "people"

    def value(self):
        total = 0
        for member in self.screen.household_members.all():
            # The following programs use income from the tax unit,
            # so we want to skip any members that are not in the tax unit.
            if not self.in_tax_unit(member.id) and self.tax_unit_dependent:
                continue

            pe_value = self.get_member_variable(member.id)

            total += pe_value

        return total

    def in_tax_unit(self, member_id: int) -> bool:
        return str(member_id) in self.sim.members("tax_units", "tax_unit")

    def get_member_variable(self, member_id: int):
        return self.sim.value(self.pe_category, str(member_id), self.pe_name, self.pe_period)
