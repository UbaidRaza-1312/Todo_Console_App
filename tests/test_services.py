import unittest
from console.models import Task
from console.services import TaskService

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.service = TaskService()

    def test_add_task(self):
        task = self.service.add_task("Buy groceries", "Milk, Eggs")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Buy groceries")
        self.assertEqual(task.description, "Milk, Eggs")
        self.assertFalse(task.status)
        self.assertEqual(task.id, 1)
        self.assertEqual(len(self.service.get_all_tasks()), 1)

        with self.assertRaises(ValueError):
            self.service.add_task("")
        with self.assertRaises(ValueError):
            self.service.add_task("  ")

    def test_get_all_tasks(self):
        self.assertEqual(len(self.service.get_all_tasks()), 0)
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.assertEqual(len(self.service.get_all_tasks()), 2)

    def test_get_task_by_id(self):
        task1 = self.service.add_task("Task 1")
        task_retrieved = self.service.get_task_by_id(task1.id)
        self.assertEqual(task_retrieved.title, "Task 1")
        self.assertIsNone(self.service.get_task_by_id(999))

    def test_update_task(self):
        task = self.service.add_task("Task to update")
        updated_task = self.service.update_task(task.id, title="Updated Title", status=True)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertTrue(updated_task.status)

        with self.assertRaises(ValueError):
            self.service.update_task(999, title="Non Existent")
        with self.assertRaises(ValueError):
            self.service.update_task(task.id, title="")

    def test_delete_task(self):
        task1 = self.service.add_task("Task 1")
        self.assertEqual(len(self.service.get_all_tasks()), 1)
        self.service.delete_task(task1.id)
        self.assertEqual(len(self.service.get_all_tasks()), 0)
        with self.assertRaises(ValueError):
            self.service.delete_task(999)

    def test_toggle_task_status(self):
        task = self.service.add_task("Task to toggle")
        self.assertFalse(task.status)
        
        toggled_task = self.service.toggle_task_status(task.id)
        self.assertTrue(toggled_task.status)
        
        toggled_task_again = self.service.toggle_task_status(task.id)
        self.assertFalse(toggled_task_again.status)

        with self.assertRaises(ValueError):
            self.service.toggle_task_status(999)

if __name__ == '__main__':
    unittest.main()
