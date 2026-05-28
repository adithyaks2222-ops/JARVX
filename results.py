def render_results(results):
    print("\n[JARVX SCAN RESULTS]\n")

    print(f"{'PORT':<8}{'STATE':<10}{'SERVICE':<12}{'RISK'}")
    print("-" * 40)

    for result in results:
        print(
            f"{result['port']:<8}"
            f"{result['state']:<10}"
            f"{result['service']:<12}"
            f"{result['risk']}"
        )