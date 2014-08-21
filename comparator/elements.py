
class ElementMixin():
	def get_label(self):
		raise NotImplementedError

class TopicMixin(ElementMixin):
	def get_answers(self):
		raise NotImplementedError

class AnswerMixin(ElementMixin):
	def get_topic(self):
		raise NotImplementedError
