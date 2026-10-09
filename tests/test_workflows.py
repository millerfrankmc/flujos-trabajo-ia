import unittest

from flujos_ia.fixtures import PROPOSALS, REQUESTS, REQUIREMENTS, RULES
from flujos_ia.workflows import compare_proposals, organize_requests


class RequestWorkflowTests(unittest.TestCase):
    def test_detects_missing_date_and_timezone(self):
        results = organize_requests(REQUESTS, RULES)
        ana = results[0]
        self.assertEqual(ana.category, "formación")
        self.assertEqual(ana.status, "requiere aclaración")
        self.assertIn("fecha exacta", ana.missing)
        self.assertIn("zona horaria", ana.missing)

    def test_does_not_grant_access(self):
        result = organize_requests(REQUESTS, RULES)[1]
        self.assertEqual(result.status, "requiere aprobación")
        self.assertIn("aprobador", result.missing)
        self.assertNotIn("habilitado", result.next_step)

    def test_does_not_treat_pre_tax_price_as_final(self):
        result = organize_requests(REQUESTS, RULES)[2]
        self.assertIn("importe final con impuestos", result.missing)
        self.assertEqual(result.status, "requiere aclaración")

    def test_blocks_instruction_inside_source(self):
        result = organize_requests(REQUESTS, RULES)[3]
        self.assertTrue(result.policy_conflict)
        self.assertEqual(result.status, "requiere revisión")
        self.assertIsNone(result.draft)


class ProposalWorkflowTests(unittest.TestCase):
    def test_norte_meets_known_mandatory_requirements(self):
        result = compare_proposals(REQUIREMENTS, PROPOSALS)
        norte = result.proposals[0]
        self.assertIn("90 minutos por sesión", norte.covered)
        self.assertIn("precio final dentro del máximo: USD 540", norte.covered)
        self.assertIn("fechas por acordar", norte.missing_or_unconfirmed)

    def test_sur_is_not_comparable_as_quoted(self):
        result = compare_proposals(REQUIREMENTS, PROPOSALS)
        sur = result.proposals[1]
        self.assertIn("ofrece 60 minutos, no 90", sur.missing_or_unconfirmed)
        self.assertIn("precio final con impuestos no confirmado", sur.missing_or_unconfirmed)
        self.assertNotIn("precio final dentro del máximo: USD 420", sur.covered)

    def test_comparison_does_not_purchase(self):
        result = compare_proposals(REQUIREMENTS, PROPOSALS)
        self.assertIn("Norte", result.provisional_conclusion)
        self.assertIn("contratar", result.actions_blocked)
        self.assertIn("comprar", result.actions_blocked)


if __name__ == "__main__":
    unittest.main()
