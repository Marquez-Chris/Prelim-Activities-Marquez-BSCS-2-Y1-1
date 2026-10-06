class WaitingTicketIterator:
    """Snapshot iterator of tickets that are waiting when the iterator is created."""

    def __init__(self, tickets):
        self._snapshot = [ticket for ticket in tickets if ticket["status"] == "waiting"]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._snapshot):
            raise StopIteration
        ticket = self._snapshot[self._index]
        self._index += 1
        return ticket


class CampusQueueManager:
    PURPOSES = ("Enrollment", "Records", "Payment")
    SERVICE_TYPES = ("regular", "priority")

    def __init__(self):
        self.tickets = []
        self.completed_history = []
        self.counters = [
            {"name": "Counter 1", "ticket": None},
            {"name": "Counter 2", "ticket": None},
        ]
        self.next_number = 1
        self.priority_streak = 0

    def issue_ticket(self, purpose, service_type="regular"):
        purpose = str(purpose).strip().title()
        service_type = str(service_type).strip().lower()

        if purpose not in self.PURPOSES:
            raise ValueError("Invalid purpose. Choose Enrollment, Records, or Payment.")

        if service_type not in self.SERVICE_TYPES:
            raise ValueError("Invalid service type. Choose regular or priority.")

        ticket = {
            "number": self.next_number,
            "purpose": purpose,
            "service_type": service_type,
            "status": "waiting",
        }

        self.tickets.append(ticket)
        self.next_number += 1
        return ticket["number"]

    def issue_many(self, *requests):
        # Validate every request before creating any ticket.
        validated = []

        for request in requests:
            if not isinstance(request, (tuple, list)) or len(request) != 2:
                raise ValueError(
                    "Each request must contain purpose and service type."
                )

            purpose, service_type = request
            purpose = str(purpose).strip().title()
            service_type = str(service_type).strip().lower()

            if purpose not in self.PURPOSES:
                raise ValueError(f"Invalid purpose: {purpose}")
            if service_type not in self.SERVICE_TYPES:
                raise ValueError(f"Invalid service type: {service_type}")

            validated.append((purpose, service_type))

        numbers = []

        for purpose, service_type in validated:
            numbers.append(self.issue_ticket(purpose, service_type))

        return numbers

    def next_ticket(self, waiting=None, priority_streak=None):
        """
        Returns the eligible ticket dictionary, or None if no ticket is eligible.

        Fairness rule:
        - If two priority tickets were served consecutively and a regular ticket
          is waiting, serve the oldest regular ticket.
        - Otherwise, priority goes first when available.
        - Within each type, ticket creation order is preserved.
        """
        if waiting is None:
            waiting = [t for t in self.tickets if t["status"] == "waiting"]

        if priority_streak is None:
            priority_streak = self.priority_streak

        regular = [t for t in waiting if t["service_type"] == "regular"]
        priority = [t for t in waiting if t["service_type"] == "priority"]

        if not regular and not priority:
            return None

        if priority_streak >= 2 and regular:
            return regular[0]

        if priority:
            return priority[0]

        return regular[0]

    def call_next(self):
        free_counter = None

        for counter in self.counters:
            if counter["ticket"] is None:
                free_counter = counter
                break

        if free_counter is None:
            return None, "Both counters are busy."

        waiting = [t for t in self.tickets if t["status"] == "waiting"]
        ticket = self.next_ticket(waiting, self.priority_streak)

        if ticket is None:
            return None, "No waiting tickets."

        ticket["status"] = "served"
        free_counter["ticket"] = ticket["number"]

        if ticket["service_type"] == "priority":
            self.priority_streak += 1
        else:
            self.priority_streak = 0

        return ticket, f"Ticket #{ticket['number']} called to {free_counter['name']}."

    def complete_service(self, ticket_number):
        for counter in self.counters:
            if counter["ticket"] == ticket_number:
                ticket = self.get_ticket(ticket_number)
                if ticket is None:
                    return False, "Ticket not found."

                ticket["status"] = "served"
                self.completed_history.append(ticket.copy())
                counter["ticket"] = None

                return True, f"Ticket #{ticket_number} completed at {counter['name']}."

        for ticket in self.tickets:
            if ticket["number"] == ticket_number and ticket["status"] == "served":
                if any(
                    item["number"] == ticket_number
                    for item in self.completed_history
                ):
                    return False, f"Ticket #{ticket_number} has already been completed."

        return False, f"Ticket #{ticket_number} is not currently being served."

    def cancel_ticket(self, ticket_number):
        ticket = self.get_ticket(ticket_number)

        if ticket is None:
            return False, "Ticket not found."

        if ticket["status"] != "waiting":
            return False, f"Ticket #{ticket_number} cannot be cancelled because it is {ticket['status']}."

        ticket["status"] = "cancelled"
        return True, f"Ticket #{ticket_number} cancelled."

    def get_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket["number"] == ticket_number:
                return ticket
        return None

    def waiting_tickets(self):
        return [t for t in self.tickets if t["status"] == "waiting"]

    def completed_tickets(self):
        return [t for t in self.tickets if t["number"] in
                [x["number"] for x in self.completed_history]]

    def waiting_position(self, ticket_number):
        """
        Estimates a ticket's future waiting position without changing the live queue.

        Position is based on simulated calls, not on actual elapsed time.
        Busy counters are not simulated as time delays; the position means the
        number of eligible service calls ahead of the ticket once a counter is free.
        """
        target = self.get_ticket(ticket_number)

        if target is None or target["status"] != "waiting":
            return None

        queue_copy = [t.copy() for t in self.tickets if t["status"] == "waiting"]
        streak = self.priority_streak
        position = 1

        while queue_copy:
            regular = [t for t in queue_copy if t["service_type"] == "regular"]
            priority = [t for t in queue_copy if t["service_type"] == "priority"]

            if streak >= 2 and regular:
                chosen = regular[0]
            elif priority:
                chosen = priority[0]
            elif regular:
                chosen = regular[0]
            else:
                break

            if chosen["number"] == target["number"]:
                return position

            queue_copy.remove(chosen)

            if chosen["service_type"] == "priority":
                streak += 1
            else:
                streak = 0

            position += 1

        return None

    def show_waiting(self):
        waiting = self.waiting_tickets()

        if not waiting:
            print("\nNo waiting tickets.")
            return

        print("\n========== WAITING TICKETS ==========")

        for position in range(len(waiting)):
            ticket = waiting[position]
            estimate = self.waiting_position(ticket["number"])

            print(
                f"{position + 1}. Ticket #{ticket['number']} | "
                f"{ticket['purpose']} | {ticket['service_type']} | "
                f"Estimated position: {estimate}"
            )

    def show_status(self):
        print("\n========== COUNTER STATUS ==========")

        for counter in self.counters:
            if counter["ticket"] is None:
                print(f"{counter['name']}: FREE")
            else:
                print(f"{counter['name']}: Ticket #{counter['ticket']}")

        print("\n========== COMPLETED HISTORY ==========")

        if not self.completed_history:
            print("No completed services.")
            return

        for ticket in self.completed_history:
            print(
                f"Ticket #{ticket['number']} | "
                f"{ticket['purpose']} | {ticket['service_type']} | SERVED"
            )

    def report(self, **kwargs):
        waiting = sum(t["status"] == "waiting" for t in self.tickets)
        served = len(self.completed_history)
        cancelled = sum(t["status"] == "cancelled" for t in self.tickets)
        free_counters = sum(c["ticket"] is None for c in self.counters)

        print("\n========== SUMMARY REPORT ==========")

        counts = {
            "waiting": waiting,
            "served": served,
            "cancelled": cancelled,
            "free counters": free_counters,
        }

        for key, value in counts.items():
            print(f"{key.title()}: {value}")

        if kwargs:
            print("\nAdditional metadata:")
            for key, value in kwargs.items():
                print(f"{key}: {value}")


