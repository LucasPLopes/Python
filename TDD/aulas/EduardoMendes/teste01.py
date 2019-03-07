from unittest import TestCase, main


def soma(x,y):
	return x+y

def sub(x,y):
	return x-y

def mux(x,y):
	return x*y

class Testes(TestCase):
	def test_soma(self):
		self.assertLessEqual(soma(5,5),10)
		
	def test_sub(self):
		self.assertEqual(sub(5,5),2,'não passou')
	


if __name__ == '__main__':
	main()
