#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Androwarn.
#
# Copyright (C) 2012, Thomas Debize <tdebize at mail.com>
# All rights reserved.
#
# Androwarn is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androwarn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androwarn.  If not, see <http://www.gnu.org/licenses/>.

# Global imports
import os
import hashlib
import logging

# Androguard imports
from guard.core.analysis import analysis
from guard.core.bytecodes.apk import *

# Androwarn modules import
from warn.core.core import *
from warn.util.util import *

# Logguer
log = logging.getLogger('log')

# APK and Manifest related functions #
def grab_apk_file_hashes(apk_file) :
    """
        @param apk_file : apk file path (not an apk instance)
    
        @rtype : a list of several hexified hashes
    """
    results = []
        
    block_size=2**20
    
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    
    with open(apk_file,'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
    
    f.close()
    
    results.append("MD5: %s" % md5.hexdigest())
    results.append("SHA-1: %s" % sha1.hexdigest())
    results.append("SHA-256: %s" % sha256.hexdigest())
    
    return results
    

def grab_filename(apk) :
    """
        @param apk : an APK instance
        
        @rtype : the APK's filename
    """
    # Grab only the name.apk, not the full path provided
    return os.path.basename(apk.filename)
