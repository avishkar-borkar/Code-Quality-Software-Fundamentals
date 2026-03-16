"""
Parking Lot System — Starter Code

This is a WORKING but poorly designed parking lot.
Everything is crammed into one class. Your job is to refactor it
and extend it with new features.

Current features:
- Park vehicles (car, motorcycle, truck)
- Different spot sizes (small, medium, large)
- Entry/exit tracking
"""
import time


class ParkingLot:
    """
    A parking lot that handles everything in one class.
    Works, but adding new features will be painful.
    """

    def __init__(self, small_spots, medium_spots, large_spots):
        self.spots = {}
        spot_id = 1
        for _ in range(small_spots):
            self.spots[spot_id] = {"size": "small", "vehicle": None, "entry_time": None}
            spot_id += 1
        for _ in range(medium_spots):
            self.spots[spot_id] = {"size": "medium", "vehicle": None, "entry_time": None}
            spot_id += 1
        for _ in range(large_spots):
            self.spots[spot_id] = {"size": "large", "vehicle": None, "entry_time": None}
            spot_id += 1

        self.vehicle_spot_map = {}  # license_plate -> spot_id
        self.rate_per_hour = 2.0  # flat rate

    def park_vehicle(self, license_plate, vehicle_type):
        """
        Park a vehicle. Returns spot_id if successful, None if lot is full.
        vehicle_type: 'motorcycle', 'car', 'truck'
        """
        if license_plate in self.vehicle_spot_map:
            return None  # Already parked

        # Determine which spot sizes this vehicle can use
        if vehicle_type == "motorcycle":
            allowed_sizes = ["small", "medium", "large"]
        elif vehicle_type == "car":
            allowed_sizes = ["medium", "large"]
        elif vehicle_type == "truck":
            allowed_sizes = ["large"]
        else:
            return None  # Unknown vehicle type

        # Find first available spot of allowed size (prefer smallest fit)
        for spot_id, spot in self.spots.items():
            if spot["vehicle"] is None and spot["size"] in allowed_sizes:
                spot["vehicle"] = {
                    "license_plate": license_plate,
                    "vehicle_type": vehicle_type,
                }
                spot["entry_time"] = time.time()
                self.vehicle_spot_map[license_plate] = spot_id
                return spot_id

        return None  # No spot available

    def remove_vehicle(self, license_plate):
        """
        Remove a vehicle and calculate the fee.
        Returns (spot_id, fee) or None if vehicle not found.
        """
        if license_plate not in self.vehicle_spot_map:
            return None

        spot_id = self.vehicle_spot_map[license_plate]
        spot = self.spots[spot_id]

        # Calculate fee
        hours = (time.time() - spot["entry_time"]) / 3600
        hours = max(1, round(hours))  # Minimum 1 hour
        fee = hours * self.rate_per_hour

        # Clear the spot
        spot["vehicle"] = None
        spot["entry_time"] = None
        del self.vehicle_spot_map[license_plate]

        return spot_id, fee

    def get_available_spots(self):
        """Returns count of available spots by size."""
        counts = {"small": 0, "medium": 0, "large": 0}
        for spot in self.spots.values():
            if spot["vehicle"] is None:
                counts[spot["size"]] += 1
        return counts

    def is_full(self):
        """Check if all spots are occupied."""
        return all(spot["vehicle"] is not None for spot in self.spots.values())

    def get_vehicle_info(self, license_plate):
        """Get info about a parked vehicle."""
        if license_plate not in self.vehicle_spot_map:
            return None
        spot_id = self.vehicle_spot_map[license_plate]
        spot = self.spots[spot_id]
        return {
            "license_plate": license_plate,
            "vehicle_type": spot["vehicle"]["vehicle_type"],
            "spot_id": spot_id,
            "spot_size": spot["size"],
            "entry_time": spot["entry_time"],
        }
