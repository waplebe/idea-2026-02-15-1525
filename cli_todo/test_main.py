import unittest
import sys
import os
from cli_todo.main import main, load_tasks, save_tasks, add_task, list_tasks, remove_task, mark_complete

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

    def test_remove_invalid_task(self):
        main(["remove", "abc"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_remove_task_out_of_range(self):
        main(["remove", "99"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_add_multiple_tasks(self):
        main(["task1", "task2", "task3"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0], "task1")
        self.assertEqual(tasks[1], "task2")
        self.assertEqual(tasks[2], "task3")
        save_tasks(tasks)

    def test_no_tasks_provided(self):
        main(["add"])
        sys.stdout = None  # Suppress output
        main(["add"])
        sys.stdout = sys.__stdout__
        self.assertEqual(load_tasks(), [])

    def test_persistent_tasks(self):
        main(["task1"])
        main(["list"])
        main(["remove", "1"])
        main(["list"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_empty_file_add_remove(self):
        # Test adding and removing tasks when the file is empty
        main(["add", "task1"])
        main(["remove", "1"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_complete(self):
        main(["add", "task1"])
        main(["complete", "1"])
        tasks = load_tasks()
        self.assertEqual(tasks[0], "[DONE] task1")
        save_tasks(tasks)

    def test_mark_complete_invalid_task(self):
        main(["complete", "abc"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_complete_out_of_range(self):
        main(["complete", "99"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()