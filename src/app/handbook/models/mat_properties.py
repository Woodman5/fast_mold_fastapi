import datetime
import ormar
from src.app.base.models_base import (
    AbstractBaseModel,
    ModelMixin,
    SoftDeleteMixin,
    TimestampMixin,
    NameMixin,
    DescriptionMixin,
    ShortDescriptionMixin,
    UrlMixin,
)

from . import common_data


class HardnessScales(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Hardness Scales Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_hd"

    hs_min = ormar.Integer(default=0)
    hs_max = ormar.Integer(default=100)
    hs_units = ormar.String(max_length=30, nullable=True)


class CommonHardness(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Human readable hardness Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_comhd"


class Status(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Statuses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_status"


class Tech(AbstractBaseModel, NameMixin):
    """ Technologies list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_tech"


class ToolClass(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ ToolClasses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_toolclasses"


class MaterialType(AbstractBaseModel, NameMixin):
    """ MaterialTypes list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_mattypes"


class ImitationMaterial(AbstractBaseModel, NameMixin):
    """ ImitationMaterials list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_imitmat"


class ChemicalResistance(AbstractBaseModel, NameMixin):
    """ ChemicalResistances list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_chemres"


class MeasuringStandards(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ MeasuringStandards Model """

    standard_type = ormar.String(max_length=30, choices=common_data.standard_type_list)
    application_type = ormar.String(max_length=30, choices=common_data.application_type_list)

    class Meta(ormar.ModelMeta):
        tablename = "hb_measuring"


class Colors(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Colors Model """

    color_type = ormar.String(max_length=30, choices=common_data.color_type_list)
    hex_code = ormar.String(max_length=30)
    rgb_code = ormar.String(max_length=30)

    class Meta(ormar.ModelMeta):
        tablename = "hb_colors"


class TypeTech(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin):
    """ TypeTech Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_typetech"

    technology = ormar.ForeignKey(Tech)


class ToolType(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin):
    """ ToolType Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_tooltype"

    tool_class = ormar.ForeignKey(ToolClass)


class ToolMan(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin, UrlMixin):
    """ Tool Manufacturer Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_toolman"

    country = ormar.String(max_length=800)
    technology = ormar.ManyToMany(Tech)


#  --------------------------------------------------
# todo material = ormar.ForeignKey(Material)
class ThermalChars(AbstractBaseModel):
    """ Thermal Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_therm"

    thermal_expansion = ormar.Decimal(minimum=0.0, max_digits=12, precision=8, nullable=True)
    temp_oper_min = ormar.Integer(minimum=-274, nullable=True)
    temp_deform = ormar.Integer(minimum=-274, nullable=True)

    thermal_expansion_st = ormar.ForeignKey(MeasuringStandards, related_name='the_st', nullable=True)
    temp_deform_st = ormar.ForeignKey(MeasuringStandards, related_name='temdef_st', nullable=True)


# todo material = ormar.ForeignKey(Material)
class ShockLoad(AbstractBaseModel):
    """ Shock Load Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_shload"

    izod_notched = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    izod_unnotched = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    sharpy = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)

    izod_notched_st = ormar.ForeignKey(MeasuringStandards, related_name='in_st', nullable=True)
    izod_unnotched_st = ormar.ForeignKey(MeasuringStandards, related_name='iun_st', nullable=True)
    sharpy_st = ormar.ForeignKey(MeasuringStandards, related_name='sh_st', nullable=True)


#  todo chemical_resistance = models.ManyToManyField(ChemicalResistance) перенести в Material
# todo material = ormar.ForeignKey(Material)
class MechanicalChars(AbstractBaseModel):
    """ Mechanical Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_mechchars"

    tensile_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    flexural_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    compressive_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_strength_lengthwise = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_strength_crosswise = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    elastic_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    tensile_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    flexural_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    compressive_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_modulus_lengthwise = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_modulus_crosswise = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    elongation_at_break = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    interlaminar_shear_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    shear_strain = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    single_shear_bearing = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    openhole_tension_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    openhole_tension_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    filledhole_tension_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    filledhole_tension_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    filledhole_compression_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    filledhole_compression_modulus = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    tool_side_peel = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    water_absorption = ormar.Decimal(minimum=0.0, max_digits=5, precision=2, nullable=True)
    shrinkage = ormar.Decimal(minimum=0.0, max_digits=5, precision=2, nullable=True)

    shrinkage_desc = ormar.String(max_length=400, nullable=True)

    tensile_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='ts_st', nullable=True)
    flexural_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='fs_st', nullable=True)
    compressive_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='cs_st', nullable=True)
    shear_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='ss_st', nullable=True)
    shear_strength_lengthwise_st = ormar.ForeignKey(MeasuringStandards, related_name='ssl_st', nullable=True)
    shear_strength_crosswise_st = ormar.ForeignKey(MeasuringStandards, related_name='ssc_st', nullable=True)
    elastic_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='el_st', nullable=True)
    tensile_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='tm_st', nullable=True)
    flexural_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='fm_st', nullable=True)
    compressive_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='cm_st', nullable=True)
    shear_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='sm_st', nullable=True)
    shear_modulus_lengthwise_st = ormar.ForeignKey(MeasuringStandards, related_name='sml_st', nullable=True)
    shear_modulus_crosswise_st = ormar.ForeignKey(MeasuringStandards, related_name='smc_st', nullable=True)
    elongation_at_break_st = ormar.ForeignKey(MeasuringStandards, related_name='eb_st', nullable=True)
    interlaminar_shear_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='ilss_st', nullable=True)
    shear_strain_st = ormar.ForeignKey(MeasuringStandards, related_name='sst_st', nullable=True)
    single_shear_bearing_st = ormar.ForeignKey(MeasuringStandards, related_name='ssb_st', nullable=True)
    openhole_tension_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='oht_st', nullable=True)
    openhole_tension_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='ohtm_st', nullable=True)
    filledhole_tension_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='fht_st', nullable=True)
    filledhole_tension_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='fhtm_st', nullable=True)
    filledhole_compression_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='fhc_st', nullable=True)
    filledhole_compression_modulus_st = ormar.ForeignKey(MeasuringStandards, related_name='fhcm_st', nullable=True)
    water_absorption_st = ormar.ForeignKey(MeasuringStandards, related_name='wa_st', nullable=True)
    shrinkage_st = ormar.ForeignKey(MeasuringStandards, related_name='shr_st', nullable=True)


