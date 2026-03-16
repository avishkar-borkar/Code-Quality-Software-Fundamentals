"""
In-Memory Key-Value Store — Starter Code

A working but flat KV store with TTL (time-to-live).
Everything is in one class, no extensibility, no events, no namespaces.
"""
import time
import threading


class KeyValueStore:
    """
    A simple in-memory key-value store with TTL support.
    Keys expire after their TTL elapses.
    """

    def __init__(self):
        self._data = {}       # key -> value
        self._expiry = {}     # key -> expiry_timestamp
        self._lock = threading.Lock()

    def set(self, key, value, ttl=None):
        """
        Set a key-value pair. Optional TTL in seconds.
        If key exists, overwrite it.
        """
        with self._lock:
            self._data[key] = value
            if ttl is not None:
                self._expiry[key] = time.time() + ttl
            elif key in self._expiry:
                del self._expiry[key]

    def get(self, key):
        """
        Get a value by key. Returns None if not found or expired.
        Lazy expiry: checks TTL on access.
        """
        with self._lock:
            if key not in self._data:
                return None
            if key in self._expiry and time.time() > self._expiry[key]:
                del self._data[key]
                del self._expiry[key]
                return None
            return self._data[key]

    def delete(self, key):
        """Delete a key. Returns True if existed, False if not."""
        with self._lock:
            if key not in self._data:
                return False
            del self._data[key]
            if key in self._expiry:
                del self._expiry[key]
            return True

    def exists(self, key):
        """Check if a key exists (and is not expired)."""
        return self.get(key) is not None

    def keys(self):
        """Return all non-expired keys."""
        with self._lock:
            now = time.time()
            valid_keys = []
            expired_keys = []
            for key in self._data:
                if key in self._expiry and now > self._expiry[key]:
                    expired_keys.append(key)
                else:
                    valid_keys.append(key)
            # Clean up expired
            for key in expired_keys:
                del self._data[key]
                del self._expiry[key]
            return valid_keys

    def clear(self):
        """Remove all keys."""
        with self._lock:
            self._data.clear()
            self._expiry.clear()

    def size(self):
        """Return count of non-expired keys."""
        return len(self.keys())
