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
from bitcoinlib.keys import HDKey
import timeit
import random
import multiprocessing


witness_type = 'segwit'

def address_search(search_for='l200wd'):
    global witness_type
    privkey = random.randrange(2**256)
    address = ''
    count = 0
    start = timeit.default_timer()

    bech32 = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
    base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    is_bech32 = True
    is_base58 = True
    for letter in search_for:
        if letter not in bech32:
            is_bech32 = False
        if letter not in base58:
            is_base58 = False
    if not (is_bech32 or is_base58):
        raise ValueError(f"This is not a valid base58 or bech32 search string: {search_for}")
    if is_base58 and not is_bech32:
        witness_type = 'p2sh-segwit'

    print(f"Searching for {search_for}, witness_type is {witness_type} (pid {os.getpid()})")

    while not search_for in address:
        privkey += 1
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

    # print(ps)
    # print('Main process exiting')


main()
