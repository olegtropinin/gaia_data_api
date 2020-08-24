# Generated by Django 3.1 on 2020-08-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GaiaSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_id', models.PositiveBigIntegerField(help_text='1635721458409799680')),
                ('designation', models.CharField(help_text='Gaia DR2 1000225938242805248', max_length=28)),
                ('source_id', models.PositiveBigIntegerField(help_text='1000225938242805248')),
                ('random_index', models.PositiveIntegerField(help_text='1197051105')),
                ('ref_epoch', models.CharField(help_text='2015.5', max_length=6)),
                ('ra', models.FloatField()),
                ('ra_error', models.FloatField()),
                ('dec', models.FloatField()),
                ('dec_error', models.FloatField()),
                ('parallax', models.FloatField()),
                ('parallax_error', models.FloatField()),
                ('parallax_over_error', models.FloatField()),
                ('pmra', models.FloatField()),
                ('pmra_error', models.FloatField()),
                ('pmdec', models.FloatField()),
                ('pmdec_error', models.FloatField()),
                ('ra_dec_corr', models.FloatField()),
                ('ra_parallax_corr', models.FloatField()),
                ('ra_pmra_corr', models.FloatField()),
                ('ra_pmdec_corr', models.FloatField()),
                ('dec_parallax_corr', models.FloatField()),
                ('dec_pmra_corr', models.FloatField()),
                ('dec_pmdec_corr', models.FloatField()),
                ('parallax_pmra_corr', models.FloatField()),
                ('parallax_pmdec_corr', models.FloatField()),
                ('pmra_pmdec_corr', models.FloatField()),
                ('astrometric_n_obs_al', models.PositiveSmallIntegerField(help_text='184')),
                ('astrometric_n_obs_ac', models.PositiveSmallIntegerField(help_text='0')),
                ('astrometric_n_good_obs_al', models.PositiveSmallIntegerField(help_text='181')),
                ('astrometric_n_bad_obs_al', models.PositiveSmallIntegerField(help_text='3')),
                ('astrometric_gof_al', models.FloatField()),
                ('astrometric_chi2_al', models.FloatField()),
                ('astrometric_excess_noise', models.FloatField()),
                ('astrometric_excess_noise_sig', models.FloatField()),
                ('astrometric_params_solved', models.PositiveSmallIntegerField(help_text='3 or 31')),
                ('astrometric_primary_flag', models.BooleanField()),
                ('astrometric_weight_al', models.FloatField()),
                ('astrometric_pseudo_colour', models.FloatField()),
                ('astrometric_pseudo_colour_error', models.FloatField()),
                ('mean_varpi_factor_al', models.FloatField()),
                ('astrometric_matched_observations', models.PositiveSmallIntegerField(help_text='21')),
                ('visibility_periods_used', models.PositiveSmallIntegerField(help_text='10')),
                ('astrometric_sigma5d_max', models.FloatField()),
                ('frame_rotator_object_type', models.PositiveSmallIntegerField(help_text='0')),
                ('matched_observations', models.PositiveSmallIntegerField(help_text='22')),
                ('duplicated_source', models.BooleanField()),
                ('phot_g_n_obs', models.PositiveSmallIntegerField(help_text='189')),
                ('phot_g_mean_flux', models.FloatField()),
                ('phot_g_mean_flux_error', models.FloatField()),
                ('phot_g_mean_flux_over_error', models.FloatField()),
                ('phot_g_mean_mag', models.FloatField()),
                ('phot_bp_n_obs', models.PositiveSmallIntegerField(help_text='189')),
                ('phot_bp_mean_flux', models.FloatField()),
                ('phot_bp_mean_flux_error', models.FloatField()),
                ('phot_bp_mean_flux_over_error', models.FloatField()),
                ('phot_bp_mean_mag', models.FloatField()),
                ('phot_rp_n_obs', models.PositiveSmallIntegerField(help_text='21')),
                ('phot_rp_mean_flux', models.FloatField()),
                ('phot_rp_mean_flux_error', models.FloatField()),
                ('phot_rp_mean_flux_over_error', models.FloatField()),
                ('phot_rp_mean_mag', models.FloatField()),
                ('phot_bp_rp_excess_factor', models.FloatField()),
                ('phot_proc_mode', models.PositiveSmallIntegerField(help_text='0, 1 or 2')),
                ('bp_rp', models.FloatField()),
                ('bp_g', models.FloatField()),
                ('g_rp', models.FloatField()),
                ('radial_velocity', models.FloatField()),
                ('radial_velocity_error', models.FloatField()),
                ('rv_nb_transits', models.PositiveSmallIntegerField(help_text='0')),
                ('rv_template_teff', models.IntegerField(help_text='5000')),
                ('rv_template_logg', models.FloatField()),
                ('rv_template_fe_h', models.FloatField()),
                ('phot_variable_flag', models.CharField(help_text='NOT_AVAILABLE', max_length=13)),
                ('l', models.FloatField()),
                ('b', models.FloatField()),
                ('ecl_lon', models.FloatField()),
                ('ecl_lat', models.FloatField()),
                ('priam_flags', models.PositiveIntegerField(help_text='100001')),
                ('teff_val', models.FloatField()),
                ('teff_percentile_lower', models.FloatField()),
                ('teff_percentile_upper', models.FloatField()),
                ('a_g_val', models.FloatField()),
                ('a_g_percentile_lower', models.FloatField()),
                ('a_g_percentile_upper', models.FloatField()),
                ('e_bp_min_rp_val', models.FloatField()),
                ('e_bp_min_rp_percentile_lower', models.FloatField()),
                ('e_bp_min_rp_percentile_upper', models.FloatField()),
                ('flame_flags', models.PositiveIntegerField(help_text='200111')),
                ('radius_val', models.FloatField()),
                ('radius_percentile_lower', models.FloatField()),
                ('radius_percentile_upper', models.FloatField()),
                ('lum_val', models.FloatField()),
                ('lum_percentile_lower', models.FloatField()),
                ('lum_percentile_upper', models.FloatField()),
            ],
        ),
    ]