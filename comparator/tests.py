import unittest
from comparator import Comparator
from comparator.elements import TopicMixin, AnswerMixin

class ComparatorTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test_instanciate(self):
		comparator = Comparator()
		self.assertTrue(comparator)


class TopicMixinTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test_instanciate(self):
		topic = TopicMixin()
		self.assertTrue(topic)

	def test_it_is_a_non_implemented_mixin(self):
		topic = TopicMixin()
		with self.assertRaises(NotImplementedError):
			topic.get_label()
		with self.assertRaises(NotImplementedError):
			topic.get_answers()


class AnswerMixinTestCase(unittest.TestCase):
	def test_instanciate(self):
		answer = AnswerMixin()
		self.assertTrue(answer)

	def test_it_is_a_non_implemented_mixin(self):
		answer = AnswerMixin()
		with self.assertRaises(NotImplementedError):
			answer.get_label()
		with self.assertRaises(NotImplementedError):
			answer.get_topic()
