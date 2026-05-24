from typing import List, Dict

def heapify(arr: List[Dict], n: int, i: int, key: str):
    """Maintains the max-heap property for match dictionaries based on a specific key."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][key] > arr[largest][key]:
        largest = left

    if right < n and arr[right][key] > arr[largest][key]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heapsort_matches(matches: List[Dict], sort_key: str = "efficiency_score") -> List[Dict]:
    """
    Sorts a list of match dictionaries in descending order using Heapsort.
    Perfect for finding peak performance matches in O(n log n) time.
    """
    n = len(matches)
    sorted_matches = matches.copy()

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_matches, n, i, sort_key)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        sorted_matches[i], sorted_matches[0] = sorted_matches[0], sorted_matches[i]
        heapify(sorted_matches, i, 0, sort_key)

    # Reverse to get descending order (highest score first)
    return sorted_matches[::-1]