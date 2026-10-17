import unittest

from task_tracker.tasks import add_task, complete_task, delete_task


class TaskOperationsTests(unittest.TestCase):
    def test_add_task_assigns_next_id(self):
        tasks = [{"id": 1, "description": "Existing", "completed": False}]
        add_task(tasks, "New task")
        self.assertEqual(tasks[-1]["id"], 2)
        self.assertEqual(tasks[-1]["description"], "New task")

    def test_complete_task(self):
        tasks = [{"id": 1, "description": "Test", "completed": False}]
        self.assertTrue(complete_task(tasks, 1))
        self.assertTrue(tasks[0]["completed"])

    def test_delete_task(self):
        tasks = [{"id": 1, "description": "Test", "completed": False}]
        self.assertTrue(delete_task(tasks, 1))
        self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()
