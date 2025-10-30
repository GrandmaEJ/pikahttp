import time
import sys
import urllib.request
import statistics
from typing import List, Callable
import requests
import pikahttp

from tests.mock_server import MockServer

server = MockServer()
TEST_URL = f"{server.start()}/get"
NUM_REQUESTS = 100


def print_progress(current: int, total: int, label: str = "") -> None:
    """Print a progress bar.

    Args:
        current (int): Current progress value
        total (int): Total value for 100% progress
        label (str): Label to show next to the progress bar
    """
    bar_width = 40
    progress = float(current) / total
    filled = int(bar_width * progress)
    bar = "=" * filled + "-" * (bar_width - filled)
    percentage = int(progress * 100)
    sys.stdout.write(f"\r{label} [{bar}] {percentage}% ({current}/{total})")
    sys.stdout.flush()
    if current == total:
        print()


def measure_time(func: Callable) -> float:
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time


async def measure_time_async(func: Callable) -> float:
    start_time = time.time()
    await func()
    end_time = time.time()
    return end_time - start_time


def benchmark_urllib():
    urllib.request.urlopen(TEST_URL).read()


def benchmark_requests():
    requests.get(TEST_URL)


def benchmark_pikahttp():
    session = pikahttp.Session()
    response = session.request(
        "GET", TEST_URL, headers={"User-Agent": "pikahttp-benchmark/0.1.0"}
    )
    response["content"]  # Content is already downloaded


def run_benchmarks():
    # Warm up
    print("Warming up...")
    for _ in range(5):
        benchmark_urllib()
        benchmark_requests()
        benchmark_pikahttp()

    print(f"\nRunning benchmarks ({NUM_REQUESTS} requests each)...")

    # urllib benchmarks
    urllib_times: List[float] = []
    print("\nBenchmarking urllib...")
    for i in range(NUM_REQUESTS):
        time_taken = measure_time(benchmark_urllib)
        urllib_times.append(time_taken)
        print_progress(i + 1, NUM_REQUESTS, "urllib")

    # requests benchmarks
    requests_times: List[float] = []
    print("\nBenchmarking requests...")
    for i in range(NUM_REQUESTS):
        time_taken = measure_time(benchmark_requests)
        requests_times.append(time_taken)
        print_progress(i + 1, NUM_REQUESTS, "requests")

    # pikahttp benchmarks
    pikahttp_times: List[float] = []
    print("\nBenchmarking pikahttp...")
    for i in range(NUM_REQUESTS):
        time_taken = measure_time(benchmark_pikahttp)
        pikahttp_times.append(time_taken)
        print_progress(i + 1, NUM_REQUESTS, "pikahttp")

    # Calculate statistics
    def calc_stats(times: List[float]) -> tuple:
        return (
            statistics.mean(times),
            statistics.median(times),
            min(times),
            max(times),
            statistics.stdev(times),
        )

    urllib_stats = calc_stats(urllib_times)
    requests_stats = calc_stats(requests_times)
    pikahttp_stats = calc_stats(pikahttp_times)

    # Print results
    print("\nResults:")
    print("-" * 80)
    print(
        f"{'Library':<15} {'Mean (s)':<12} {'Median (s)':<12} {'Min (s)':<12} {'Max (s)':<12} {'StdDev (s)':<12}"
    )
    print("-" * 80)
    print(
        f"urllib         {urllib_stats[0]:<12.4f} {urllib_stats[1]:<12.4f} {urllib_stats[2]:<12.4f} {urllib_stats[3]:<12.4f} {urllib_stats[4]:<12.4f}"
    )
    print(
        f"requests       {requests_stats[0]:<12.4f} {requests_stats[1]:<12.4f} {requests_stats[2]:<12.4f} {requests_stats[3]:<12.4f} {requests_stats[4]:<12.4f}"
    )
    print(
        f"pikahttp      {pikahttp_stats[0]:<12.4f} {pikahttp_stats[1]:<12.4f} {pikahttp_stats[2]:<12.4f} {pikahttp_stats[3]:<12.4f} {pikahttp_stats[4]:<12.4f}"
    )
    print("-" * 80)

    # Calculate and print speed improvements
    pikahttp_mean = pikahttp_stats[0]
    urllib_speedup = (urllib_stats[0] / pikahttp_mean - 1) * 100
    requests_speedup = (requests_stats[0] / pikahttp_mean - 1) * 100

    print("\nSpeed Improvements:")
    print(f"pikahttp is {urllib_speedup:.1f}% faster than urllib")
    print(f"pikahttp is {requests_speedup:.1f}% faster than requests")


if __name__ == "__main__":
    try:
        print("Starting HTTP Client Benchmarks")
        print("=" * 60)
        run_benchmarks()
    finally:
        server.stop()
