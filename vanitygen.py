# -*- coding: utf-8 -*-
#
#    coineva vanitygen.py
#    Copyright (C) 2016 February 
#    1200 Web Development
#    http://1200wd.com/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
# from bitcoin import *
from bitcoinlib.keys import HDKey
import timeit
import random
import multiprocessing


witness_type = 'segwit'

def address_search(search_for='bc1q2345'):
    privkey = random.randrange(2**256)
    address = ''
    count = 0
    start = timeit.default_timer()

    print("Searching for %s (pid %s)" % (search_for, os.getpid()))

    while not search_for in address:
        privkey += 1
        # pubkey_point = fast_multiply(G, privkey)
        # address = pubkey_to_address(pubkey_point)
        k = HDKey(witness_type=witness_type)
        address = k.address()
        count += 1
        if not count % 10000:
            print("Searched %d in %d seconds (pid %d)" % (count, timeit.default_timer()-start, os.getpid()))

    print("Found address %s" % address)
    print("Private key HEX %s" % k.private_hex)
    return((address, k.private_hex))


def main():
    # print(multiprocessing.cpu_count())
    processors = 8
    print("Starting %d processes" % processors)
    ps = []
    for i in range(processors):
        print("Starting process %d" % i)
        p = multiprocessing.Process(target=address_search)
        p.start()
        ps.append(p)
        # pipein, pipeout = os.pipe()
        # pid = os.fork()
        # if pid == 0:
        #     os.close(pipein)
        #     address_search(pipeout)
        # else:
        #     pipein = os.fdopen(pipein)
            # while True:
            #     line = os.read(pipein, 32)
            #     print(line)

    # print(ps)
    # print('Main process exiting')


main()
