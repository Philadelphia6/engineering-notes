"""Recalculate examples from the Buck engineering notes. No third-party dependencies.

These are analytical estimates, not measured hardware results.
Run: python recalculate.py
"""
import math
import json

def calculate():
    vin, vo, fs, inductance = 32.0, 18.0, 440000.0, 15e-6
    power = 220.0
    average = power / (2 * vo)
    ripple = vo * (1 - vo / vin) / (inductance * fs)
    ripple_low_l = vo * (1 - vo / vin) / (0.8 * inductance * fs)
    peak = average + ripple / 2
    peak_with_bias = 1.1 * average + ripple_low_l / 2
    ov_ref = 3.3 * 9.1 / (1.5 + 9.1)
    oc_ref = 3.3 * 9.1 / (3.3 + 9.1)
    gain = 0.11
    ov_min = 3.3*.98*(9.1*.99)/(1.5*1.01+9.1*.99)/(gain*1.01/.99)
    ov_max = 3.3*1.02*(9.1*1.01)/(1.5*.99+9.1*1.01)/(gain*.99/1.01)
    return {
        "assumptions": "32V to 18V, 220W, per-phase 15uH, 440kHz; no transient model",
        "phase_average_A": average,
        "phase_ripple_pp_A": ripple,
        "phase_peak_nominal_A": peak,
        "phase_peak_Lminus20pct_A": average+ripple_low_l/2,
        "phase_peak_plus10pct_bias_A": peak_with_bias,
        "phase_rms_A": math.sqrt(average**2+ripple**2/12),
        "AP_cm4_15uH_6A_conservative": inductance*6**2/(6e6*.35*.25)*1e8,
        "AP_cm4_15uH_7p5A_conservative": inductance*7.5**2/(6e6*.35*.25)*1e8,
        "illustrative_gap_mm_Ae40_N12": 4*math.pi*1e-7*12**2*40e-6/inductance*1000,
        "PWM_Hz_TBCLK60MHz_PRD68_updown": 60e6/(2*68),
        "control_period_us_544ticks": 544/60e6*1e6,
        "hall_adc_minus10A_V_gain0p33": .33*(2.5-.2*10),
        "hall_adc_zero_V_gain0p33": .33*2.5,
        "hall_adc_plus10A_V_gain0p33": .33*(2.5+.2*10),
        "hall_adc_minus10A_V_divider10k18k": 18/28*(2.5-.2*10),
        "hall_adc_zero_V_divider10k18k": 18/28*2.5,
        "hall_adc_plus10A_V_divider10k18k": 18/28*(2.5+.2*10),
        "OV_reference_V": ov_ref,
        "OV_trip_V": ov_ref/gain,
        "OC_reference_V": oc_ref,
        "OC_trip_A": oc_ref/.2,
        "OC_trip_A_R56_1p6k": 3.3*9.1/(1.6+9.1)/.2,
        "OV_illustrative_min_V_2pct_supply_1pct_resistors": ov_min,
        "OV_illustrative_max_V_2pct_supply_1pct_resistors": ov_max,
        "V5_illustrative_min_V_1pct_feedback": .591*(1+200*.99/(27*1.01)),
        "GS8552_estimated_bandwidth_Hz_gain200": 1.8e6/201,
        "RC_corner_Hz_100ohm_330pF": 1/(2*math.pi*100*330e-12),
        "SY8303A_fs_Hz_Rfs47k": 1e8/47,
        "SY8303A_fs_Hz_Rfs100k": 1e8/100,
        "Cu_skin_depth_mm_440kHz_rho1p72e8": math.sqrt(1.72e-8/(math.pi*fs*4*math.pi*1e-7))*1000,
    }

if __name__ == "__main__":
    result=calculate()
    # Selected independent range checks catch unit/factor-of-two errors.
    assert 1.19 < result["phase_ripple_pp_A"] < 1.20
    assert 7.46 < result["phase_peak_plus10pct_bias_A"] < 7.48
    assert .102 < result["AP_cm4_15uH_6A_conservative"] < .104
    assert 25.75 < result["OV_trip_V"] < 25.76
    assert 12.10 < result["OC_trip_A"] < 12.12
    print(json.dumps(result, ensure_ascii=False, indent=2))
