"""
Library Checkout System — Starter Code

This is a WORKING but poorly designed library system.
Everything is crammed into one class. Your job is to refactor it.

Current features:
- Add items (book, magazine, dvd)
- Check out items to members
- Return items with late fee calculation
- Track member checkouts
"""
import datetime


class Library:
    """
    A library that handles everything in one class.
    Works, but adding new item types or fee rules is painful.
    """

    def __init__(self):
        self.items = {}        # item_id -> dict with all info
        self.checkouts = {}    # member_id -> list of item_ids
        self.late_fee_rate = 0.50  # flat rate per day overdue

    def add_item(self, item_id, title, item_type):
        """
        Add an item to the library.
        item_type: 'book', 'magazine', 'dvd'
        """
        if item_type == "book":
            loan_days = 14
        elif item_type == "magazine":
            loan_days = 7
        elif item_type == "dvd":
            loan_days = 3
        else:
            return None  # Unknown type

        self.items[item_id] = {
            "title": title,
            "type": item_type,
            "loan_days": loan_days,
            "available": True,
            "due_date": None,
            "checked_out_by": None,
        }
        return item_id

    def checkout(self, member_id, item_id):
        """
        Check out an item to a member.
        Returns due_date if successful, None otherwise.
        """
        if item_id not in self.items:
            return None

        item = self.items[item_id]
        if not item["available"]:
            return None  # Already checked out

        due_date = datetime.date.today() + datetime.timedelta(days=item["loan_days"])
        item["available"] = False
        item["due_date"] = due_date
        item["checked_out_by"] = member_id

        if member_id not in self.checkouts:
            self.checkouts[member_id] = []
        self.checkouts[member_id].append(item_id)

        return due_date

    def return_item(self, item_id):
        """
        Return an item. Calculates late fee if overdue.
        Returns late_fee (0.0 if on time), or None if item not found.
        """
        if item_id not in self.items:
            return None

        item = self.items[item_id]
        if item["available"]:
            return None  # Not checked out

        today = datetime.date.today()
        late_fee = 0.0
        if today > item["due_date"]:
            days_late = (today - item["due_date"]).days
            late_fee = days_late * self.late_fee_rate

        member_id = item["checked_out_by"]
        self.checkouts[member_id].remove(item_id)
        item["available"] = True
        item["due_date"] = None
        item["checked_out_by"] = None

        return late_fee

    def get_available_items(self):
        """Returns list of available item_ids."""
        return [item_id for item_id, item in self.items.items() if item["available"]]

    def get_member_checkouts(self, member_id):
        """Returns list of item_ids currently checked out by a member."""
        return self.checkouts.get(member_id, [])
