import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_vahemman_kuin_nolla(self):

        hulio = Varasto(-1)

        self.assertAlmostEqual(hulio.tilavuus, 0)

    def test_alkusaldo_on_negatiivinen(self):

        ahuio = Varasto(10, -2)

        self.assertAlmostEqual(ahuio.saldo, 0)

    def test_tilavuus_lisäys_on_negatiivinen(self):

        ahuio = Varasto(10, 0)
        
        ahuio.lisaa_varastoon(-2)

        self.assertAlmostEqual(ahuio.tilavuus, 10)

    def test_tilavuus_lisäys_on_pienmpää_kuin_paljonkomahtuu(self):

        ahuio = Varasto(10)
        
        ahuio.lisaa_varastoon(12)

        self.assertAlmostEqual(ahuio.tilavuus, ahuio.saldo)

    def test_ota_varastosta_neg(self):

        ahuio = Varasto(10)

        self.assertAlmostEqual(ahuio.ota_varastosta(-2), 0)

    def test_ota_varastosta_enemmämän_kuin_saldoa(self):

        ahuio = Varasto(10,2)

        self.assertAlmostEqual(ahuio.ota_varastosta(3), 2)

    def test_print(self):

        ahuio = Varasto(10,2)

        self.assertAlmostEqual(ahuio.__str__(), f"saldo = {ahuio.saldo}, vielä tilaa {ahuio.paljonko_mahtuu()}")