# todo material = ormar.ForeignKey(Material)
class ElectroProp(AbstractBaseModel):
    """ Electrical Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_elecprop"

    dielectric_const = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)
    volume_resistivity = ormar.Decimal(minimum=0.0, max_digits=20, precision=18, nullable=True)
    dissipation_factor = ormar.Decimal(minimum=0.0, max_digits=8, precision=5, nullable=True)
    dielectric_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=5, nullable=True)

    dielectric_const_st = ormar.ForeignKey(MeasuringStandards, related_name='dc_st', nullable=True)
    volume_resistivity_st = ormar.ForeignKey(MeasuringStandards, related_name='vr_st', nullable=True)
    dissipation_factor_st = ormar.ForeignKey(MeasuringStandards, related_name='df_st', nullable=True)
    dielectric_strength_st = ormar.ForeignKey(MeasuringStandards, related_name='ds_st', nullable=True)


# todo material = ormar.ForeignKey(Material)
class BurnTesting(AbstractBaseModel):
    """ Burn Testing Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_burnt"

    hor_burn_15 = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    hor_burn_60 = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    ver_burn_12 = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    ignition45 = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    heat_release = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    nbs_flamm = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    nbs_non_flamm = ormar.Integer(minimum=0, maximum=10000, nullable=True)

    flammability = ormar.String(max_length=100, choices=common_data.flammability_list, nullable=True)

    additional_props = ormar.Text(nullable=True)

    flammability_st = ormar.ForeignKey(MeasuringStandards, related_name='flam', nullable=True)
    hor_burn_15_st = ormar.ForeignKey(MeasuringStandards, related_name='hb15_st', nullable=True)
    hor_burn_60_st = ormar.ForeignKey(MeasuringStandards, related_name='hb60_st', nullable=True)
    ver_burn_12_st = ormar.ForeignKey(MeasuringStandards, related_name='vb12_st', nullable=True)
    ignition45_st = ormar.ForeignKey(MeasuringStandards, related_name='i45_st', nullable=True)
    heat_release_st = ormar.ForeignKey(MeasuringStandards, related_name='hr_st', nullable=True)
    nbs_flamm_st = ormar.ForeignKey(MeasuringStandards, related_name='nbsf_st', nullable=True)
    nbs_non_flamm_st = ormar.ForeignKey(MeasuringStandards, related_name='nbsn_st', nullable=True)


