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
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select E1 Instant
netedit.changeAdditional("instantInductionLoop")

# create E1 Instant with default parameters
netedit.leftClick(match, 200, 250)

# set a invalid  frequency (dummy)
netedit.modifyAdditionalDefaultValue(2, "dummyFrequency")

# try to create E1 Instant with invalid frequency
netedit.leftClick(match, 250, 250)

# set a invalid  frequency
netedit.modifyAdditionalDefaultValue(2, "-30")

# try to create E1 Instant with invalid frequency
netedit.leftClick(match, 250, 250)

# set a valid frequency
netedit.modifyAdditionalDefaultValue(2, "150")

# try to create E1 Instant with valid frequency
netedit.leftClick(match, 250, 250)

# set invalid filename
netedit.modifyAdditionalDefaultValue(3, "&&&&&&&&")

# try to create E1 Instant with invalid filename
netedit.leftClick(match, 300, 250)

# set valid filename
netedit.modifyAdditionalDefaultValue(3, "myOwnFilename.txt")

# create E1 Instant with valid filename
netedit.leftClick(match, 300, 250)

# set invalid vehicle type
netedit.modifyAdditionalDefaultValue(4, "dummy vehicles")

# try to create E1 Instant with invalid vehicle types
netedit.leftClick(match, 350, 250)

# set valid vehicle type
netedit.modifyAdditionalDefaultValue(4, "private passenger taxi bus")

# create E1 Instant with valid vehicle types
netedit.leftClick(match, 350, 250)

# Change friendlyPos
netedit.modifyAdditionalDefaultBoolValue(5)

# create E1 Instant with different split by type
netedit.leftClick(match, 400, 250)

# Check undo redo
netedit.undo(match, 5)
netedit.redo(match, 5)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
