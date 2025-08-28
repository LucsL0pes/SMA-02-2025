import math

# Linear Congruential Generator parameters
# Using constants from Numerical Recipes
A = 1664525
C = 1013904223
M = 2**32

seed = 42  # initial seed
x = seed
remaining_randoms = 0


def reset_random(seed_value: int, max_numbers: int):
    global seed, x, remaining_randoms
    seed = seed_value
    x = seed
    remaining_randoms = max_numbers


def NextRandom() -> float:
    """Return next pseudo-random number normalized between 0 and 1.

    Raises StopIteration when the pre-defined amount of numbers is exhausted."""
    global x, remaining_randoms
    if remaining_randoms <= 0:
        raise StopIteration("No more random numbers available")
    x = (A * x + C) % M
    remaining_randoms -= 1
    return x / M


def simulate(num_servers: int, capacity: int, arrival_min: float, arrival_max: float,
             service_min: float, service_max: float, seed_value: int,
             max_randoms: int):
    """Simulate a queue system using event scheduling."""

    reset_random(seed_value, max_randoms)

    clock = 0.0
    state_times = [0.0 for _ in range(capacity + 1)]
    customers = 0
    next_arrival = 2.0  # first customer arrives at time 2.0
    departures = []  # list of departure times for customers in service
    losses = 0

    while True:
        # Determine time of next departure
        next_departure = min(departures) if departures else math.inf

        # Choose next event type
        if next_arrival <= next_departure:
            event_time = next_arrival
            state_times[customers] += event_time - clock
            clock = event_time

            # Process arrival
            if customers < capacity:
                customers += 1
                if customers <= num_servers:
                    try:
                        service_time = service_min + (service_max - service_min) * NextRandom()
                    except StopIteration:
                        break
                    departures.append(clock + service_time)
            else:
                losses += 1

            try:
                interarrival = arrival_min + (arrival_max - arrival_min) * NextRandom()
            except StopIteration:
                break
            next_arrival = clock + interarrival
        else:
            event_time = next_departure
            state_times[customers] += event_time - clock
            clock = event_time

            # Process departure
            departures.remove(next_departure)
            customers -= 1
            if customers >= num_servers:
                try:
                    service_time = service_min + (service_max - service_min) * NextRandom()
                except StopIteration:
                    break
                departures.append(clock + service_time)

        if remaining_randoms <= 0:
            break

    total_time = clock
    probabilities = [t / total_time if total_time > 0 else 0.0 for t in state_times]
    return {
        "state_times": state_times,
        "probabilities": probabilities,
        "total_time": total_time,
        "losses": losses,
    }


def format_results(results):
    lines = []
    lines.append(f"Tempo total de simulacao: {results['total_time']:.4f}")
    lines.append(f"Clientes perdidos: {results['losses']}")
    lines.append("Estado\tTempo acumulado\tProbabilidade")
    for idx, (t, p) in enumerate(zip(results["state_times"], results["probabilities"])):
        lines.append(f"{idx}\t{t:.4f}\t{p:.6f}")
    return "\n".join(lines)


if __name__ == "__main__":
    arrival_min, arrival_max = 2.0, 5.0
    service_min, service_max = 3.0, 5.0
    capacity = 5
    max_randoms = 100000

    print("Simulacao G/G/1/5:\n")
    r1 = simulate(num_servers=1, capacity=capacity,
                  arrival_min=arrival_min, arrival_max=arrival_max,
                  service_min=service_min, service_max=service_max,
                  seed_value=42, max_randoms=max_randoms)
    print(format_results(r1))

    print("\nSimulacao G/G/2/5:\n")
    r2 = simulate(num_servers=2, capacity=capacity,
                  arrival_min=arrival_min, arrival_max=arrival_max,
                  service_min=service_min, service_max=service_max,
                  seed_value=42, max_randoms=max_randoms)
    print(format_results(r2))
