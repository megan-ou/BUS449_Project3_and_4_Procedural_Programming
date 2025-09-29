from unittest import TestCase
from unittest import main

import math

import queues as q


class Test_queues(TestCase):

    def setUp(self):
        self.lamda = 20.0
        self.mu = 25.0
        self.c = 1.0

    def test_is_valid(self):
        lamda = self.lamda
        mu = self.mu
        c = self.c

        # valid single valued lamda
        self.assertEqual(True, q.is_valid(lamda, mu))
        self.assertEqual(True, q.is_valid(lamda, mu, c))
        self.assertEqual(True, q.is_valid(lamda, mu, 2))
        self.assertEqual(True, q.is_valid(25, 20, 1))

        # test with non-positive arguments
        self.assertEqual(False, q.is_valid(0, mu, c))
        self.assertEqual(False, q.is_valid(lamda, 0, c))
        self.assertEqual(False, q.is_valid(lamda, mu, 0))
        self.assertEqual(False, q.is_valid(0, mu, 1))
        self.assertEqual(False, q.is_valid(0, 0, 1))
        self.assertEqual(False, q.is_valid(lamda, 0, 0))
        self.assertEqual(False, q.is_valid(0, mu, 0))
        self.assertEqual(False, q.is_valid(0, 0, 0))

        self.assertEqual(False, q.is_valid(-lamda, mu, c))
        self.assertEqual(False, q.is_valid(lamda, -mu, c))
        self.assertEqual(False, q.is_valid(lamda, mu, -c))
        self.assertEqual(False, q.is_valid(-lamda, -mu, c))
        self.assertEqual(False, q.is_valid(-lamda, mu, -c))
        self.assertEqual(False, q.is_valid(lamda, -mu, -c))
        self.assertEqual(False, q.is_valid(-lamda, -mu, -c))

        # test with non-numeric arguments
        self.assertEqual(False, q.is_valid("twenty", mu, c))
        self.assertEqual(False, q.is_valid(lamda, "25", c))
        self.assertEqual(False, q.is_valid(lamda, mu, "one"))
        self.assertEqual(False, q.is_valid("twenty", "25", c))
        self.assertEqual(False, q.is_valid("twenty", mu, "one"))
        self.assertEqual(False, q.is_valid(lamda, "25", "one"))
        self.assertEqual(False, q.is_valid("twenty", "25", "one"))

        # test valid with multi-valued lamda (or at least lamda a tuple)
        self.assertEqual(True, q.is_valid((5, 10, 5), mu))
        self.assertEqual(True, q.is_valid((5, 10, 5), mu, c))
        self.assertEqual(True, q.is_valid((20,), mu, 1))
        self.assertEqual(True, q.is_valid((20,), mu, 2))

        # test invalid with multi-valued lamda
        self.assertEqual(False, q.is_valid((-5, 10, 5), mu, c))
        self.assertEqual(False, q.is_valid((5, -10, 5), mu, c))
        self.assertEqual(False, q.is_valid((5, 10, -5), mu, c))
        self.assertEqual(False, q.is_valid((-5, -10, 5), mu, c))
        self.assertEqual(False, q.is_valid((-5, 10, -5), mu, c))
        self.assertEqual(False, q.is_valid((5, -10, -5), mu, c))
        self.assertEqual(False, q.is_valid((-5, -10, -5), mu, c))

        self.assertEqual(False, q.is_valid((-5, 10, 5), -mu, c))
        self.assertEqual(False, q.is_valid((5, -10, 5), -mu, c))
        self.assertEqual(False, q.is_valid((5, 10, -5), -mu, c))
        self.assertEqual(False, q.is_valid((-5, -10, 5), -mu, c))
        self.assertEqual(False, q.is_valid((-5, 10, -5), -mu, c))
        self.assertEqual(False, q.is_valid((5, -10, -5), -mu, c))
        self.assertEqual(False, q.is_valid((-5, -10, -5), -mu, c))

        self.assertEqual(False, q.is_valid((-5, 10, 5), mu, -c))
        self.assertEqual(False, q.is_valid((5, -10, 5), mu, -c))
        self.assertEqual(False, q.is_valid((5, 10, -5), mu, -c))
        self.assertEqual(False, q.is_valid((-5, -10, 5), mu, -c))
        self.assertEqual(False, q.is_valid((-5, 10, -5), mu, -c))
        self.assertEqual(False, q.is_valid((5, -10, -5), mu, -c))
        self.assertEqual(False, q.is_valid((-5, -10, -5), mu, -c))


        self.assertEqual(False, q.is_valid((-5, 10, 5), -mu, -c))
        self.assertEqual(False, q.is_valid((5, -10, 5), -mu, -c))
        self.assertEqual(False, q.is_valid((5, 10, -5), -mu, -c))
        self.assertEqual(False, q.is_valid((-5, -10, 5), -mu, -c))
        self.assertEqual(False, q.is_valid((-5, 10, -5), -mu, -c))
        self.assertEqual(False, q.is_valid((5, -10, -5), -mu, -c))
        self.assertEqual(False, q.is_valid((-5, -10, -5), -mu, -c))


    def test_is_feasible(self):

        lamda = self.lamda
        mu = self.mu
        c = self.c

        # test with valid queues, single-valued lamda
        self.assertEqual(True, q.is_feasible(20, 25))
        self.assertEqual(True, q.is_feasible(20, 25, 1))
        self.assertEqual(True, q.is_feasible(20, 25, 2))
        self.assertEqual(False, q.is_feasible(25, 25))
        self.assertEqual(False, q.is_feasible(25, 25, 1))
        self.assertEqual(True, q.is_feasible(25, 25, 2))
        self.assertEqual(False, q.is_feasible(40, 25, 1))
        self.assertEqual(True, q.is_feasible(40, 25, 2))
        self.assertEqual(False, q.is_feasible(50, 25, 2))
        self.assertEqual(True, q.is_feasible(50, 25, 3))

        # test for valid queues, multi-valued lamda
        self.assertEqual(True, q.is_feasible((5, 10, 5), 25))
        self.assertEqual(True, q.is_feasible((5, 10, 5), 25, 1))
        self.assertEqual(True, q.is_feasible((5, 10, 5), 25, 2))
        self.assertEqual(False, q.is_feasible((5, 10, 10), 25))
        self.assertEqual(False, q.is_feasible((5, 10, 10), 25, 1))
        self.assertEqual(True, q.is_feasible((5, 10, 10), 25, 2))
        self.assertEqual(False, q.is_feasible((10, 20, 10), 25, 1))
        self.assertEqual(True, q.is_feasible((10, 20, 10), 25, 2))
        self.assertEqual(False, q.is_feasible((10, 20, 20), 25, 2))
        self.assertEqual(True, q.is_feasible((10, 20, 20), 25, 3))

        # test for invalid queues
        # test for non-positive arguments

        self.assertEqual(False, q.is_valid(0, mu, c))
        self.assertEqual(False, q.is_valid(lamda, 0, c))
        self.assertEqual(False, q.is_valid(lamda, mu, 0))
        self.assertEqual(False, q.is_valid(0, mu, 1))
        self.assertEqual(False, q.is_valid(0, 0, 1))
        self.assertEqual(False, q.is_valid(lamda, 0, 0))
        self.assertEqual(False, q.is_valid(0, mu, 0))
        self.assertEqual(False, q.is_valid(0, 0, 0))

        self.assertEqual(False, q.is_valid(-lamda, mu, c))
        self.assertEqual(False, q.is_valid(lamda, -mu, c))
        self.assertEqual(False, q.is_valid(lamda, mu, -c))
        self.assertEqual(False, q.is_valid(-lamda, -mu, c))
        self.assertEqual(False, q.is_valid(-lamda, mu, -c))
        self.assertEqual(False, q.is_valid(lamda, -mu, -c))
        self.assertEqual(False, q.is_valid(-lamda, -mu, -c))

        # test with non-numeric arguments
        self.assertEqual(False, q.is_feasible("twenty", mu, c))
        self.assertEqual(False, q.is_feasible(lamda, "25", c))
        self.assertEqual(False, q.is_feasible(lamda, mu, "one"))
        self.assertEqual(False, q.is_feasible("twenty", "25", c))
        self.assertEqual(False, q.is_feasible("twenty", mu, "one"))
        self.assertEqual(False, q.is_feasible(lamda, "25", "one"))
        self.assertEqual(False, q.is_feasible("twenty", "25", "one"))

        # test valid with multi-valued lamda (or at least lamda a tuple)
        self.assertEqual(True, q.is_feasible((5, 10, 5), mu))
        self.assertEqual(True, q.is_feasible((5, 10, 5), mu, c))
        self.assertEqual(True, q.is_feasible((20,), mu, 1))
        self.assertEqual(True, q.is_feasible((20,), mu, 2))

        # test invalid with multi-valued lamda
        self.assertEqual(False, q.is_feasible((-5, 10, 5), mu, c))
        self.assertEqual(False, q.is_feasible((5, -10, 5), mu, c))
        self.assertEqual(False, q.is_feasible((5, 10, -5), mu, c))
        self.assertEqual(False, q.is_feasible((-5, -10, 5), mu, c))
        self.assertEqual(False, q.is_feasible((-5, 10, -5), mu, c))
        self.assertEqual(False, q.is_feasible((5, -10, -5), mu, c))
        self.assertEqual(False, q.is_feasible((-5, -10, -5), mu, c))
        self.assertEqual(False, q.is_feasible((5, 10, 5), -mu, c))
        self.assertEqual(False, q.is_feasible((5, 10, 5), mu, -c))
        self.assertEqual(False, q.is_feasible((5, 10, 5), -mu, -c))
        self.assertEqual(False, q.is_feasible((-5, 10, 5), -mu, -c))

    # def test_calc_lq_mm1(self):
    #
    #     self.assertAlmostEqual(3.2, q.calc_lq_mm1(20,25))
    #     self.assertAlmostEqual(math.inf, q.calc_lq_mm1(25,25))
    #     self.assertTrue(math.isnan(q.calc_lq_mm1(0,25)))
    #     self.assertTrue(math.isnan(q.calc_lq_mm1(20,0)))
    #     self.assertTrue(math.isnan(q.calc_lq_mm1(0,0)))


    def test_calc_p0(self):

        lamda = self.lamda
        mu = self.mu
        c = self.c

        # test for valid queues, single valued lamda
        self.assertAlmostEqual(0.2, q.calc_p0(20, 25, 1))
        self.assertAlmostEqual(0.4, q.calc_p0(15, 25))
        self.assertAlmostEqual(0.0345423, q.calc_p0(65, 25, 3))


        # test for invalid queues
        self.assertTrue(math.isnan(q.calc_p0(0, 25, 1)))
        self.assertTrue(math.isnan(q.calc_p0(20, 0, 1)))
        self.assertTrue(math.isnan(q.calc_p0(20, 25, 0)))
        self.assertTrue(math.isnan(q.calc_p0(0, 0, 1)))
        self.assertTrue(math.isnan(q.calc_p0(0, 25, 0)))
        self.assertTrue(math.isnan(q.calc_p0(20, 0, 0)))
        self.assertTrue(math.isnan(q.calc_p0(0, 0, 0)))

        self.assertTrue(math.isnan(q.calc_p0(-lamda, mu, c)))
        self.assertTrue(math.isnan(q.calc_p0(lamda, -mu, c)))
        self.assertTrue(math.isnan(q.calc_p0(lamda, mu, -c)))
        self.assertTrue(math.isnan(q.calc_p0(-lamda, -mu, c)))
        self.assertTrue(math.isnan(q.calc_p0(-lamda, mu, -c)))
        self.assertTrue(math.isnan(q.calc_p0(lamda, -mu, -c)))
        self.assertTrue(math.isnan(q.calc_p0(-lamda, -mu, -c)))

        # test for infeasible queues
        self.assertTrue(math.isinf(q.calc_p0(lamda, lamda, c)))
        self.assertTrue(math.isinf(q.calc_p0(mu, mu, c)))
        self.assertTrue(math.isinf(q.calc_p0(2 * lamda, mu, c)))
        self.assertTrue(math.isinf(q.calc_p0((5, 10, 5), lamda, c)))

        # test for valid queues, multi-valued lamda
        self.assertAlmostEqual(0.2, q.calc_p0((5, 10, 5), 25, 1))
        self.assertAlmostEqual(0.4, q.calc_p0((2, 3, 10), 25))
        self.assertAlmostEqual(0.0345423, q.calc_p0((15, 20, 30), 25, 3))



    def test_calc_lq_mmc(self):

        lamda = self.lamda
        mu = self.mu
        c = self.c

        # test valid results
        self.assertAlmostEqual(3.2, q.calc_lq_mmc(20, 25))
        self.assertAlmostEqual(3.2, q.calc_lq_mmc(20, 25, 1))
        self.assertAlmostEqual(2.8444, q.calc_lq_mmc(40, 25, 2), 4)
        self.assertAlmostEqual(0.8889, q.calc_lq_mmc(50, 25, 3), 4)
        self.assertAlmostEqual(1.0002, q.calc_lq_mmc(70, 25, 4), 4)
        self.assertAlmostEqual(46.8439, q.calc_lq_mmc(98, 25, 4), 4)

        # test invalid results

        self.assertTrue(math.isnan(q.calc_lq_mmc(0, 25, 1)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(20, 0, 1)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(20, 25, 0)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(0, 0, 1)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(0, 25, 0)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(20, 0, 0)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(0, 0, 0)))

        self.assertTrue(math.isnan(q.calc_lq_mmc(-lamda, mu, c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(lamda, -mu, c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(lamda, mu, -c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(-lamda, -mu, c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(-lamda, mu, -c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(lamda, -mu, -c)))
        self.assertTrue(math.isnan(q.calc_lq_mmc(-lamda, -mu, -c)))

        # test infeasible queues
        self.assertTrue(math.isinf(q.calc_lq_mmc(lamda, lamda, c)))
        self.assertTrue(math.isinf(q.calc_lq_mmc(mu, mu, c)))
        self.assertTrue(math.isinf(q.calc_lq_mmc(2 * lamda, mu, c)))
        self.assertTrue(math.isinf(q.calc_lq_mmc((5, 10, 5), lamda, c)))

        # test valid results with multiple classes
        self.assertAlmostEqual(3.2, q.calc_lq_mmc((5, 10, 5), 25, 1))
        self.assertAlmostEqual(2.8444, q.calc_lq_mmc((10, 15, 15), 25, 2), 4)
        self.assertAlmostEqual(0.8889, q.calc_lq_mmc((10, 20, 20), 25, 3), 4)
        self.assertAlmostEqual(1.0002, q.calc_lq_mmc((20, 20, 30), 25, 4), 4)
        self.assertAlmostEqual(46.8439, q.calc_lq_mmc((40, 58), 25, 4), 4)


# suite = unittest.TestSuite([Test_queues()])

if __name__ == '__main__':
    rslt = main(verbosity=2, exit=False)
    #Qprint(rslt)

    print('done')






