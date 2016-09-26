#!/usr/bin/env python
# -*- coding: utf-8 -*-

# First file editing:
# 24-09-2016 16h20:45 (UTC+1)
#
# Copyright (c) 2016, Samuel Prevost <samuel.prevost@gmx.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of CanoniPy nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from cmath import *
import sys

try:
    a = complex(sys.argv[1])
    b = complex(sys.argv[2])
    c = complex(sys.argv[3])
except:
    print("Syntaxe: \"python canonipy.py a b c\" \n a, b et c sont les coefficients du polynôme du second degré de forme: \n ax^2 + bx + c \n Les nombres complexes sont notés a + bj avec j^2 = -1 et (a,b) € |R")
    exit()


print "###############################################################################"
print "CanoniPy V1.0 - Par Samuel Prevost"
print "Algorithme de résolution de polynômes du second degré"
print "Avantages:"
print "- Très rapide"
print "- Supporte aussi bien les nombres réels que les nombres complexes"
print "- Permet de tester la concordance de la forme canonique et développée"
print "- Testé et fiable"
print "- Simple d'utilisation"

if a.imag == 0 and b.imag == 0 and c.imag == 0:
    a = a.real
    b = b.real
    c = c.real

print "Propriétés de %sx^2 + %sx +%s :\n" % (a, b, c)

delta = pow(b, 2) - (4 * a * c)
print "Delta = %s" % str(delta)

alpha = -1 * (b / (2 * a))
print "Alpha = %s" % str(alpha)

beta = -1 * (delta / (4 * a))
print "Beta = %s \n" % str(beta)

if alpha.imag == 0 and beta.imag == 0 and delta.imag == 0:
    alpha = alpha.real
    beta = beta.real
    delta = delta.real

canonique = "%s(x - %s)^2 + %s" % (str(a), str(alpha), str(beta))
print "Forme canonique :\n%s" % canonique

r1 = (-b-sqrt(delta))/(2*a)
r2 = (-b+sqrt(delta))/(2*a)

if(delta.real >= 0 and a.imag == 0 and b.imag == 0 and c.imag == 0):
    print "\tRacine 1 = (-%s - sqrt(%s)) / (2*%s) = %s" % (str(b), str(delta), str(a), str(r1.real))
    print "\tRacine 2 = (-%s + sqrt(%s)) / (2*%s) = %s" % (str(b), str(delta), str(a), str(r2.real))
else:
    print "\tAvec j^2 = -1"
    print "\tRacine complexe 1 = (-%s - sqrt(%s)) / (2*%s) = %s" % (str(b), str(delta), str(a), str(r1))
    print "\tRacine complexe 2 = (-%s + sqrt(%s)) / (2*%s) = %s" % (str(b), str(delta), str(a), str(r2))

if delta.real >= 0:
    print "Forme factorisée :\n%s(x - %s)(x - %s)" % (a, str(r1.real), str(r2.real))
else:
    print "Forme factorisée :\n%s(x - %s)(x - %s)" % (a, str(r1), str(r2))

while True:
    x = raw_input("\n\n(Entrez la lettre x pour quitter)\nTestez %sx^2 + %sx +%s pour x = " % (a, b, c))

    if("x" in x):
        exit()

    x = complex(x)
    if(x.imag == 0):
        x = x.real

    cano_result = a * pow((x - alpha),2) + beta
    cano_str = "%s(%s - %s)^2 + %s = %s" % (str(a), str(x), str(alpha), str(beta), str(cano_result))
    print cano_str

    dev_result = a * pow(x, 2) + b * x + c
    dev_str = "%sx%s + %sx%s + %s = %s" % (str(a), str(x), str(b), str(x), str(c), str(dev_result))
    print dev_str

    facto_result = a * (x - r1) * (x - r2)
    if delta.real >= 0:
        print "%s(x - %s)(x - %s) = %s" % (a, str(r1.real), str(r2.real), str(facto_result.real))
    else:
        print "%s(x - %s)(x - %s) = %s" % (a, str(r1), str(r2), str(facto_result))
