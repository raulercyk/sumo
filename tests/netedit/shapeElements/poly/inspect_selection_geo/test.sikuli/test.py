#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# apply zoom (to see all POIS)
netedit.setZoom("0", "0", "100")

# go to select mode
netedit.selectMode()

# select all using invert
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect POIs
netedit.leftClick(match, 350, 100)

# Set invalid color
netedit.modifyAttribute(1, "Jren")

# Set valid color
netedit.modifyAttribute(1, "green")

# change fill
netedit.modifyBoolAttribute(2)

# Set invalid layer
netedit.modifyAttribute(3, "dummyLayer")

# Set layer
netedit.modifyAttribute(3, "1")

# Set type
netedit.modifyAttribute(4, "common type")

# Set invalid imgfile
netedit.modifyAttribute(5, "paris.ico")

# Set empty imgfile
netedit.modifyAttribute(5, "")

# Set imgfile
netedit.modifyAttribute(5, "berlin_icon.ico")

# change save relative path
netedit.modifyBoolAttribute(6)

# Set invalid angle
netedit.modifyAttribute(7, "dummyAngle")

# Set valid angle
netedit.modifyAttribute(7, "180")

# change use geo
netedit.modifyBoolAttribute(9)

# change block move
netedit.modifyBoolAttribute(13)

# change block shape
netedit.modifyBoolAttribute(14)

# change close
netedit.modifyBoolAttribute(15)

# go to select mode
netedit.selectMode()

# clear selection
netedit.selectionClear()

# Check undos and redos
netedit.undo(match, 15)
netedit.redo(match, 15)

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
