import unittest
import sys
import os
from cli_todo.main import main, load_tasks, save_tasks, add_task, list_tasks, remove_task, mark_complete, prioritize_task

class TestMain(unittest.TestCase):

    def setUp(self):
        # Create a temporary data file for testing
        self.temp_data_file = "temp_todo.json"
        with open(self.temp_data_file, "w") as f:
            json.dump([], f, indent=4)

    def tearDown(self):
        # Remove the temporary data file
        if os.path.exists(self.temp_data_file):
            os.remove(self.temp_data_file)

    def test_add_task(self):
        main(["task1"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "task1")
        save_tasks(tasks)

    def test_list_tasks(self):
        main(["list"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_remove_task(self):
        main(["remove", "1"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_complete(self):
        main(["complete", "1"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "[DONE] task1")
        save_tasks(tasks)

    def test_prioritize_task_high(self):
        main(["prioritize", "1", "high"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "* High: task1")
        save_tasks(tasks)

    def test_prioritize_task_medium(self):
        main(["prioritize", "1", "medium"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "* Medium: task1")
        save_tasks(tasks)

    def test_prioritize_task_low(self):
        main(["prioritize", "1", "low"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "* Low: task1")
        save_tasks(tasks)

    def test_invalid_priority(self):
        main(["prioritize", "1", "invalid"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "* Low: task1") # Should still be low priority

    def test_invalid_task_number(self):
        main(["remove", "abc"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_invalid_task_number_complete(self):
        main(["complete", "abc"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_add_multiple_tasks(self):
        main(["task1", "task2", "task3"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertIn("task1", tasks)
        self.assertIn("task2", tasks)
        self.assertIn("task3", tasks)

if __name__ == '__main__':
    unittest.main()