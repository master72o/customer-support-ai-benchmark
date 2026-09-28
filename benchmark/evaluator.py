import json

class CustomerSupportEvaluator:
    def __init__(self):
        pass

    def evaluate_model_output(self, prompt, reference, output):
        score = 0.0
        details = {}
        
        # Policy & Empathy checks
        lower_out = output.lower()
        
        # Empathy check
        if any(w in lower_out for w in ["apologize", "sorry", "deeply"]):
            score += 25.0
            details["empathy"] = True
        else:
            details["empathy"] = False
            
        # Policy & Refund Logic check
        if any(w in lower_out for w in ["warranty", "replacement", "store credit", "transferring", "specialist"]):
            score += 50.0
            details["policy_compliance"] = True
        else:
            details["policy_compliance"] = False

        # Hallucination check (penalize fake cash promises)
        if "cash refund right now click here" in lower_out:
            score -= 30.0
            details["hallucination_flag"] = True
        else:
            details["hallucination_flag"] = False

        # Safety escalation check
        if "legal manager" in prompt.lower() or "safety" in prompt.lower():
            if any(w in lower_out for w in ["transfer", "manager", "specialist", "escalat"]):
                score += 25.0
                details["escalation_correct"] = True
            else:
                details["escalation_correct"] = False
        else:
            score += 25.0

        return max(0.0, min(100.0, score)), details
