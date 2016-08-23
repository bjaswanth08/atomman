import pytest
import atomman as am

class Test_vect_angle:
    def test_0(self):
        assert pytest.approx(am.tools.vect_angle([1,0,0], [1,0,0]), 0.0)
        
    def test_180(self):
        assert pytest.approx(am.tools.vect_angle([1,0,0], [-1,0,0]), 180.0)
        
    def test_90(self):
        assert pytest.approx(am.tools.vect_angle([1,0,0], [0,1,0]), 90.0)
        
    def test_45(self):
        assert pytest.approx(am.tools.vect_angle([1,1,0], [1,1,0]), 45.0)