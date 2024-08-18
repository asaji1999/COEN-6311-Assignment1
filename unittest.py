import unittest

class TestEventSystem(unittest.TestCase):
    def test_subscription(self):
        event = Event("evt003", "Dev Meetup", "2024-09-15")
        subscriber = Subscriber("sub003", "Carol White", "carol@example.com")

        event.subscribe(subscriber)

        self.assertIn(subscriber, event.subscribers)
        self.assertIn(event.event_id, subscriber.subscribed_events)

    def test_notification(self):
        event = Event("evt004", "Blockchain Summit", "2024-09-20")
        subscriber = Subscriber("sub004", "David Brown", "david@example.com")

        event.subscribe(subscriber)

        with self.assertLogs() as log:
            event.notify_subscribers()
            self.assertIn("Notification to David Brown", log.output[0])

if __name__ == '__main__':
    unittest.main()
