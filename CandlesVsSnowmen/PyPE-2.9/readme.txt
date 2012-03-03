
.. raw:: html

    <style type="text/css">
    pre.literal-block {
        background-color: rgb(192, 192, 255);
        margin: 0cm 1.5cm 0cm 1.5cm;
    }
    </style>

=================================================
Readme/Help for PyPE (Python Programmer's Editor)
=================================================

.. contents:: Table of Contents

-------------------------------
License and Contact information
-------------------------------
http://pype.sourceforge.net
http://come.to/josiah

PyPE is copyright 2003-2006 Josiah Carlson.
Contributions are copyright their respective authors.

This software is licensed under the GPL (GNU General Public License) version 2
as it appears here: http://www.gnu.org/copyleft/gpl.html
It is also included with this archive as `gpl.txt <gpl.txt>`_.

The portions of STCStyleEditor.py included in StyleSetter.py, which is used to
support styles, was released under the wxWindows license and is copyright (c)
2001 - 2002 Riaan Booysen.  The wxWindows license and the LGPL license it
references are included with this software as `wxwindows.txt <wxwindows.txt>`_
and `lgpl.txt <lgpl.txt>`_.

The included stc-styles.rc.cfg was modified from the original version in order
to not cause exceptions during style changes, as well as adding other language
style definitions, and was originally distributed with wxPython version
2.4.1.2 for Python 2.2 .

If you do not also receive a copy of `gpl.txt <gpl.txt>`_,
`wxwindows.txt <wxwindows.txt>`_, and `lgpl.txt <lgpl.txt>`_ with your version
of this software, please inform me of the violation at either web page at the
top of this document.

------------
Requirements
------------

Either a machine running Python and wxPython, or a Windows machine that can
run the binaries should be sufficient.  Initial revisions of PyPE were
developed on a PII-400 with 384 megs of ram, but it should work on any machine
that can run the most recent wxPython revisions.  Some portions may be slow
(when using Document->Wrap Long Lines especially, which is a known issue with
the scintilla text editor control), but it should still be usable.

PyPE 2.x has been tested on Python 2.3 and wxPython 2.6.3.0.  It should work
on later versions of Python and wxPython.  If you are having issues, file a
bug report on http://sourceforge.net/projects/pype .

------------
Installation
------------

If you have Python 2.3 or later as well as wxPython 2.6.3 or later, you can
extract PyPE-X.Y.Z-src.zip anywhere and run it by double-clicking on pype.py
or pype.pyw .  Note that the 2.6.3.3 ansi build of wxPython has issues with
pasting, so use some other ansi build, or even the 2.6.3.3 unicode build.

If you don't have Python 2.3 wxPython 2.6.3 or later, and are running Windows,
you should (hopefully) be able to run the Windows binaries.  They are provided
for your convenience (so you don't have to install Python and wxPython).

At the current time, the Windows binaries are constructed with Python 2.3 and
wxPython 2.6.3.0 .  I have considered moving to Python 2.5 or even 2.4 with
wxPython 2.8, but switching to Python 2.4 with wxPython 2.6.x adds 700k to the
binary distribution, and going with Python 2.5 and wxPython 2.8 (there are
currently no wxPython 2.6.3.* releases for Python 2.5) adds 2.2 megs to the
binary distribution, some of which is the Python 2.4-2.5 size difference, much
of it being the necessity to include the gdi plus dll for non-XP/Vista
platforms, and even the MSVC 7.1 runtime.  While many users have copies of
both of these runtimes *somewhere* on their system, PyPE cannot rely on them
being accessable (on my machine only the MSVC 7.1 runtime is in a system path,
while the gdi plus dll is in about a dozen places).

If it so happens that the Windows binaries don't work for you, and you have an
installation of Python and wxPython that fits the requirements, why don't you
run the source version?  The only difference is a pass through py2exe, and a
minor loading time speed increase.  Just because the Windows binaries exist,
doesn't mean that you /have/ to run them.  If you have a Python and wxPython
installation, you should have the necessary dlls to make PyPE run (Python is
shipped with the 7.1 runtime, and wxPython 2.7+ ships with the gdi plus dll).

Why doesn't the Windows install work?
=====================================
Depending on your platform, it may or may not work.  It works for me on
Windows 2k and XP.  Most problems people have is that they mistakenly extract
library.zip, which they shouldn't do (and in recent PyPE binary releases
may not be able to do).  It could also be due to the lack of some DLL, in
which case an error message should inform you of which DLL you are missing.


Why doesn't PyPE work on Linux?
===============================
PyPE 2.5+ has been tested on Ubuntu 6.06 with...

* python-wxversion_2.6.1.2ubuntu2_all.deb

* libwxgtk2.6-0_2.6.1.2ubuntu2_i386.deb

* python-wxgtk2.6_2.6.1.2ubuntu2_i386.deb

And 

* libwxgtk2.7-0_2.7.1.3-0_i386.deb

* python-wxgtk2.7_2.7.1.3-0_i386.deb

The only anomalies observed so far is seemingly a bug with some
wx.ScrolledPanel uses (which have been replaced in more recent releases), and
when using a pure Kubuntu install (installed via the Kubuntu install, and not
Ubuntu + Kubuntu core via synaptic), there may be errors and/or warnings
during PyPE startup.  I have not been able to crash PyPE yet, so I presume it
is stable.  I have recently switched to using Ubuntu + Kubuntu core + Xubuntu
core, and I haven't noticed any of aforementioned errors.

There have previously been reports of PyPE segfaulting in certain Linux
distributions when opening a file.  This seems to be caused by icons in the
file listing in the 'Documents' tab on the right (or left) side of the editor
(depending on your preferences), or by icons in the notebook tabs along the
top of the editor.  It was due to either the platform not being able to find
the icons to display, or the icons being improperly sized.  You can disable
these icons by starting up PyPE, going to Options->Use Icons, and making sure
that it is unchecked.  You should restart PyPE to make sure that the setting
sticks.  PyPE will be uglier, but it should work.  I believe that this has
been fixed in PyPE 2.4.1 and later, but this documentation persists "just in
case".


Why isn't the most recent PyPE available as deb or RPM?
=======================================================
Short answer: it's a pain in the ass.

Longer answer: I'm not the maintainer for the PyPE package in any of the
Ubuntu repositories, but have recently discovered that PyPE has a newer
maintainer.  Whether or not the new maintainer keeps PyPE up-to-date is up to
him.  Personal attempts to create .debs have resulted in utter failure, which
I can either blame on a personal failure to comprehend the documentation, or a
failure in the documentation to impart the necessary information.  Either way,
you are going to have to wait for the debian/ubuntu/whatever repositories to
update, or you can get the most recent PyPE from
http://sourceforge.net/projects/pype and extract it wherever you desire.  I'm
a fan of ~/apps/PyPE, but choose what you will.

I'm not going to package any RPMs for PyPE, primarily because I'm not going to
install the RPM build/install stuff into Ubuntu.  Recent attempts to get
bdist_wininst working in such a way that the results don't mangle Python
installations have failed, and this experience leads me to believe that
bdist_rpm has similar issues.  Essentially, you are on your own with regards
to rpm packages.


Why doesn't PyPE work on OSX?
=============================
Aside from "PyPE works on OSX" (or "almost works") from 2 users, I don't know
what may be causing PyPE to not work in OSX.  If you send bug reports with
tracebacks, etc., we can probably figure out what is going on and how we can
fix it.

In the summer of 2008, I actually had an OS X laptop to use mid June 2008 to
late August 2008.  I did my best to improve PyPE, but because of how slow PyPE
is on OS X (I believe it is caused by the way the editor control is wrapped on
OS X with wxPython), I actually abandoned the platform.  PyPE inside an Ubuntu
or Windows virtual machine (Virtual Box or Parallels are both good) works
well on OS X.

--------------------
Command Line Options
--------------------

--last
======
When PyPE is run with the '--last' command line option, PyPE will attempt to
load all documents that were opened the last time you shut down PyPE.  This is
equivalent to starting up PyPE and using File->Open Last .

--unicode and --ansi
====================
If PyPE is started up with the --unicode or --ansi command line options, it
will attempt to use the unicode or ansi versions of wxPython respectively.  On
failure, it will display to the user with a failure notice.  These options
have no effect on the Windows distributions of PyPE, or wherever 
``hasattr(sys, 'frozen')`` is true.

--fontsize
==========
If you provide ``--fontsize=12``, PyPE will change the font size for all open
documents to 12.  The default font size that PyPE uses is 10.  If you want
text to be bigger, use a number larger than 10.  If you want text to be
smaller, use a number smaller than 10.  The line number margin will be scaled
proportional to the font size specified.

--font
======
If you provide ``--font=Lucida-Console``, PyPE will change the font for all
open documents to "Lucida Console".  The default font that PyPE uses is
Courier New.

--nothread
==========
This command line option will disable the threaded parser, which has caused
problems on some platforms.  This will reduce the accuracy of the tools in
the "Tools" menu, due to the faster and not necessarily correct parser being
used in its place.

--macros
========
PyPE 2.6 has what I would consider to be a fully-functioning macro system.
The Python 2.5 ``--macros`` command line option is now ignored because macros
are enabled by default in 2.6+.

--standalone
============
Providing this command line option will use the path in which the PyPE source
or binary is for where PyPE's state is saved (document history, menu
configuration, etc.).  This will allow for 'embedded' applications.

