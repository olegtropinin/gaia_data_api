from django.db import models

# Create your models here.

class GaiaSource(models.Model):
    # TODO: Go over all fields to do models.Choices or models.IntegerChoices. For example priam_flags.

    solution_id = models.PositiveBigIntegerField(help_text='1635721458409799680')
    designation = models.CharField(max_length=28, help_text='Gaia DR2 1000225938242805248')
    source_id = models.PositiveBigIntegerField(primary_key=True, help_text='1000225938242805248')
    random_index = models.PositiveIntegerField(help_text='1197051105')
    ref_epoch = models.CharField(max_length=6, null=True, help_text='2015.5')
    ra = models.FloatField(null=True)
    ra_error = models.FloatField(null=True)
    dec = models.FloatField(null=True)
    dec_error = models.FloatField(null=True)
    parallax = models.FloatField(null=True)
    parallax_error = models.FloatField(null=True)
    parallax_over_error = models.FloatField(null=True)
    pmra = models.FloatField(null=True)
    pmra_error = models.FloatField(null=True)
    pmdec = models.FloatField(null=True)
    pmdec_error = models.FloatField(null=True)
    ra_dec_corr = models.FloatField(null=True)
    ra_parallax_corr = models.FloatField(null=True)
    ra_pmra_corr = models.FloatField(null=True)
    ra_pmdec_corr = models.FloatField(null=True)
    dec_parallax_corr = models.FloatField(null=True)
    dec_pmra_corr = models.FloatField(null=True)
    dec_pmdec_corr = models.FloatField(null=True)
    parallax_pmra_corr = models.FloatField(null=True)
    parallax_pmdec_corr = models.FloatField(null=True)
    pmra_pmdec_corr = models.FloatField(null=True)
    astrometric_n_obs_al = models.PositiveSmallIntegerField(null=True, help_text='184')
    astrometric_n_obs_ac = models.PositiveSmallIntegerField(null=True, help_text='0')
    astrometric_n_good_obs_al = models.PositiveSmallIntegerField(null=True, help_text='181')
    astrometric_n_bad_obs_al = models.PositiveSmallIntegerField(null=True, help_text='3')
    astrometric_gof_al = models.FloatField(null=True)
    astrometric_chi2_al = models.FloatField(null=True)
    astrometric_excess_noise = models.FloatField(null=True)
    astrometric_excess_noise_sig = models.FloatField(null=True)
    astrometric_params_solved = models.PositiveSmallIntegerField(null=True, help_text='3 or 31')
    astrometric_primary_flag = models.BooleanField(null=True)
    astrometric_weight_al = models.FloatField(null=True)
    astrometric_pseudo_colour = models.FloatField(null=True)
    astrometric_pseudo_colour_error = models.FloatField(null=True)
    mean_varpi_factor_al = models.FloatField(null=True)
    astrometric_matched_observations = models.PositiveSmallIntegerField(null=True, help_text='21')
    visibility_periods_used = models.PositiveSmallIntegerField(null=True, help_text='10')
    astrometric_sigma5d_max = models.FloatField(null=True)
    frame_rotator_object_type = models.PositiveSmallIntegerField(null=True, help_text='0')
    matched_observations = models.PositiveSmallIntegerField(null=True, help_text='22')
    duplicated_source = models.BooleanField(null=True)
    phot_g_n_obs = models.PositiveSmallIntegerField(null=True, help_text='189')
    phot_g_mean_flux = models.FloatField(null=True)
    phot_g_mean_flux_error = models.FloatField(null=True)
    phot_g_mean_flux_over_error = models.FloatField(null=True)
    phot_g_mean_mag = models.FloatField(null=True)
    phot_bp_n_obs = models.PositiveSmallIntegerField(null=True, help_text='189')
    phot_bp_mean_flux = models.FloatField(null=True)
    phot_bp_mean_flux_error = models.FloatField(null=True)
    phot_bp_mean_flux_over_error = models.FloatField(null=True)
    phot_bp_mean_mag = models.FloatField(null=True)
    phot_rp_n_obs = models.PositiveSmallIntegerField(null=True, help_text='21')
    phot_rp_mean_flux = models.FloatField(null=True)
    phot_rp_mean_flux_error = models.FloatField(null=True)
    phot_rp_mean_flux_over_error = models.FloatField(null=True)
    phot_rp_mean_mag = models.FloatField(null=True)
    phot_bp_rp_excess_factor = models.FloatField(null=True)
    phot_proc_mode = models.PositiveSmallIntegerField(null=True, help_text='0, 1 or 2')
    bp_rp = models.FloatField(null=True)
    bp_g = models.FloatField(null=True)
    g_rp = models.FloatField(null=True)
    radial_velocity = models.FloatField(null=True)
    radial_velocity_error = models.FloatField(null=True)
    rv_nb_transits = models.PositiveSmallIntegerField(null=True, help_text='0')
    rv_template_teff = models.FloatField(null=True)
    rv_template_logg = models.FloatField(null=True)
    rv_template_fe_h = models.FloatField(null=True)
    phot_variable_flag = models.CharField(max_length=13, null=True, help_text='NOT_AVAILABLE')
    l = models.FloatField(null=True)
    b = models.FloatField(null=True)
    ecl_lon = models.FloatField(null=True)
    ecl_lat = models.FloatField(null=True)
    priam_flags = models.PositiveIntegerField(null=True, help_text='100001')
    teff_val = models.FloatField(null=True)
    teff_percentile_lower = models.FloatField(null=True)
    teff_percentile_upper = models.FloatField(null=True)
    a_g_val = models.FloatField(null=True)
    a_g_percentile_lower = models.FloatField(null=True)
    a_g_percentile_upper = models.FloatField(null=True)
    e_bp_min_rp_val = models.FloatField(null=True)
    e_bp_min_rp_percentile_lower = models.FloatField(null=True)
    e_bp_min_rp_percentile_upper = models.FloatField(null=True)
    flame_flags = models.PositiveIntegerField(null=True, help_text='200111')
    radius_val = models.FloatField(null=True)
    radius_percentile_lower = models.FloatField(null=True)
    radius_percentile_upper = models.FloatField(null=True)
    lum_val = models.FloatField(null=True)
    lum_percentile_lower = models.FloatField(null=True)
    lum_percentile_upper = models.FloatField(null=True)
