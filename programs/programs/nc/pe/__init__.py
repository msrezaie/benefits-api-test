import programs.programs.nc.pe.member as member
import programs.programs.nc.pe.spm as spm
from programs.programs.policyengine.calculators.base import PolicyEngineCalulator


nc_member_calculators = {"nc_medicaid": member.NcMedicaid, "nc_wic": member.NcWic}
nc_spm_calculators = {"nc_tanf": spm.NcTanf}

nc_pe_calculators: dict[str, type[PolicyEngineCalulator]] = {
    **nc_member_calculators,
    **nc_spm_calculators,
}