#  todo support_mat = models.ManyToManyField(Material)
# todo material = ormar.ForeignKey(Material)
class Printing3D(AbstractBaseModel):
    """ Printing3D Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_p3d"

    mat_type = ormar.String(max_length=50, choices=common_data.mat_type_list, nullable=True)
    supp_removing_desc = ormar.String(max_length=800, nullable=True)

    fraction_dim = ormar.Decimal(minimum=0.0, maximum=10, max_digits=4, precision=2, nullable=True)
    filament_diam = ormar.Decimal(minimum=0.0, maximum=10, max_digits=4, precision=2, nullable=True)

    support = ormar.Boolean(nullable=True)
    supp_removing = ormar.Boolean(nullable=True)

    heat_release = ormar.Integer(minimum=0, maximum=99, nullable=True)


# todo material = ormar.ForeignKey(Material)
class Silicone(AbstractBaseModel):
    """ Silicone Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_sil"

    tear_strength = ormar.Decimal(minimum=0.0, max_digits=8, precision=2, nullable=True)

    silicon_base = ormar.Boolean(nullable=True)


# todo hardener = models.ForeignKey(Material)
# todo material = ormar.ForeignKey(Material)
class Resins(AbstractBaseModel):
    """ Resin Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_resins"

    resin_type = ormar.String(max_length=50, choices=common_data.resin_type_list, nullable=True)

    accel = ormar.Boolean(nullable=True)
    pre_accel = ormar.Boolean(nullable=True)

    hardener_percent = ormar.Decimal(minimum=0.0, maximum=100, max_digits=4, precision=2, nullable=True)
    accel_percent = ormar.Decimal(minimum=0.0, maximum=100, max_digits=4, precision=2, nullable=True)
    styrene_percent = ormar.Decimal(minimum=0.0, maximum=100, max_digits=4, precision=2, nullable=True)

    temp_glass = ormar.Integer(minimum=0, nullable=True)
    temp1 = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    temp2 = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    temp3 = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    temp1_time = ormar.Integer(minimum=0, maximum=259200, nullable=True)  # 3 суток
    temp2_time = ormar.Integer(minimum=0, maximum=259200, nullable=True)  # 3 суток
    temp3_time = ormar.Integer(minimum=0, maximum=259200, nullable=True)  # 3 суток

    temp_glass_st = ormar.ForeignKey(MeasuringStandards, related_name='temp_gl_st', nullable=True)


# todo material = ormar.ForeignKey(Material)
class Fibers(AbstractBaseModel):
    """ Fiber Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_fiber"

    fiber_form = ormar.String(max_length=50, choices=common_data.fiber_form_list, nullable=True)
    fiber_type = ormar.String(max_length=50, choices=common_data.fiber_type_list, nullable=True)
    netting = ormar.String(max_length=50, choices=common_data.netting_list, nullable=True)

    fb_density = ormar.Integer(minimum=0, maximum=50000, nullable=True)

    fb_thickness = ormar.Decimal(minimum=0, maximum=20, max_digits=5, precision=3, nullable=True)
    fb_thickness_curing = ormar.Decimal(minimum=0, maximum=20, max_digits=5, precision=3, nullable=True)
    fb_curing_pressure = ormar.Decimal(minimum=0, maximum=20, max_digits=6, precision=3, nullable=True)
    fb_resin_percent = ormar.Decimal(minimum=0, maximum=100, max_digits=4, precision=2, nullable=True)


