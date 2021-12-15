import sys
from os.path import dirname, abspath, join
sys.path.append(abspath(join(dirname(__file__), "../../..")))
from sgad.cgn.models.cgn import CGN
from sgad.cgn.models.discriminator import DiscLin, DiscConv
from sgad.cgn.models.classifier import CNN

__all__ = [
    CGN, DiscLin, DiscConv, CNN
]