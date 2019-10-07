=============
vmod_boltsort
=============

**important note: this vmod is obsolete as its goals can be achieved using the .querysort() function of vmod_std (bundled with Varnish)**

-----------------------
Varnish boltsort Module
-----------------------

:Author: Naren Venkataraman
:Date: 2012-09-01
:Version: 1.0
:Manual section: 3

SYNOPSIS
========

At Vimeo we use Varnish Cache to cache our player traffic. It has
worked out great for us.

Varnish at this point has no built in module to sort querystrings.  
Say I have two of these:

* /video/48088296?title=0&byline=0&portrait=0&color=51a516
* /video/48088296?byline=0&color=51a516&portrait=0&title=0

Boltsort sorts the querystring and ensures that Varnish treats the
above one and the same.

DESCRIPTION
===========

The boltsort Varnish vmod sorts querystring.

* Insertion sort on tokenized querystring params makes it twice as fast as current qsort implementations
* Custom param compare instead of storing param lengths for each querystring param means lesser stack usage


FUNCTIONS
=========

sort
-----

Prototype
        ::

                sort(STRING S)
Return value
	STRING
Description
	Returns url with querystring sorted
Example
        ::

                set req.url = boltsort.sort(req.url);

INSTALLATION
============
Same as libvmod-example installation instructions

Usage::

 yum install python-docutils or apt-get install python-docutils
 ./autogen.sh
 ./configure [VMODDIR=DIR]

Optionally you can also set the vmod install directory by adding
`VMODDIR=DIR` (defaults to the pkg-config discovered directory from your
Varnish installation).

Make targets:

* make - builds the vmod
* make install - installs your vmod in `VMODDIR`
* make check - runs the unit tests in ``src/tests/*.vtc``

In your VCL you could then use this vmod along the following lines::
        
        import boltsort;

        sub vcl_hash {
                # sort the querysting and use the sorted one for hashing
                set req.url = boltsort.sort(req.url);
        }

COPYRIGHT
=========

This document is licensed under the same license as the
libvmod-boltsort project. See LICENSE for details.

* Copyright (c) 2012 Vimeo