# todo material = ormar.ForeignKey(Material)
class Prepregs(AbstractBaseModel):
    """ Prepreg Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_prepreg"

    plastic_density = ormar.Integer(minimum=0, maximum=50000, nullable=True)

    pp_thickness_curing = ormar.Decimal(minimum=0, maximum=20, max_digits=5, precision=3, nullable=True)
    pp_autoclave_pressure = ormar.Decimal(minimum=0, maximum=20, max_digits=6, precision=3, nullable=True)
    pp_vacuum_pressure = ormar.Decimal(minimum=0, maximum=20, max_digits=5, precision=3, nullable=True)
    pp_resin_percent = ormar.Decimal(minimum=0, maximum=100, max_digits=4, precision=2, nullable=True)

    self_adges = ormar.Boolean(nullable=True)


# todo material = ormar.ForeignKey(Material)
class Cores(AbstractBaseModel):
    """ Core Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_core"

    core_type = ormar.String(max_length=50, choices=common_data.core_type_list, nullable=True)
    core_material = ormar.String(max_length=50, choices=common_data.core_material_list, nullable=True)
    default_thickness = ormar.String(max_length=50, choices=common_data.default_thickness_list, nullable=True)
    cuts = ormar.String(max_length=100, nullable=True)

    length = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    width = ormar.Integer(minimum=0, maximum=10000, nullable=True)
    thickness_min = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    thickness_max = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    cell_dim = ormar.Integer(minimum=0, maximum=10000, nullable=True)

    wide_cells = ormar.Boolean(nullable=True)
    double_cuts = ormar.Boolean(nullable=True)
    fiber_support = ormar.Boolean(nullable=True)

    perforation = ormar.Decimal(minimum=0, maximum=20, max_digits=3, precision=1, nullable=True)
    resin_absorb = ormar.Decimal(minimum=0, maximum=100, max_digits=4, precision=2, nullable=True)


# todo material = ormar.ForeignKey(Material)
class Storage(AbstractBaseModel):
    """ Storage Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_storage"

    expiry_date = ormar.Integer(minimum=0, maximum=600, nullable=True)
    temp_stor_max = ormar.Integer(minimum=-273, maximum=1000, nullable=True)
    temp_stor_min = ormar.Integer(minimum=-273, maximum=1000, nullable=True)
    rt_expiry_date = ormar.Integer(minimum=0, maximum=2592000, nullable=True)  # 30 суток в секундах
    rt_temp_stor = ormar.Integer(minimum=-273, maximum=1000, nullable=True)
    humidity = ormar.Integer(minimum=0, maximum=100, nullable=True)
    work_temp_min = ormar.Integer(minimum=-273, maximum=1000, nullable=True)

    uv_protection = ormar.Boolean(nullable=True)

    storage_desc = ormar.Text(nullable=True)
    before_using_desc = ormar.Text(nullable=True)


# todo material = ormar.ForeignKey(Material)
class MatFiles(AbstractBaseModel):
    """ Material Files Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_mfiles"

    tds_file = ormar.Text(nullable=True)  # URL
    sert_file = ormar.Text(nullable=True)  # URL
    avia_sert_file = ormar.Text(nullable=True)  # URL
    ships_sert_file = ormar.Text(nullable=True)  # URL
    space_sert_file = ormar.Text(nullable=True)  # URL
    med_sert_file = ormar.Text(nullable=True)  # URL
    food_sert_file = ormar.Text(nullable=True)  # URL
    car_sert_file = ormar.Text(nullable=True)  # URL

    additional_files = ormar.JSON(nullable=True)  # List[URL]

    avia_desc = ormar.String(max_length=400, nullable=True)
    ships_desc = ormar.String(max_length=400, nullable=True)
    space_desc = ormar.String(max_length=400, nullable=True)
    med_desc = ormar.String(max_length=400, nullable=True)
    food_desc = ormar.String(max_length=400, nullable=True)
    car_desc = ormar.String(max_length=400, nullable=True)


