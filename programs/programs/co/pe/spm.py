import programs.programs.policyengine.calculators.dependencies as dependency
from programs.programs.federal.pe.spm import Snap


class CoSnap(Snap):
    pe_inputs = [
        *Snap.pe_inputs,
        dependency.spm.ElectricityExpenseDependency,
    ]
