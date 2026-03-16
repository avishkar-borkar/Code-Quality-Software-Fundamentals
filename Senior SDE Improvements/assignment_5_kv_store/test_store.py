"""
Tests for the extended Key-Value Store.
DO NOT MODIFY THIS FILE.
"""
import pytest
import time


# ============================================================
# PART A — Core KV Store (refactored with proper encapsulation)
# ============================================================

class TestCoreKVStore:
    """Basic KV operations should work."""

    def test_set_and_get(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("name", "Alice")
        assert store.get("name") == "Alice"

    def test_get_nonexistent_key(self):
        from store import KeyValueStore
        store = KeyValueStore()
        assert store.get("nope") is None

    def test_overwrite_key(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("name", "Alice")
        store.set("name", "Bob")
        assert store.get("name") == "Bob"

    def test_delete_key(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("name", "Alice")
        assert store.delete("name") is True
        assert store.get("name") is None

    def test_delete_nonexistent(self):
        from store import KeyValueStore
        store = KeyValueStore()
        assert store.delete("nope") is False

    def test_exists(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("a", 1)
        assert store.exists("a") is True
        assert store.exists("b") is False

    def test_keys(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)
        store.set("c", 3)
        assert set(store.keys()) == {"a", "b", "c"}

    def test_clear(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)
        store.clear()
        assert store.size() == 0

    def test_size(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)
        assert store.size() == 2


class TestTTL:
    """TTL (time-to-live) support."""

    def test_key_expires(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("temp", "value", ttl=0.1)
        time.sleep(0.15)
        assert store.get("temp") is None

    def test_key_alive_before_expiry(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("temp", "value", ttl=10)
        assert store.get("temp") == "value"

    def test_expired_key_not_in_keys(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("temp", "value", ttl=0.1)
        store.set("perm", "value")
        time.sleep(0.15)
        assert "temp" not in store.keys()
        assert "perm" in store.keys()

    def test_overwrite_removes_ttl(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.set("key", "val1", ttl=0.1)
        store.set("key", "val2")  # No TTL — should persist
        time.sleep(0.15)
        assert store.get("key") == "val2"


# ============================================================
# PART B — Namespaces
# ============================================================

class TestNamespaces:
    """Namespaces isolate keys into separate logical groups."""

    def test_create_namespace(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("users")
        assert ns is not None

    def test_namespace_set_and_get(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("users")
        ns.set("alice", {"age": 30})
        assert ns.get("alice") == {"age": 30}

    def test_namespaces_are_isolated(self):
        """Same key in different namespaces should not conflict."""
        from store import KeyValueStore
        store = KeyValueStore()
        users = store.create_namespace("users")
        config = store.create_namespace("config")
        users.set("name", "Alice")
        config.set("name", "MyApp")
        assert users.get("name") == "Alice"
        assert config.get("name") == "MyApp"

    def test_namespace_delete(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("cache")
        ns.set("key", "value")
        assert ns.delete("key") is True
        assert ns.get("key") is None

    def test_namespace_keys(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("data")
        ns.set("a", 1)
        ns.set("b", 2)
        assert set(ns.keys()) == {"a", "b"}

    def test_namespace_does_not_affect_root(self):
        """Namespace keys should not appear in root store."""
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("cache")
        ns.set("cached_item", "value")
        store.set("root_item", "value")
        assert "cached_item" not in store.keys()
        assert "root_item" in store.keys()

    def test_namespace_clear(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("temp")
        ns.set("a", 1)
        ns.set("b", 2)
        ns.clear()
        assert ns.size() == 0

    def test_namespace_size(self):
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("data")
        ns.set("a", 1)
        ns.set("b", 2)
        assert ns.size() == 2

    def test_namespace_ttl(self):
        """TTL should work within namespaces too."""
        from store import KeyValueStore
        store = KeyValueStore()
        ns = store.create_namespace("cache")
        ns.set("temp", "val", ttl=0.1)
        time.sleep(0.15)
        assert ns.get("temp") is None

    def test_get_namespace_returns_same_instance(self):
        """Getting the same namespace twice should return the same object."""
        from store import KeyValueStore
        store = KeyValueStore()
        ns1 = store.create_namespace("data")
        ns2 = store.create_namespace("data")
        ns1.set("key", "value")
        assert ns2.get("key") == "value"

    def test_list_namespaces(self):
        from store import KeyValueStore
        store = KeyValueStore()
        store.create_namespace("users")
        store.create_namespace("config")
        assert set(store.list_namespaces()) == {"users", "config"}


# ============================================================
# PART C — Event Listeners (Observer Pattern)
# ============================================================

class TestEventListeners:
    """Event system: subscribe to set, delete, and expire events."""

    def test_on_set_fires(self):
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("set", lambda key, value: events.append(("set", key, value)))
        store.set("name", "Alice")
        assert events == [("set", "name", "Alice")]

    def test_on_delete_fires(self):
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("delete", lambda key: events.append(("delete", key)))
        store.set("name", "Alice")
        store.delete("name")
        assert ("delete", "name") in events

    def test_on_expire_fires(self):
        """Expire event should fire when a key is accessed after TTL."""
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("expire", lambda key: events.append(("expire", key)))
        store.set("temp", "val", ttl=0.1)
        time.sleep(0.15)
        store.get("temp")  # This triggers lazy expiry
        assert ("expire", "temp") in events

    def test_multiple_listeners(self):
        from store import KeyValueStore
        store = KeyValueStore()
        events1 = []
        events2 = []
        store.on("set", lambda key, value: events1.append(key))
        store.on("set", lambda key, value: events2.append(key))
        store.set("a", 1)
        assert events1 == ["a"]
        assert events2 == ["a"]

    def test_off_removes_listener(self):
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        handler = lambda key, value: events.append(key)
        store.on("set", handler)
        store.set("a", 1)
        store.off("set", handler)
        store.set("b", 2)
        assert events == ["a"]  # "b" was not captured

    def test_events_include_overwrites(self):
        """Overwriting a key should fire a set event."""
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("set", lambda key, value: events.append((key, value)))
        store.set("a", 1)
        store.set("a", 2)
        assert events == [("a", 1), ("a", 2)]

    def test_namespace_events_on_root(self):
        """Events from namespace operations should bubble up to root store with namespace prefix."""
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("set", lambda key, value: events.append(("set", key, value)))
        ns = store.create_namespace("cache")
        ns.set("item", "value")
        # Should fire with namespaced key
        assert len(events) == 1
        assert events[0] == ("set", "cache:item", "value")

    def test_delete_nonexistent_no_event(self):
        """Deleting a key that doesn't exist should NOT fire delete event."""
        from store import KeyValueStore
        store = KeyValueStore()
        events = []
        store.on("delete", lambda key: events.append(key))
        store.delete("nope")
        assert events == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
