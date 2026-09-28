import json, os
from benchmark.evaluator import CustomerSupportEvaluator

class BenchmarkRunner:
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.json')
        with open(dataset_path) as f:
            self.dataset = json.load(f)
        self.evaluator = CustomerSupportEvaluator()

    def run_benchmark(self):
        models = ["SupportBot-Pro", "SupportBot-Lite", "Base-LLM-7B", "Legacy-Bot-v1"]
        results = {m: {"total_score": 0.0, "count": 0} for m in models}

        for item in self.dataset:
            prompt = item['prompt']
            ref = item['reference_policy']
            outputs = item['model_outputs']
            for model_name, out_text in outputs.items():
                score, details = self.evaluator.evaluate_model_output(prompt, ref, out_text)
                results[model_name]["total_score"] += score
                results[model_name]["count"] += 1

        summary = {}
        for m, data in results.items():
            avg = data["total_score"] / max(1, data["count"])
            summary[m] = round(avg, 2)
        return summary
