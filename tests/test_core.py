import unittest,math
from link_budget_intervals.core import run
class DomainTests(unittest.TestCase):
 def fixture(self):return dict(frequency_hz=[1e9]*2,range_m=[1e6]*2,bitrate=[1e6]*2,tx_dbw=[0]*2,tx_gain_dbi=[0]*2,rx_gain_dbi=[0]*2,loss_db=[0]*2,noise_density_dbw_hz=[-200]*2,required_ebn0_db=[0]*2)
 def test_friis(self):
  x=run(self.fixture());self.assertAlmostEqual(x['free_space_loss_db'][0],152.4477832219,places=6);self.assertAlmostEqual(x['margin_db'][0],-12.4477832219,places=6)
 def test_doubling_range(self):
  d=self.fixture();a=run(d)['margin_db'][0];d['range_m']=[2e6]*2;self.assertAlmostEqual(a-run(d)['margin_db'][0],20*math.log10(2))
 def test_interval_contains_nominal(self):
  d=self.fixture();m=run(d)['margin_db'][0];d['loss_db']=[0,3];x=run(d)['margin_db'];self.assertEqual(x,[m-3,m])
