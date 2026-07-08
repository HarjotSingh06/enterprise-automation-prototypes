
import unittest
from automation_workflow import DataWorkflowEngine

class TestEnterpriseAutomationPipeline(unittest.TestCase):
    """
    Automated testing suite to validate data handling integrity, 
    error boundary rules, and pipeline configuration stability.
    """

    def setUp(self):
        self.engine = DataWorkflowEngine()

    def test_successful_payload_transformation(self):
        """Validates that normal operational data is correctly transformed and standardized."""
        raw_input = '{"id": "5001", "email": "User.Name@LSEC.ac.uk", "notes": "Valid request entries."}'
        
        result = self.engine.transform_and_validate_payload(raw_input)
        
        self.assertEqual(result["record_id"], 5001)
        self.assertEqual(result["sender_email"], "user.name@lsec.ac.uk") # Verify lowercasing sanitation
        self.assertEqual(result["status"], "PENDING_REVIEW")

    def test_invalid_email_governance_rejection(self):
        """Verifies that bad or unsafe data payloads are rejected by schema guardrails."""
        bad_input = '{"id": "5002", "email": "invalid_email_format", "notes": "Bad email field."}'
        
        with self.assertRaises(ValueError):
            self.engine.transform_and_validate_payload(bad_input)

    def test_ai_enrichment_logic(self):
        """Ensures the AI processing simulation successfully adds intelligent fields and changes status flags."""
        base_data = {"record_id": 99, "sender_email": "test@demo.com", "raw_notes": "Urgent structural changes."}
        
        enriched = self.engine.simulate_ai_copilot_enrichment(base_data)
        
        self.assertIn("ai_insights", enriched)
        self.assertEqual(enriched["status"], "PROCESSED_SUCCESS")
        self.assertTrue(enriched["ai_insights"].startswith("AI Auto-Summary:"))

if __name__ == "__main__":
    unittest.main()