def get_ticket_number():
    value = input("Enter ticket number: ").strip()

    try:
        return int(value)
    except ValueError:
        print("Invalid ticket number. Please enter a whole number.")
        return None


def menu_issue(manager):
    print("\n========== ISSUE A TICKET ==========")
    print("Purposes: Enrollment, Records, Payment")

    purpose = input("Enter purpose: ").strip()
    service_type = input("Enter service type (regular/priority): ").strip()

    try:
        number = manager.issue_ticket(purpose, service_type)
        print(f"Ticket #{number} issued successfully.")
    except ValueError as error:
        print(f"Error: {error}")


def menu_call(manager):
    ticket, message = manager.call_next()

    if ticket is None:
        print(f"\n{message}")
    else:
        print(f"\n{message}")
        print(
            f"Purpose: {ticket['purpose']} | "
            f"Type: {ticket['service_type']}"
        )


def menu_complete(manager):
    print("\n========== COMPLETE A SERVICE ==========")
    number = get_ticket_number()

    if number is None:
        return

    success, message = manager.complete_service(number)
    print(message)


def menu_cancel(manager):
    print("\n========== CANCEL A TICKET ==========")
    number = get_ticket_number()

    if number is None:
        return

    success, message = manager.cancel_ticket(number)
    print(message)


