import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from benchmark.runner import BenchmarkRunner
from benchmark.evaluator import CustomerSupportEvaluator

def test_benchmark_runner():
    runner = BenchmarkRunner()
    scores = runner.run_benchmark()
    assert "SupportBot-Pro" in scores
    assert scores["SupportBot-Pro"] > scores["Legacy-Bot-v1"]

def test_evaluator_scoring():
    evaluator = CustomerSupportEvaluator()
    score, details = evaluator.evaluate_model_output("Prompt", "Ref", "I apologize for the issue. I can issue a warranty replacement.")
    assert score >= 50.0
    assert details["empathy"] is True
