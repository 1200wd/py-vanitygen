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

from bitcoin import *
import timeit
import random


def main():
    privkey = random.randrange(2**256)
    search_for = '12oo'
    address = ''
    count = 0
    start = timeit.default_timer()
    pubkey_point = ''

    while not search_for.upper() in address.upper():
        pubkey_point = fast_multiply(G, privkey)
        pubkey_bin = encode_pubkey(pubkey_point, 'bin')
        address = pubkey_to_address(pubkey_bin)
        privkey += 1
        count += 1
        if not count % 1000:
            print "Searched %d in %d seconds" % (count, timeit.default_timer()-start)

    print "Found adress %s" % address
    print "Private key is %s" % encode_pubkey(pubkey_point, 'hex')


if __name__ == '__main__':
    main()