def menu_iterator_test(manager):
    print("\n========== WAITING TICKET ITERATOR ==========")

    iterator = WaitingTicketIterator(manager.tickets)

    print("Iterator uses a snapshot of waiting tickets created at initialization.")

    try:
        while True:
            ticket = next(iterator)
            print(
                f"Ticket #{ticket['number']} | "
                f"{ticket['purpose']} | {ticket['service_type']}"
            )
    except StopIteration:
        print("Iterator exhausted. StopIteration was raised.")

    try:
        next(iterator)
    except StopIteration:
        print("Calling next() again correctly raises StopIteration.")


def run_tests():
    print("\n========== RUNNING TESTS ==========")

    # Test 1: ticket numbering
    manager = CampusQueueManager()
    numbers = manager.issue_many(
        ("Enrollment", "regular"),
        ("Records", "priority"),
        ("Payment", "priority"),
    )
    assert numbers == [1, 2, 3]
    print("PASS: Ticket numbering")

    # Test 2: fairness after two priority tickets
    manager.issue_ticket("Enrollment", "regular")
    manager.issue_ticket("Records", "priority")
    manager.issue_ticket("Payment", "priority")

    first, _ = manager.call_next()
    second, _ = manager.call_next()

    # Both counters are busy, so complete one priority service first.
    manager.complete_service(first["number"])

    # Now the fairness rule can select the waiting regular ticket.
    third, _ = manager.call_next()

    assert first["service_type"] == "priority"
    assert second["service_type"] == "priority"
    assert third["service_type"] == "regular"
    print("PASS: Fairness rule")

    # Test 3: both counters busy
    manager = CampusQueueManager()
    manager.issue_ticket("Enrollment", "regular")
    manager.issue_ticket("Records", "regular")
    manager.issue_ticket("Payment", "regular")

    manager.call_next()
    manager.call_next()
    ticket, message = manager.call_next()

    assert ticket is None
    assert message == "Both counters are busy."
    print("PASS: Both counters busy")

    # Test 4: cancellation
    manager = CampusQueueManager()
    manager.issue_ticket("Enrollment", "regular")
    manager.issue_ticket("Records", "regular")

    success, _ = manager.cancel_ticket(1)
    assert success is True

    ticket, _ = manager.call_next()
    assert ticket["number"] == 2
    print("PASS: Cancellation")

    # Test 5: iterator exhaustion
    manager = CampusQueueManager()
    manager.issue_ticket("Payment", "regular")

    iterator = WaitingTicketIterator(manager.tickets)
    next(iterator)

    try:
        next(iterator)
        assert False
    except StopIteration:
        pass

    print("PASS: Iterator exhaustion")

    # Test 6: invalid issue_many does not partially create tickets
    manager = CampusQueueManager()

    try:
        manager.issue_many(
            ("Enrollment", "regular"),
            ("InvalidPurpose", "priority"),
        )
        assert False
    except ValueError:
        pass

    assert len(manager.tickets) == 0
    print("PASS: No partial creation after invalid issue_many")

    print("\nAll tests passed.")


def main():
    manager = CampusQueueManager()

    while True:
        print("\n========================================")
        print("       CAMPUS SERVICE QUEUE MANAGER")
        print("========================================")
        print("1. Issue a ticket")
        print("2. Call the next ticket")
        print("3. Complete a service")
        print("4. Cancel a waiting ticket")
        print("5. Show waiting tickets")
        print("6. Show counter status and completed history")
        print("7. Show a summary report")
        print("8. Exit")
        print("9. Test waiting ticket iterator")
        print("10. Run automated tests")

        choice = input("Select an option: ").strip()

        if choice == "1":
            menu_issue(manager)

        elif choice == "2":
            menu_call(manager)

        elif choice == "3":
            menu_complete(manager)

        elif choice == "4":
            menu_cancel(manager)

        elif choice == "5":
            manager.show_waiting()

        elif choice == "6":
            manager.show_status()

        elif choice == "7":
            manager.report(
                program="Campus Service Queue Manager",
                fairness="Maximum two consecutive priority services",
            )

        elif choice == "8":
            print("Thank you for using the Campus Service Queue Manager.")
            break

        elif choice == "9":
            menu_iterator_test(manager)

        elif choice == "10":
            run_tests()

        else:
            print("Invalid menu choice. Please select 1 to 10.")


if __name__ == "__main__":
    main()
