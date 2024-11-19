import counter
import unittest


class TestCounter(unittest.TestCase):
    def test_one_instance(self):
        counter.InstanceCounter.reset()
        instance = counter.InstanceCounter()
        self.assertEqual(instance.id, 1)
    
    def test_two_instances(self):
        counter.InstanceCounter.reset()
        instance1 = counter.InstanceCounter()
        instance2 = counter.InstanceCounter()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
    
    def test_three_instances(self):
        counter.InstanceCounter.reset()
        instance1 = counter.InstanceCounter()
        instance2 = counter.InstanceCounter()
        instance3 = counter.InstanceCounter()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)