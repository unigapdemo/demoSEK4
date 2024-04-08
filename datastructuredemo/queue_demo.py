class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)


class EventRegistrationSystem:
    def __init__(self):
        self.queue = Queue()

    def register_event(self, participant):
        self.queue.enqueue(participant)
        print(f"{participant} đã đăng ký sự kiện.")

    def process_registration(self):
        if not self.queue.is_empty():
            participant = self.queue.dequeue()
            print(f"{participant} đã xác nhận tham dự sự kiện.")
        else:
            print("Không có ai đăng ký sự kiện.")

# Sử dụng hệ thống đăng ký sự kiện
event_system = EventRegistrationSystem()
event_system.register_event("Nguyen")
event_system.register_event("Tran")
event_system.register_event("Hoang")

event_system.process_registration()
event_system.process_registration()
event_system.process_registration()
event_system.process_registration()
