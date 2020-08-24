import pytest
from django.urls import reverse


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_get_list(api_client):
    url = reverse('source-list')
    response = api_client.get(url)
    assert response.status_code == 200
    message = response.json()
    assert message['count'] == 29
    assert message['next'] == 'http://testserver/api/source/?page=2'
    assert message['previous'] is None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_get_detail(api_client):
    url = reverse('source-detail', kwargs={'pk': 1000250024419296000})
    response = api_client.get(url)
    assert response.status_code == 200
    message = response.json()
    assert message == {
        'source_id': 1000250024419296000,
        'solution_id': 1635721458409799680,
        'designation': 'Gaia DR2 1000250024419296000',
        'random_index': 574278759,
        'ref_epoch': '2015.5',
        'ra': 103.35252488087359,
        'ra_error': 0.023159487514148126,
        'dec': 56.3951438077475,
        'dec_error': 0.022835972469952497,
        'parallax': 0.7471075531667106,
        'parallax_error': 0.03640075236568113,
        'parallax_over_error': 20.52451,
        'pmra': 5.426702338191655,
        'pmra_error': 0.04541129853537301,
        'pmdec': -3.4681093990756002,
        'pmdec_error': 0.03740801268451435,
        'ra_dec_corr': 0.24057312,
        'ra_parallax_corr': -0.11131603,
        'ra_pmra_corr': -0.012407936,
        'ra_pmdec_corr': 0.02638851,
        'dec_parallax_corr': -0.36644787,
        'dec_pmra_corr': -0.15387154,
        'dec_pmdec_corr': 0.15846756,
        'parallax_pmra_corr': 0.5543776,
        'parallax_pmdec_corr': 0.17910668,
        'pmra_pmdec_corr': 0.33852795,
        'astrometric_n_obs_al': 188,
        'astrometric_n_obs_ac': 0,
        'astrometric_n_good_obs_al': 186,
        'astrometric_n_bad_obs_al': 2,
        'astrometric_gof_al': -2.6570694,
        'astrometric_chi2_al': 134.45885,
        'astrometric_excess_noise': 0.0,
        'astrometric_excess_noise_sig': 0.0,
        'astrometric_params_solved': 31,
        'astrometric_primary_flag': False,
        'astrometric_weight_al': 42.597908,
        'astrometric_pseudo_colour': 1.621749295689028,
        'astrometric_pseudo_colour_error': 0.006686582676564199,
        'mean_varpi_factor_al': -0.07543224,
        'astrometric_matched_observations': 22,
        'visibility_periods_used': 12,
        'astrometric_sigma5d_max': 0.05301447,
        'frame_rotator_object_type': 0,
        'matched_observations': 23,
        'duplicated_source': False,
        'phot_g_n_obs': 194,
        'phot_g_mean_flux': 34481.0655968688,
        'phot_g_mean_flux_error': 9.868142609987723,
        'phot_g_mean_flux_over_error': 3494.18,
        'phot_g_mean_mag': 14.344414,
        'phot_bp_n_obs': 23,
        'phot_bp_mean_flux': 18920.659953008657,
        'phot_bp_mean_flux_error': 33.11330958332746,
        'phot_bp_mean_flux_over_error': 571.3914,
        'phot_bp_mean_mag': 14.659047,
        'phot_rp_n_obs': 23,
        'phot_rp_mean_flux': 22720.349266808014,
        'phot_rp_mean_flux_error': 19.122784076572653,
        'phot_rp_mean_flux_over_error': 1188.1298,
        'phot_rp_mean_mag': 13.870882,
        'phot_bp_rp_excess_factor': 1.2076485,
        'phot_proc_mode': 0,
        'bp_rp': 0.7881651,
        'bp_g': 0.31463337,
        'g_rp': 0.47353172,
        'radial_velocity': None,
        'radial_velocity_error': None,
        'rv_nb_transits': 0,
        'rv_template_teff': None,
        'rv_template_logg': None,
        'rv_template_fe_h': None,
        'phot_variable_flag': 'NOT_AVAILABLE',
        'l': 159.7588384791222,
        'b': 22.58265744292899,
        'ecl_lon': 98.80303284136238,
        'ecl_lat': 33.36318082139236,
        'priam_flags': 100001,
        'teff_val': 5867.0,
        'teff_percentile_lower': 5805.25,
        'teff_percentile_upper': 6013.0,
        'a_g_val': 0.565,
        'a_g_percentile_lower': 0.252,
        'a_g_percentile_upper': 0.8141,
        'e_bp_min_rp_val': 0.287,
        'e_bp_min_rp_percentile_lower': 0.1196,
        'e_bp_min_rp_percentile_upper': 0.4051,
        'flame_flags': 200111,
        'radius_val': 1.5079575,
        'radius_percentile_lower': 1.4356179,
        'radius_percentile_upper': 1.5402082,
        'lum_val': 2.4273772,
        'lum_percentile_lower': 2.1525965,
        'lum_percentile_upper': 2.702158
    }
