# A simple script to demonstrate logical flow and data types
# Created by: Luke Akimoff

def calculate_success_rate(tasks_completed: int, total_tasks: int) -> float:
    """Calculates the percentage of tasks completed correctly."""
    if total_tasks == 0:
        return 0.0
    
    success_rate = (tasks_completed / total_tasks) * 100
    return round(success_rate, 2)

def main():
    # Test Data
    completed = 45
    total = 50

    # Output Result
    final_rate = calculate_success_rate(completed, total)

    print(f"Mission Analysis:")
    print(f"Tasks Completed: {completed}/{total}")
    print(f"Success Rate: {final_rate}%")

    if final_rate >= 90:
        print("Status: Mission Successful - High Accuracy Maintained.")
    else:
        print("Status: Review Required - Accuracy below threshold.")

if __name__ == "__main__":
    main()
