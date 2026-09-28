import argparse, json, sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from benchmark.runner import BenchmarkRunner

def main():
    parser = argparse.ArgumentParser(description="Customer Support AI Benchmark CLI")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("run", help="Run benchmark leaderboard evaluation")

    args = parser.parse_args()
    runner = BenchmarkRunner()

    if args.command == "run":
        scores = runner.run_benchmark()
        print("=== Customer Support AI Benchmark Leaderboard ===")
        print(json.dumps(scores, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
