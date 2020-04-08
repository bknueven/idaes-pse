##############################################################################
# Institute for the Design of Advanced Energy Systems Process Systems
# Engineering Framework (IDAES PSE Framework) Copyright (c) 2018-2019, by the
# software owners: The Regents of the University of California, through
# Lawrence Berkeley National Laboratory,  National Technology & Engineering
# Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia
# University Research Corporation, et al. All rights reserved.
#
# Please see the files COPYRIGHT.txt and LICENSE.txt for full copyright and
# license information, respectively. Both files are also available online
# at the URL "https://github.com/IDAES/idaes-pse".
##############################################################################
"""
Tests for Phase objects

Author: Andrew Lee
"""
from pyomo.environ import ConcreteModel, Set

from idaes.core.phases import (Phase, LiquidPhase, SolidPhase, VaporPhase,
                               PhaseType)


def test_PhaseType():
    assert len(PhaseType) == 4
    for i in PhaseType.__members__:
        assert i in ["undefined", "liquidPhase", "vaporPhase", "solidPhase"]


def test_config():
    m = ConcreteModel()

    m.phase = Phase()

    assert len(m.phase.config) == 2
    assert m.phase.config.component_list is None
    assert not m.phase.config._phase_list_exists


def test_populate_phase_list():
    m = ConcreteModel()

    m.phase = Phase()
    m.phase2 = Phase()

    assert isinstance(m.phase_list, Set)

    for p in m.phase_list:
        assert p in ["phase", "phase2"]


def test_is_phase_generic():
    m = ConcreteModel()

    m.phase = Phase()

    assert not m.phase.is_liquid_phase()
    assert not m.phase.is_solid_phase()
    assert not m.phase.is_vapor_phase()


def test_is_phase_old_style_liquid():
    m = ConcreteModel()

    m.Liq = Phase()

    assert m.Liq.is_liquid_phase()
    assert not m.Liq.is_solid_phase()
    assert not m.Liq.is_vapor_phase()


def test_is_phase_old_style_solid():
    m = ConcreteModel()

    m.Sol = Phase()

    assert not m.Sol.is_liquid_phase()
    assert m.Sol.is_solid_phase()
    assert not m.Sol.is_vapor_phase()


def test_is_phase_old_style_vapor():
    m = ConcreteModel()

    m.Vap = Phase()

    assert not m.Vap.is_liquid_phase()
    assert not m.Vap.is_solid_phase()
    assert m.Vap.is_vapor_phase()


def test_phase_list_exists():
    m = ConcreteModel()

    m.phase = Phase(default={"_phase_list_exists": True})
    m.phase2 = Phase(default={"_phase_list_exists": True})

    assert not hasattr(m, "phase_list")


def test_LiquidPhase():
    m = ConcreteModel()

    m.phase = LiquidPhase()

    assert m.phase.is_liquid_phase()
    assert not m.phase.is_solid_phase()
    assert not m.phase.is_vapor_phase()


def test_SolidPhase():
    m = ConcreteModel()

    m.phase = SolidPhase()

    assert not m.phase.is_liquid_phase()
    assert m.phase.is_solid_phase()
    assert not m.phase.is_vapor_phase()


def test_VaporPhase():
    m = ConcreteModel()

    m.phase = VaporPhase()

    assert not m.phase.is_liquid_phase()
    assert not m.phase.is_solid_phase()
    assert m.phase.is_vapor_phase()
