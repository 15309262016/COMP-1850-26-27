# Week 1.6, Session 1: Task 5

from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level: ")
period = input("Enter time period: ")

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)
dataset.read_feed()

strongest = dataset.strongest_quake()

print(f"{len(dataset)} quakes, from {feed}")
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")
print()
print(f"Strongest quake occurred at {strongest.when.strftime('%H:%M:%S')} on {strongest.when.strftime('%Y-%m-%d')}")
print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
print(f"The depth was {strongest.depth} km")
print(f"The magnitude was {strongest.magnitude}")
