import tensorflow as tf
import hyperchamber as hc
import hypergan as hg
import numpy as np
from hypergan.losses.lamb_gan_loss import LambGanLoss
from hypergan.ops import TensorflowOps

from unittest.mock import MagicMock
from tests.mocks import mock_graph

loss_config = {'test': True, 'reduce':'reduce_mean', 'labels': [0,1,0], 'label_smooth': 0.3, 'alpha': 0.2, 'beta': 0.1}
class LambGanLossTest(tf.test.TestCase):
    def test_config(self):
        with self.test_session():
            loss = LambGanLoss(hg.GAN(), loss_config)
            self.assertTrue(loss.config.test)

    def test_create(self):
        with self.test_session():
            graph = mock_graph()
            gan = hg.GAN(graph=graph)
            gan.create()
            loss = LambGanLoss(gan, loss_config)
            d_loss, g_loss = loss.create()
            d_shape = loss.ops.shape(d_loss)
            g_shape = loss.ops.shape(g_loss)
            self.assertEqual(d_shape, [1])
            self.assertEqual(g_shape, [1])

if __name__ == "__main__":
    tf.test.main()