--port
======
Providing this command line option will allow you to choose the port number
that PyPE uses when Options -> One PyPE is checked.  The default port number
is 9999.

--use_old_parser
================
This uses the old parser (PyPE 2.8.8 and a few revisions prior).  It is faster
than the modern parser, but it's not as accurrate, nor does it provide all of
the scope introspection capabilities that the new compiler.ast-based parser
does.


-------------------------------
PyPE features and functionality
-------------------------------

What to expect when coming from other editors/IDEs
==================================================
While PyPE has quite a few of the features that one would expect from an IDE,
I do not consider PyPE to be an IDE; I consider PyPE to be an editor.  The
semantic difference between the two in my mind is a bit wishy-washy, so I'll
not bore you with the details.  In any case:

1. Hitting F5 will not run your Python, nor compile the latex, nor compile the
   C/C++, nor open a browser for the HTML.  It will (by default) refresh the
   browsable source trees and other tools.  You can change hotkeys, and in
   particular, the (new in PyPE 2.8) 'File -> Run Current File' menu item.
   For .py and .pyw files, 'Run Current File' will use the Python specified in
   the lower part of 'Options -> Shell Options' to run your Python source,
   capturing the output and allowing interaction.  For .htm, .html, .shtm and
   .shtml, PyPE will try to use your system defined default web browser to
   open the file.  For .tex files, PyPE will attempt to run pdflatex on them.

2. If PyPE seems complicated when you are first starting out, hide all of the
   optional features; 'Options -> Layout Options -> Show Wide Tools', 'Show
   Tall Tools', and '(toolbar) Hide'.  Start editing.  If it isn't doing what
   you want/expect it to, check the 'Document' menu for per-document settings
   or the 'Options' menu for other editor-wide options.  Want to change
   hotkeys?  Use 'Options -> Change Menus and Hotkeys' .

3. PyPE is not going to gain a debugger any time soon, if ever.  I agree with
   many of you that debuggers can be useful, but aside from attempting to
   steal Idle's or some other project's remote debugger and making it work in
   PyPE, 1) I wouldn't know where to begin, 2) it may kill bookmark
   indicators, 3) I find that print statements are sufficient for me, 4) I
   have not had sufficient desire to make it happen.

4. PyPE is not like every other editor you have ever used.  It may share some
   features, but it is likely just a bit different.  Before you freak out and
   email me with, "PyPE sux, go find something else to do with your time
   newb! lols" spend some time looking for the feature in the menus, the
   various tabs, etc.  You may find that your desired feature is available.
   Again note that if the key bindings are not to your liking, you can change
   them with 'Options -> Change Menus and Hotkeys' for all the menus.  Macros
   are handled a bit differently, which you will find out by hitting the
   'hotkey' button in the Macros tab.