class Filler(AbstractBaseModel, NameMixin, ShortDescriptionMixin):
    """ Filler Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_filler"


class ChemicalCompound(AbstractBaseModel, NameMixin, ShortDescriptionMixin):
    """ Chemical Compound Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_ccomp"


# todo covering = models.ForeignKey(Material)
# todo material = ormar.ForeignKey(Material)
class MineralFiller(AbstractBaseModel):
    """ Mineral Filler Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_mfiller"

    filler = ormar.ForeignKey(Filler, related_name='filler', nullable=True)
    compound = ormar.ForeignKey(ChemicalCompound, related_name='compound', nullable=True)

    fraction = ormar.Decimal(minimum=0, maximum=10, max_digits=8, precision=7, nullable=True)
    real_density = ormar.Decimal(minimum=0, maximum=1000, max_digits=4, precision=3, nullable=True)
    fake_density = ormar.Decimal(minimum=0, maximum=1000, max_digits=4, precision=3, nullable=True)


# todo material = ormar.ForeignKey(Material)
class TechnologyChars(AbstractBaseModel):
    """ Technology Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_tchars"

    mix_density = ormar.Decimal(minimum=0, max_digits=8, precision=2, nullable=True)
    wall_thickness_min = ormar.Decimal(minimum=0, max_digits=4, precision=2, nullable=True)
    wall_thickness_max = ormar.Decimal(minimum=0, max_digits=4, precision=2, nullable=True)
    hole_min = ormar.Decimal(minimum=0, max_digits=4, precision=2, nullable=True)
    fillet_min = ormar.Decimal(minimum=0, max_digits=4, precision=2, nullable=True)
    part_volume_max = ormar.Decimal(minimum=0, max_digits=10, precision=1, nullable=True)

    tool_tempr_start = ormar.Integer(minimum=0, nullable=True)
    comp_tempr_start = ormar.Integer(minimum=0, nullable=True)
    comp_tempr_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    degasation = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    degasation_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    mixing_degasation = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    mixing_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    life_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    life_time_temp_min = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    life_time_temp_max = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    degasation_before_molding = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    degasation_before_molding_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    degasation_during_molding = ormar.Integer(minimum=0, maximum=1000, nullable=True)
    degasation_during_molding_time = ormar.Integer(minimum=0, maximum=86400, nullable=True)
    curing_inmold_time = ormar.Integer(minimum=0, maximum=2592000, nullable=True)
    temp_curing_inmold_min = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    temp_curing_inmold_max = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    demold_time = ormar.Integer(minimum=0, maximum=259200, nullable=True)
    demold_time_temp_min = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    demold_time_temp_max = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    curing_time = ormar.Integer(minimum=0, maximum=2592000, nullable=True)
    curing_time_temp_min = ormar.Integer(minimum=-273, maximum=10000, nullable=True)
    curing_time_temp_max = ormar.Integer(minimum=-273, maximum=10000, nullable=True)

    wall_thickness_min_desc = ormar.String(max_length=400, nullable=True)
    wall_thickness_max_desc = ormar.String(max_length=400, nullable=True)
    tool_tempr_start_desc = ormar.String(max_length=400, nullable=True)
    comp_tempr_start_desc = ormar.String(max_length=400, nullable=True)
    degasation_desc = ormar.String(max_length=400, nullable=True)
    mixing_degasation_desc = ormar.String(max_length=400, nullable=True)
    mixing_desc = ormar.String(max_length=400, nullable=True)
    life_time_desc = ormar.String(max_length=400, nullable=True)
    degasation_before_molding_desc = ormar.String(max_length=400, nullable=True)
    degasation_during_molding_desc = ormar.String(max_length=400, nullable=True)
    curing_inmold_desc = ormar.String(max_length=400, nullable=True)
    demold_time_desc = ormar.String(max_length=400, nullable=True)
    curing_time_desc = ormar.String(max_length=400, nullable=True)

    painting = ormar.JSON()  # мультиселект из списка painting_list

    mix_density_st = ormar.ForeignKey(MeasuringStandards, related_name='mixd_st', nullable=True)
    life_time_st = ormar.ForeignKey(MeasuringStandards, related_name='lft_st', nullable=True)

