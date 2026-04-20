"""
Task Scheduler — Starter Code

A working but rigid task scheduler. Tasks have priorities and get executed
in priority order. That's it. No dependencies, no extensibility.

Your job: refactor this into proper OOP and add task dependencies.
"""
import heapq
from datetime import datetime


class TaskScheduler:
    """
    A priority-based task scheduler.
    Lower priority number = higher priority (runs first).
    """

    #Start assignment

    def __init__(self):
        self._queue = []  # heap of (priority, insertion_order, task_dict)
        self._counter = 0
        self._completed = []
        self._task_lookup = {}  # task_name -> task_dict

    def add_task(self, name, priority, action):
        """
        Add a task to the scheduler.
        name: unique string identifier
        priority: int (lower = more important)
        action: callable to execute
        """
        if name in self._task_lookup:
            return False  # Duplicate

        task = {
            "name": name,
            "priority": priority,
            "action": action,
            "status": "pending",
            "created_at": datetime.now(),
        }
        self._task_lookup[name] = task
        heapq.heappush(self._queue, (priority, self._counter, task))
        self._counter += 1
        return True

    def execute_next(self):
        """Execute the highest priority task. Returns task name or None."""
        while self._queue:
            priority, _, task = heapq.heappop(self._queue)
            if task["status"] != "pending":
                continue  # Skip cancelled tasks

            task["action"]()
            task["status"] = "completed"
            self._completed.append(task)
            return task["name"]

        return None  # Nothing to execute

    def execute_all(self):
        """Execute all pending tasks in priority order. Returns list of task names."""
        executed = []
        while True:
            name = self.execute_next()
            if name is None:
                break
            executed.append(name)
        return executed

    def cancel_task(self, name):
        """Cancel a pending task. Returns True if cancelled, False if not found."""
        if name not in self._task_lookup:
            return False
        task = self._task_lookup[name]
        if task["status"] != "pending":
            return False
        task["status"] = "cancelled"
        return True

    def get_task_status(self, name):
        """Get the status of a task: 'pending', 'completed', 'cancelled', or None."""
        if name not in self._task_lookup:
            return None
        return self._task_lookup[name]["status"]

    def get_pending_tasks(self):
        """Return names of all pending tasks in priority order."""
        pending = [(t["priority"], t["name"]) for t in self._task_lookup.values()
                   if t["status"] == "pending"]
        pending.sort()
        return [name for _, name in pending]