5. PyPE has macros.  These macros can record what you do with the keyboard and
   some menu actions, then play them back.  You can also use them to
   programmatically edit the document you are working on, including the
   handling of 'code snippets'.  Look at the macro help below and the samples
   included with PyPE (including the failure conditions).



Encoding detection for opening files
====================================
If you are using the Unicode version of PyPE, when opening a file, PyPE will
attempt to decode your file using the following encodings in order:

1. The encoding specified by the BOM, if any (PyPE writes BOMs for UTF-*
   encodings by default).

2. Encodings specified by "coding directives" in the first two lines of
   source, if any.

3. Ascii (only allows for values from 0...127)

4. Latin-1/iso-8859-1 (allows for values 0...255)

If options 1-3 above fail, then 4 will succeed, but may not necessarily
display the correct content, and may cause corruption if you were to save the
document.

In 2.6.3 and earlier, PyPE would try 1, 2, then 3, but not 4.

Note that PyPE does not default to assuming XML or HTML files are UTF-8 as per
spec: http://www.w3.org/TR/2000/REC-xml-20001006#NT-EncodingDecl due to
backwards compatability concerns with PyPE 2.6.3 and earlier. Users desiring
UTF-8 decoding support should make sure that their xml/html files include a
UTF-8 encoding directive or BOM at the beginning of their file, which is
recommended for all xml/html anyways.


Encoding detection for saving files
===================================
If you are using the Unicode version of PyPE, when saving a file, PyPE will
attempt to encode your file using the following encodings in order:

1. Any encoding specified by the Document -> Encodings menu option (note that
   a specification of 'other' will be ignored, and will assume the existence
   of a "coding" directive.

2. Encodings specified by "coding directives" in the first two lines of
   source, if any.

3. Ascii (only allows for values from 0...127)

4. Latin-1/iso-8859-1 (allows for values 0...255)

5. UTF-8

If options 1-4 above fail, 5 will succeed.  If the first encoding option does
not succeed: say, for instance, that you have specified "other" as the
Document -> Encodings option, then used the iso-8859-9 coding declaration for
Turkish, but included some Arabic letters in a comment somewhere (possibly an
unlikely occurrence, I don't know, but this is an example), PyPE will inform
you that your intended encoding (iso-8859-9) does not match the first encoding
to succeed (UTF-8), and ask you if it is ok to continue.

In 2.6.3 and earlier, PyPE would try 1, 2, 3, then 5.


What is a "coding directive"?
=============================
If in the first two lines of your source file (all initial blank lines being
ignored), the following regular expression matches something::
    
    [cC][oO][dD][iI][nN][gG][=:](?:["'\s]*)([-\w.]+)

... then you have a properly specified "coding directive".  This regular
expression was intended to match things like::

    # -*- coding: ENCODING_NAME -*-
    # -*- cOdInG: ENCODING-NAME -*-
    # vim:fileencoding=ENCODING_NAME
    <?xml version='1.0' encoding='ENCODING-NAME' ?>

... in [X]Emacs or Vim style encoding declarations for Python source, or
XML-style declarations in XML or HTML source.


Shells
======
PyPE includes the ability to open up Python or command shells.  See the File
menu.  To choose which Python is used in the "New Python Shell" or "Run
Selected Code", see "Options -> Shell Options".

When using "New Python shell" or the "Run Selected Code", you may notice that
when you run wxPython code, any initial wx.Frame.Show() calls may not actually
show the frame on Windows.  To work around this, use a .Show(), followed by a
.Hide(), followed by a .Show() again.  This should work around the issue on
Windows platforms.

When using "Run Selected Code", PyPE will try to find some open Python shell.
If one is not found, PyPE will open a new Python shell using the Python
specified in "Options -> Shell Options".  PyPE will then send the selected
code to the Python shell after reindenting it.

When using "Run Current File", PyPE will try to find a currently unused output
document that was previously created.  If it cannot find one, it will open a
new output document and use that.

Note: as of May 2009, though shells work, there are some bugs, and seem to
have become quite slow.  There are some things I've been meaning to do to
improve their functionality, but I've not had time (in over 2 years).


Vim options
===========
When opening up a file that you have never opened before, or whose history you
have cleared by closing and removing it from the "Recently Open" list in the
Documents tab, PyPE will scan the first and last 20 lines of the file for
comments (see the Todo stuff below for what constitutes a comment), then check
for :set commands.  If :set commands are found, only cul, nocul, et, noet, sw,
sts, ts, and their aliases (including 'inv' prefix or '!' suffix for toggles,
and both '=' and ':' assignment operators for values) are used to set the
preferences in the Document menu.

If there exists both sw and sts options, sw will be preferred.


Using Options -> Realtime Options for syntax checking and tool updates
======================================================================
Syntax checking is always enabled for Python shells, and will highlight the
first line with an error as you type (it is actually checks shortly after you
stop typing), using the same indicator as defined in Options -> Shell Options.

Syntax checking for Python source files is only enabled if you have chosen a
delay in the Options -> Realtime Options submenu.  If your file is fewer than
200,000 bytes long, it will take max(SYNTAX_CHECK_TIME, 1)\*CHOICE_IN_SECONDS,
and wait that long after you have stopped using your keyboard, etc., to check
the syntax, indicating the first error, if any, using the same indicator as
defined in Options -> Shell Options.

Automatic source tree rebuilding for the Name and Line tools, entries for the
Filter tool, Todo listing, autocomple entries, and calltips is only enabled if
you have chosen a delay for update tools in the Options -> Realtime Options
submenu.  Otherwise you need to use Document -> Refresh (or the equivalent key
binding).  Similar to syntax checking above, it will take max(REFRESH_TIME, 1)
\*CHOICE_IN_SECONDS, and wait that long after you have stopped using your
keyboard, etc., to do the automatic Document -> Refresh call.

Note that PyPE will only check syntax or rebuild the tree if the content has
changed since the last time either operation was scheduled.


What is Sloppy Cut/Copy?
========================
When selecting multiple lines for a cut/copy operation, Sloppy Cut/Copy will
select the entirety of partially selected lines.  This saves the user from
having to meticulously select the start and end points of multi-line
selections.


What is Smart Paste?
====================
Smart Paste is two functionalities in one.

1. When pasting multiple lines into a currently indented region, it will
   reindent the pasted region such that the least indented line of the pasted
   region matches the current indentation level, all other indent levels being
   relative to the current/minimum.

2. When the cursor is in a non-indent portion of a line, and you paste, Smart
   Paste will automatically paste to the next line, indenting one level deeper
   as necessary if you had selected the start of a new block (like if, for,
   while, def, etc., for Python, open curly braces '{' in C, etc.).


What do the different options in the Filter tool do?
====================================================

subsequence
    will match things like ``us.et`` to ``UserString.ExpandTabs``

score
    when subsequence is defined, will score the matches and show the best
    matches at the top of the list

no context
    will not provide any context in the display or search

long
    will provide a 'verbose' display and search context, like
    ``class foo: def bar(self)`` 

short
    will provide a concise display and search context, like
    ``def foo.bar(self)``

exact
    will find entries that include *exactly* what you typed in.

any
    will find entries that include *any* of the 'words' you provide.

all
    will find the entries that include *all* of the 'words' you provide

Given the following three definitions and the ``no context`` option without
subsequence searching::

    def abc(ghi, jkl)
    def jkl(mno, pqr)
    def stu(vwx, yz)

...the following searches are true::

    exact 'def abc' -> #1
    any 'def abc' -> #1, #2, #3
    all 'def abc' -> #1
    
    exact 'abc ghi' -> Nothing
    any 'abc ghi' -> #1
    all 'abc ghi' -> #1
    
    exact 'jkl stu' -> Nothing
    any 'jkl stu' -> #1, #2, #3
    all 'jkl stu' -> Nothing

With the new parser introduced in PyPE 2.9, line count information should be
fairly precise.


How do I update the default settings for a particular document type?
====================================================================
1. Close all open documents of the particular type whose default settings you
   want to update.

2. Create or open a document of the specific document type that you want to
   change the settings of.

3. Adjust all of the settings in the "Document" menu to those settings that
   you want to be the default when you open up that particular kind of
   document.

4. Use "Options -> Save Settings" and choose the particular language whose
   settings you would like to save.

5. If in the future, a particular document of that type does not have the
   proper settings, use "Options -> Load Settings" to load the defaults for
   that specific language.

In PyPE 2.6.3 and later, whenever a document shares the default settings for
its file type and is closed, those settings aren't explicitly saved, under the
assumption that you would prefer to have it use the default settings directly.
If you are going to change the default settings for all documents of a
specific type, follow the above 5 steps.


Dictionaries and alphabets for the Spell checker
================================================
You can create/delete custom dictionaries via the +/- buttons right next to
the "Custom Dictionaries:" section.  You can add words to these custom
dictionaries by "Check"ing your document for misspellings, checking all of the
words you want to add, clicking "+ ./", then choosing the custom dictionary
you want the words added to.

If you want to use a large primary dictionary, create a 'dictionary.txt' file
that is utf-8 encoded, and place it into the same path that PyPE is.  This
will be far faster for startup, shutdown, and creating the list than manually
adding all of the words to custom dictionaries.  Fairly reasonable word lists
for english (British, Canadian, or American) are available at Kevin's Word 
list page: http://wordlist.sourceforge.net/ Words should be separated by any
standard whitespace character (spaces, tabs, line endings, etc.).

If you want to customize the alphabet that PyPE uses for suggesting spelling,
you can create an 'alphabet.txt' file that is utf-8 encoded, where alphabet
characters separated by commas ',', and place it into the same path that PyPE
is.

Please note that the spell checker is very simple.  After discovering "words",
which are contiguous sequences of letters, suggestions are created by removing
single letters, inserting single letters, and swapping pairs of letters
internally.  It then checks these suggestions against the user-supplied
dictionaries, and any that match become suggestions.


How does "One PyPE" work?
=========================
If "One PyPE" is selected, it will remove the file named 'nosocket' from the
path in which PyPE is running from (if it exists), and start a listening
socket on 127.0.0.1:9999 .  If "One PyPE" is deselected, it will create a file
called 'nosocket' in the path from which PyPE is running, and close the
listening socket (if one was listening).

Any new PyPE instances which attempt to open will check for the existence of
the nosocket file.  If it does not find that file, it will attempt to create a
new listening socket on 127.0.0.1:9999 .  If the socket creation fails, it
will attempt to connect to 127.0.0.1:9999 and send the documents provided on
the command-line to the other PyPE instance.  If it found the file, or if it
was able to create the socket, then a new instance of PyPE will be created,
and will use the preferences-defined "One PyPE" (preventing certain issues
involving a read-only path which PyPE is on, or a read-only nosocket file).

If you want to prevent new instances of PyPE from ever creating or using
sockets, create a file called 'nosocket' and make it read-only to PyPE.


What the heck is a Trigger?
===========================
Let us say that you writing a web page from scratch.  Let us also say that
typing in everything has gotten a bit tiresome, so you want to offer yourself
a few macro-like expansions, like 'img' -> '<img src="">'.

1. Go to: Document->Set Triggers.

2. Click on 'New Trigger'.

3. In the 'input' column of the new trigger, type in ``img``

4. In the 'output' column, type in ``<img src="%C">``


In the future, if you type in ``img`` and use Transforms->Perform Trigger, it
will expand itself to ``<img src="">`` with your cursor between the two double
quotes.

What other nifty things are possible?  How about automatic curly and square
brace matching with [, [%C] and {, {%C}?  Note that triggers with a single
character in the 'enter' column are automatically done as you type, but
triggers with multiple characters in the 'input' column require using
Transforms->Perform Trigger (or its equivalent hotkey if you have assigned
one via Options -> Change Menus and Hotkeys).

As described, there is a ``%C`` directive that defines where the cursor will
end up.  There is also a ``%L`` directive that inserts a line break with
autoindentation.  The semantics for string escapes are the same as in the
Find/Replace bar, and a non-indenting line break can be inserted with the
standard ``\n``.


Find/Replace bars
=================
If you have ' or " as the first character in a find or find/replace entry, and
what you entered is a proper string declaration in Python, PyPE will use the
compiler module to parse and discover the the string.  For example, to
discover LF characters, use ``"\n"``, including quotes.


What happens when "Smart Case" is enabled during a replace?
===========================================================
If the found string is all upper or lower case, it will be replaced by a
string that is also all upper or lower case.

Else if the length of the found string is the same length as the replacement
string, you can replace one string for another, preserving capitalization.

For example... ::

    def handleFoo(foo, arg2):
        tfOO = fcn(foo)
        tFOO2 = fcn2(tfOO)
        return fcn3(tfOO, tFOO2, foo)

...becomes... ::

    def handleGoo(goo, arg2):
        tgOO = fcn(goo)
        tGOO2 = fcn2(tgOO)
        return fcn3(tgOO, tGOO2, goo)

...by enabling "Smart Case", and putting 'foo' and 'goo' in the find/replace
boxes.

Otherwise if the first letter of the found string is upper or lowercase, then
its replacement will have the first letter be upper or lowercase respectively.


String escapes in regular expressions and multiline searches?
=============================================================
When using the 'Search' tab, you can use standard Python strings with escapes
and quote marks just like when you use the find/replace bars with one minor
difference; all searched data is normalized to have ``\n`` line endings
regardless of the input.  This means that if you want to find a colon followed
by a line ending followed by a space, you would use ``":\n "``, including
quotes.

If you include line endings in your search string, then multiline searching
will be automatically enabled during the search (but the box will remain
checked or unchecked).



How do I use the 'Todo' list?
=============================
On a line by itself (any amount of leading spaces), place something that
matches the following regular expression: ``([a-zA-Z0-9 ]+):(.*)`` and is
immediately proceeded with a language-specific single-line comment (``#``,
``//``, ``%``, or ``<!--``).

The first group (after a .strip().lower() translation) will become category in
the 'Category' column, the second group (after a .strip()) becomes the todo in
the 'Todo' column, and the number of exclamation points will become the number
in the '!' column.

PyPE should also toss all entries with a 'Category' that is also a keyword
(keyword.kwlist), or one of the following: http, ftp, mailto, news, gopher,
and telnet.

The following lines are all valid todos ::

    # todo: fix the code below
            #todo:fix the code below!
        #        TODo: fix the code below
    #bug:I am a big ugly bug...no, I really am, but I'm also a todo
    # this thing can even have spaces: but it cannot have punctuation!
    
    #I am not a valid todo...: because there is punctuation on the left

In PyPE 2.6.5 and later, for Python, C/C++, and TeX files, PyPE supports the
use of ``#>`` (or equivalents for non-XML/HTML languages) as a "strict" todo,
with the option to only recognize these "strict" todos.


Labels / Transforms -> Insert Comment
=====================================
When you use Transforms -> Insert Comment, you create a comment of the form
(for example in Python)::

    #--------------------- comment ---------------------

With your comment centered, and the comment filling up the number of columns
defined via Document -> Set Long Line Column.  Such comments will show up as
'labels' within the Name, Line, and Filter tools as::

    -- comment --

This works similarly to SPE's display of such labels, but PyPE trims
extraneous dashes and spaces from either end, inserting a single space and a
double dash around the comment (for consistency and readability).


What are the known issues within PyPE's parser?
===============================================

The C/C++ parser
----------------
PyPE 2.6.1 and later added a C/C++ parser that uses a combination of regular
expressions and some post-processing to extract function definition
information.  Note that it can handle things like the following and their
variations::

    int ** foo(char* arg1, int larg1) \{ ...
    
    str1 myClass :: operator[] (indices, count)
    int* indices;
    int count;
    \{ ...

Generally speaking, it searches for all matches of the following regular
expressions for function-like examples of ``#define`` and functions
respectively::

    (#ys+i\(i(?:,s*i)*\))
    (?:(cs*\([^\)]*\))[^{;\)]*[;{])

Where the following replacements are made to the regular expressions prior to
matching::
    
    c -> (?:i|operator[^\w]+)
    i -> (?:[a-zA-Z_]\w*)
    s -> [ \t]
    y -> (?:[dD][eE][fF][iI][nN][eE])

The function-like macros are returned unchanged, while the possible function
matches have various other tests performed on them and everything on the same
line as the potential function definition.

Note that the parser doesn't recognize struct definitions, data members of
classes, class hierarchies, functions with default values, etc., but it should
generally be sufficient for most navigation and/or file-specific autocomplete
and calltips.


The Python parser
-----------------
For Python source files, if given a syntactically correct Python source file,
the Python parser should work without issue (as long as --nothread is not
provided), though it may not be quite as fast as desired (where fast is < .1
seconds).  Recent versions of PyPE have a much faster "slow" parser than
previous versions, but it is still limited to syntactically correct source
files.

If not given a syntactically correct Python source file (or if --nothread was
provided as a command line option), the parser splits the file into lines,
performing a check to see if there is a function, class, or comment on that
line, then saves the hierarchy information based on the level of indentation
and what came before it.  This can be inaccurate, as it will mistakenly
believe that the below function 'enumerate' is a method of MyException. ::

    class MyException(Exception):
        pass
    try:
        enumerate
    except:
        def enumerate(inp):
            return zip(range(len(inp)), inp)

It also doesn't know anything about multi-line strings, so the definition nada
in the following lines would be seen as a function, and not part of a string. ::

    '''
    this used to be a function
    def nada(inp):
        return None
    '''

This parser will not pull out doc strings or handle multi-line function
definitions properly (which can be difficult if not impossible when provided
with a bad source file).


TeX/LaTeX
---------
In TeX/LaTeX, PyPE extracts \\(sub)*section and \\label headings, todo items,
and labels (defined below).


HTML/XML
--------
PyPE only extracts todo items and labels (defined below).


Label Parser
------------
Knowing where to insert a label (in the trees) is tricky work, and we can only
generally choose the right place to insert labels in one of the following two
cases::

    def foo():
        #-- label 1 --
        ...
    
    #--label 2--

Relying on indentation for these is not generally reliable, so we place it in
the context of the scope of the following function/class/whatever definition.
The following source::


    class foo:
        def bar(self):
            #-- label 1 --
            def goo():
                #-- label 2 --
                ...
        #-- label 3 --
        def baz(self):
            #-- label 4 --
            ...
        #-- label 5 --

Will have a general tree layout of::

    class foo:
        def bar():
            -- label 1 --
            def goo():
        -- label 2 --
        -- label 3 --
        def baz():
    -- label 4 --
    -- label 5 --

Using a 'previous definition' semantic, we get a layout of::

    class foo:
        def bar():
            -- label 1 --
            def goo():
                -- label 2 --
                -- label 3 --
        def baz():
            -- label 4 --
            -- label 5 --

Which is different, but not substantially better, and may hide labels. It is
better to show too many labels in a particular context than too few.


Name/Line Expanded State
------------------------
PyPE will only be able to remember those items that were expanded, selected or
first visible (to keep the scrollbar consistant) if the names hadn't been
changed.  Say that you had an item named ``class foo:`` that was expanded
prior to using Document -> Refresh.  If you renamed it to ``class foo_bar:``,
then PyPE wouldn't remember that it was expanded in the browsable source tree.

Also, if you have two classes with the same name like the following::

    if CONDITION:
        class foo:
            def bar(self):
                ...
    else:
        class foo:
            def bar(self):
                ...

And one was expanded in the Name (or Line) tool, then both will be expanded in
the Name (or Line) tool.


How do you get usable Calltips?
===============================
Hit F5.  This will also rebuild the browsable source tree, autocomplete
listing, filter, and todo list.


How do you get autocompletion?
==============================
Easy.  In the 'Document' menu, there is an entry for 'Show autocomplete'.
Make sure there is a check by it, and you are set.  If you want to get a new
or updated listing of functions, hit the F5 key on your keyboard.


CRLF/LF/CR line endings
=======================
PyPE will attempt to figure out what kind of file was opened, it does this by
counting the number of different kinds of line endings.  Which ever line
ending appears the most in an open file will set the line ending support for
viewing and editing in the window.  Also, any new lines will have that line
ending.  New files will have the same line endings as the host operating
system.

Additionally, copying from an open document will not change the line-endings.
Future versions of PyPE may support the automatic translation of text during
copying and pasting to/from the host operating system's native line endings.

Converting between line endings is a menu item that is available in the
'Document' menu.


STCStyleEditor.py
=================
As I didn't write this, I can offer basically no support for it.  It seems to
work to edit python colorings, and if you edit some of the last 30 or so lines
of it, you can actually use the editor to edit some of the other styles that
are included.

If it doesn't work for you, I suggest you revert to the copy of the editor and
stc-styles.rc.cfg that is included with the distribution of PyPE you received.
As it is a known-good version, use it.


Expandable/collapsable/foldable code
====================================
Since the beginning, there have been expandable and collapsable scopes thanks
to wxStyledTextCtrl.  How to use them...
Given the below... ::

    - class nada:
    -     def funct(self):
    -         if 1:
    |             #do something
    |             pass

Shift-clicking the '-' next to the class does this... ::

    - class nada:
    +     def funct(self):

Or really, it's like ctrl-clicking on each of the functions declared in the
scope of the definition.  Shift-clicking on the '-' a second time does
nothing. Shift-clicking on a '+' expands that item completely.

Control-clicking on a '+' or '-' collapses or expands the entirety of the
scopes contained within.

I don't know about you, but I'm a BIG fan of shift-clicking classes.  Yeah.
Play around with them, you may like it.


Converting between tabs and spaces
==================================
So, you got tabs and you want spaces, or you have spaces and want to make them
tabs.  As it is not a menu option, you're probably wondering "how in the hell
am I going to do this".  Well, if you read the above stuff about string
escapes in the find/replace bar, it would be trivial.
Both should INCLUDE the quotation marks.
To convert from tabs to 8 spaces per tab; replace ``"\t"`` with ``"        "``
To convert from 8 spaces to one tab; replace ``"        "`` with ``"\t"``

Note that you don't need to use the double quotes for the spaces, but it
allowed me to be explicit in this documentation.

Alternatively, this is available via the "Transforms" menu.


-------------------------------
How do I program my own macros?
-------------------------------

Users of PyPE 2.5.1 (a test release) and later will have the ability to
record, edit, playback, and delete macros.  Most keyboard related tasks are
recorded (typing, keyboard movement, selection, cut, copy, paste, etc.), as
are all items in the Transforms menu; including automatic and manual triggers.

Any macro without any action performed will not be recorded.  That is, if you
hit "Start Recording" and do nothing other than hit "Stop Recording", a macro
will not be created.  If you would like to create an initially empty macro,
you can use "Empty Macro" and it will get everything all set up for you.

Before you execute your macro, I encourage you to save all currently open
documents.  While I haven't experienced any recent crashes or segfaults while
using macros, I may not be able to replicate your particular crash condition
even if given the macro source, so may not be able to fix your problem.  Be
careful!


Let us assume that you have created an initially empty macro with the "Empty
Macro" button, whose contents are something like the following::
    
        creation_date = 'Wed Jul 12 21:35:34 2006'
        name = 'macro: Wed Jul 12 21:35:34 2006'
        hotkeydisplay = ""
        hotkeyaccept = ""
        
        def macro(self):
            pass
    

``creation_date``
    is merely for reference purposes

``name``
    is the name you will see in the macro list.  If this value is
    missing, you will see the file name instead.

``hotkeydisplay``
    if you have created a hotkey for this macro, this represents how the
    hotkey would be displayed to PyPE.  To get usable values for
    ``hotkeydisplay``, use the 'Create Hotkey' button.

``hotkeyaccept``
    if you have created a hotkey for this macro, this represents the
    actual underlying keyboard keypresses necessary to make the macro run.  To
    get usable values for ``hotkeyaccept``, use the 'Create Hotkey' button.

``def macro(self):``
    is the initial definition of the macro.  You can have any number of helper
    functions, extra data, etc., but the macro itself must be named ``macro``,
    and must take at least one argument, the first of which being the
    ``wxStyledTextCtrl`` instance that contains the current document.  You can
    also import any module that is available (which may be limited on systems
    using the Windows binary).

The ``self`` parameter will actually be my own custom subclass of the
``StyledTextCtrl``.  You will never receive a shell or interpreter, and you
will not be able to execute macros on shells or interpreters. 

Generally speaking, the ``wxStyledTextCtrl`` subclass has everything that the
normal control subclass has, with a few caveats.

1.  ``self.GetText()`` and ``self.SetText()`` will return and set the content
    of the document, paying attention to encodings as necessary.  That is, if
    you perform ``y = self.GetText()`` inside a macro on a document including
    unicode characters, or a document defining one of the standard Python
    document encoding methods, you will receive the encoded version of your
    document.  Strictly ASCII documents or those without any encodings will
    produce the document as-is.
    
    If you would like to acquire the contents of the file as-is, unicode on
    unicode platforms, etc.::
    
        import wx.stc
        
        def macro(self):
            content = wx.stc.StyledTextCtrl.GetText(self)

2.  ``self.lines`` is a special property that gives you a line-based view of
    the current document.::

        line = self.lines[i]        # will return line "i" including whitespace
        lines = self.lines[i:j]     # will return lines i...j-1, using standard Python slice semantics
        bad = self.lines[i:j:-1]    # will raise an exception (only steps == 1 are acceptable)
        
        self.lines[0] = 'hello world\n' # will set the first line to be "hello world"
        self.lines[0] = 'hello world '  # will set the first line to be "hello world ",
                                        # and the next line will become the tail end of the first line
        
        del self.lines[i] # same as self.lines[i] = ''
    
        #other special properties of self.lines:
        self.lines.curline          # manipulation of the line the cursor is on
        self.lines.curlinei         # manipulation of the index where the cursor is
        self.lines.curlinep         # manipulation of the column in the line where the cursor is
        self.lines.selectedlines    # manipulation of the lines where the selection exists
        self.lines.selectedlinesi   # manipulation of the indices where the selection exists
        self.lines.targetlines      # manipulation of the lines where the target exists
        self.lines.targetlinesi     # manipulation of the indices where the target exists
                                    # the target is like an invisible selection
        
        
        #to force the selection of all of all lines where a selection currently exists:
        self.lines.selectedlinesi = self.lines.selectedlinesi
        
        #to iterate over the indices of all selected lines:
        for i in xrange(*self.lines.selectedlinesi):
            ...
    
        #etcetera.

3.  ``self.InterpretTrigger(text)`` will interpret the text you provide as it
    would interpret a trigger, with a small change.  That is,::
   
        self.InterpretTrigger('def foo(%C):\npass')

    will produce the following, with the cursor where the ``@`` is, without
    the ``@`` sign.::
   
        def foo(@):
            pass

    If you want your ``'\n'`` line endings to not include auto-indenting (as
    is the default for normal triggers), use ``self.InterpretTrigger(text, 1)``.

4.  ``self._autoindent(0)`` will perform the equivalent of
    ``self.InterpretTrigger('\n')``.


An example nontrivial macro
===========================
When I was writing macro support, I would have found macros to be quite
convenient for developing macros.  What do I mean?  Let us say that I wanted
to turn a line that read (from main_window_callback.c in the gPHPedit sources)::

        case (2316) : gtk_scintilla_document_start(GTK_SCINTILLA(main_window.current_editor->scintilla)); break;

Into a line that read::

        2316: 'DocumentStart',

As I ended up doing by hand.  Well, I could write the following macro, select
those lines I wanted to update, and execute the macro.::

        def macro(self):
            lines = self.lines
            newlines = []
            for i in xrange(*lines.selectedlinesi):
                line = lines[i]
                pieces = line.split()
                num = pieces[1].strip('()')
                name = pieces[3]
                name = name.split('(', 1)[0].title()
                name = ''.join(name.split('_')[2:])
                newlines.append("    %s: '%s',"%(num, name))
            lines.selectedlines = newlines
    
Presumably one would want to include error handling in your nontrivial macros,
but that shouldn't be terribly difficult.


Using macros as code snippets
=============================
1. Create a macro.

2. Paste the content of your snippet into a global variable in the macro and
   call it something like ``snippet``.

3. Use ``self.InterpretTrigger(snippet)``.

That is, let us say that you wanted a snippet that inserted the following
content::

    def foo(bar):
        pass

You would create the following macro::

    name = 'Code Snippet foo()'
    
    snippet = '''
    def foo(bar):
        pass
    '''
    
    def macro(self):
        self.InterpretTrigger(snippet, 1)


Sample Macros included with PyPE
================================

PyPE includes a handful of sample macros to give you some idea of what works
and what doesn't.  The most important ones you should look at are the various
Timeout macros.  They will show you what things will and won't stop after the
5 second timeout.  The timeout conditions are there to try to prevent you from
trying to kill PyPE because it stopped responding.  The general rule of thumb:
don't perform any system calls that could take a long time to finish.


Non-white background colors
===========================

In PyPE 2.8.6, the stylesetter now has support for non-white background
colors.  To set a non-white background color, change the 'backcol' value in
the proper common.defs.* in your 'stc-styles.rc.cfg'.


---
FAQ
---

How do you come up with new feature ideas?
==========================================
Every once and a while, I'll be editing with PyPE, and I'll say, "hey, it
would be neat if I could do X with PyPE".  This is rare, though it has
produced things like the dragable document list, spell check, customizable
menu hotkey bindings, open module, "One PyPE", etc.

More often than not, I will be surfing the net, and someone will rant and rave
about their super ultra mega favorite editor X, and how it has so many
features that are so great that no other editor has.  Out of curiosity, I'll
usually go to the specific site, look at the editor, the features it offers,
and consider if I would want PyPE to have such features, what changes would be
necessary, and what it would take to make them happen.  This has produced
things like workspaces, shells, find/replace bars (idea from Firefox),
triggers (and most everything else in the Transforms menu), the name and line
oriented browsable source trees, etc.

Occasionally, some user of PyPE will contact me, perhaps report a bug, or
somesuch, and eventually either suggest features or offer up patches.  While
I had written the original Search tab, the current Search tab and the table
display of results were submitted almost complete.  Suggestions have resulted
in the addition of Start/End selection, bookmarks, the line-based abstraction
for macros, macros themselves, tools whose positions can be switched, title
options, the optional toolbar, caret tracking and width options, find/replace
bar history, the actual find/replace bar keybindings and what they do based on
context, the embedded HTML help, the Find Definition/filter tool, etc.

Astute observers will note that I have not really come up with anything
terribly original myself.  However, through observing other editors and IDEs,
and receiving great suggestions from users, I think that PyPE has managed to
acquire some very useful features.  Generally, I have written PyPE primarily
for myself, so if tools have a particular aesthetic or design, it's so that
look and work according to how I think they should (the exception being how
document preferences are handled, I really need to change that design).  I
hope that others find PyPE as natural to use as I do, but if not, then I
welcome your feedback.


What's the deal with the version numbering scheme?
==================================================
Early in development, PyPE raised version numbers very quickly.  From 1.0 to
1.5, not much more than 2 months passed.  In that time, most of the major
initial architectural changes that were to happen, happened.  This is not the
reason for the version number change.  Really it was so that the MAJOR
versions could have their own point release (1.0 being the first), and minor
bugfixes on the point releases would get a minor release number (like 1.0.1).

Then, at around PyPE 1.4.2, I had this spiffy idea.  What if I were to release
a series of PyPE versions with the same version numbers as classic Doom?  I
remembered updating to 1.1, then to 1.2a, etc.  My favorite was 1.666.  Ah
hah! PyPE 1.6.6.6, the best version of PyPE ever.

I decided that I would slow version number advancement, if only so that people
didn't get sick of new releases of PyPE being numbered so much higher when
there were minimal actual changes.  Then the more I thought about it, the more
I realized that it doesn't matter at all, I mean, Emacs is on version 20+.
\*shrug\*

When PyPE 1.9.3 came out, I had a few other ideas for what I wanted to happen,
but since major changes to the underlying architecture were required, it
really should get a major number bump to 2.0.  After spending 3 months not
working on PyPE May-July 2004, I got some time to muck around with it here and
there.  After another few months of trying to rebuild it to only require a
single STC (with multiple document pointers, etc.) I realized that I'd have to
rebuild too much of PyPE to be able to get 2.0 out the door by 2010.  So I
started modifying 1.9.3.  All in all, around 85% of what I wanted made it into
PyPE 2.0, the rest was either architectural (ick), or questionable as to
whether or not anyone would even want to use the feature (even me).


How did PyPE come about?
========================
The beginnings of PyPE were written from 10:30PM on the 2nd of July through
10:30PM on the 3rd of July, 2003.  Additional features were put together on
the 4th of July along with some bug fixing and more testing for version 1.0.
Truthfully, I've been using it to edit itself since the morning of the 3rd of
July, and believe it is pretty much feature-complete (in terms of standard
Python source editing).  There are a few more things I think it would be nice
to have, and they will be added in good time (if I have it).

One thing you should never expect is for PyPE to become an IDE.  Don't expect
a UML diagram.  Don't expect a debugger.  Don't expect debugging support
(what, print statements not good enough for you?)

On the most part, this piece of software should work exactly the way you
expect it to...or at least the way I expect it to.  That is the way I wrote
it.  As a result, you don't get much help in using it (mostly because I am
lazy).  There was a discussion of a PyPE wiki a long time ago, but that will
likely never happen (I've lost contact with the people who initially put
forward the wiki idea, and I have no interest in starting or maintaining one).

The majority of the things that this editor can do are in the menus.  Hotkeys
for things that have them are listed next to their menu items, and you can
both rename menu items and change their hotkeys via Options->Change Menus and
Hotkeys.


----------
Thank Yous
----------
Certainly there are some people I should thank, because without them, the
piece of software you are using right now, just wouldn't be possible.

Guido van Rossum - without Guido, not only would I not have Python, I also
wouldn't have had some of the great inspiration that IDLE has offered.  IDLE
is a wonderful editor, has some excellent ideas in terms of functionality, but
unfortunately does not offer the extended functionality I want, and it hurts
my brain to use tk, so I cannot add it myself.

The people writing wxWidgets (previously named wxWindows) and wxPython -
without you, this also would not have been possible.  You have made the most
self-consistent GUI libraries that I have ever used, made them easy to use,
and offer them on every platform that I would ever want or need.  You rock.

Neil Hodgson and others who work on Scintilla.  As wx.StyledTextCtrl is a
binding for scintilla in wxWidgets, which then has bindings for wxPython,
basically ALL the REAL functionality of the editor you are now using is the
result of Scintilla.  The additional things like tabbed editing, hotkeys,
etc., they are mere surface decorations in comparison to what it would take to
write everything required for a text editor from scratch.  Gah, an editor
widget that just works?  Who would have figured?

To everyone who I have already thanked: thank you for making PyPE an almost
trivial task.  It would have been impossible to go so far so fast by hand in
any other language using any other GUI toolkit or bindings.
