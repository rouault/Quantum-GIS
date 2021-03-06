# -*- coding: utf-8 -*-
#
#   Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
#    All rights reserved.
#
#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are met:
#        * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#        * Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#        * Neither the name of the  Simon Edwards <simon@simonzone.com> nor the
#        names of its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#
#    THIS SOFTWARE IS PROVIDED BY Simon Edwards <simon@simonzone.com> ''AS IS'' AND ANY
#    EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#    DISCLAIMED. IN NO EVENT SHALL Simon Edwards <simon@simonzone.com> BE LIABLE FOR ANY
#    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# FindPyQt.py
# Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

import os.path
import PyQt5.QtCore

try:
    __import__('sipbuild')
except ImportError:
    import sipconfig  # won't work for SIP v5
    import sys

    cfg = sipconfig.Configuration()
    sip_dir = cfg.default_sip_dir
    for p in (os.path.join(sip_dir, "PyQt5"),
              os.path.join(sip_dir, "PyQt5-3"),
              sip_dir,
              os.path.join(cfg.default_mod_dir, "PyQt5", "bindings")):
        if os.path.exists(os.path.join(p, "QtCore", "QtCoremod.sip")):
            sip_dir = p
            break
    cfg = {
        'pyqt_mod_dir': os.path.join(cfg.default_mod_dir, "PyQt5"),
        'pyqt_sip_dir': sip_dir,
        'pyqt_bin_dir': cfg.default_bin_dir,
    }
else:  # Code for SIP v5
    from distutils.sysconfig import get_python_lib
    import shutil
    cfg = {
        'pyqt_mod_dir': os.path.dirname(PyQt5.__file__),
        'pyqt_sip_dir': os.path.join(get_python_lib(plat_specific=1), "PyQt5", "bindings"),
        'pyqt_bin_dir': os.path.dirname(shutil.which("pyuic5")),
    }

print("pyqt_version:%06.0x" % PyQt5.QtCore.PYQT_VERSION)
print("pyqt_version_num:%d" % PyQt5.QtCore.PYQT_VERSION)
print("pyqt_version_str:%s" % PyQt5.QtCore.PYQT_VERSION_STR)

pyqt_version_tag = ""
in_t = False
pyqt_config_list = PyQt5.QtCore.PYQT_CONFIGURATION["sip_flags"].split(' ')
for item in pyqt_config_list:
    if item == "-t":
        in_t = True
    elif in_t:
        if item.startswith("Qt_5"):
            pyqt_version_tag = item
    else:
        in_t = False
print("pyqt_version_tag:%s" % pyqt_version_tag)

print("pyqt_mod_dir:%s" % cfg['pyqt_mod_dir'])
print("pyqt_sip_dir:%s" % cfg['pyqt_sip_dir'])
print("pyqt_sip_flags:%s" % PyQt5.QtCore.PYQT_CONFIGURATION['sip_flags'])
print("pyqt_bin_dir:%s" % cfg['pyqt_bin_dir'])

try:
    import PyQt5.sip

    print("pyqt_sip_module:PyQt5.sip")
except:
    print("pyqt_sip_module:sip")
