# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_gamin 1}
%{?fc4:%define _with_gamin 1}
%{?el4:%define _with_gamin 1}
%{?fc3:%define _with_gamin 1}
%{?fc2:%define _with_fam 1}
%{?el3:%define _with_fam 1}

%define desktop_vendor rpmforge

Summary: Graphical file management program in GTK+ for Linux
Name: gentoo
Version: 0.11.55
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.obsession.se/gentoo/
Source: http://dl.sf.net/gentoo/gentoo-%{version}.tar.gz
Patch: gentoo-0.11.52-pomkinstalldirs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, desktop-file-utils
%{?_with_gamin:BuildRequires: gamin-devel}
%{?_with_fam:BuildRequires: fam-devel}


%description
gentoo is a file manager for Linux written from scratch in pure C. It
uses the GTK+ toolkit for all of its interface needs. gentoo provides
100%% GUI configurability; no need to edit config files by hand and re-
start the program. gentoo supports identifying the type of various
files (using extension, regular expressions, and/or the 'file' command),
and can display files of different types with different colors and icons.
gentoo borrows some of its look and feel from the classic Amiga
file manager "Directory OPUS"(TM) (written by Jonathan Potter).


%prep
%setup
%patch -p1 -b .pomkinstalldirs


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__install} -D docs/gentoo.1x %{buildroot}%{_mandir}/man1/gentoo.1
%{__install} -D -m 644 icons/gentoo.png \
    %{buildroot}%{_datadir}/pixmaps/gentoo.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Gentoo File Manager
Comment=Graphical file managment program in GTK+ for Linux
Icon=gentoo.png
Exec=gentoo
Terminal=false
Type=Application
Categories=Application;Utility;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog CONFIG-CHANGES COPYING CREDITS docs/
%doc NEWS ONEWS README README.gtkrc TODO
%config %{_sysconfdir}/gentoo*
%{_bindir}/gentoo
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/gentoo/
%{_datadir}/pixmaps/gentoo.png
%{_mandir}/man1/gentoo.1*


%changelog
* Mon Jun 27 2005 Matthias Saou <http://freshrpms.net/> 0.11.55-1
- Update to 0.11.55.
- Replace gnome-db-icon.png used until now with included gentoo.png.
- Fix wrong gamin/fam build requirement.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 0.11.54-1
- Update to 0.11.54.

* Mon Nov  8 2004 Matthias Saou <http://freshrpms.net/> 0.11.53-1
- Update to 0.11.53.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.11.52-1
- Update to 0.11.52.
- Add gentoo-0.11.52-pomkinstalldirs.patch to fix building.

* Mon May 10 2004 Matthias Saou <http://freshrpms.net/> 0.11.51-1
- Update to 0.11.51.

* Tue May  4 2004 Matthias Saou <http://freshrpms.net/> 0.11.50-1
- Update to 0.11.50.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 0.11.49-1
- Update to 0.11.49.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 0.11.48-1
- Update to 0.11.48.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 0.11.47-1
- Update to 0.11.47.

* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net/> 0.11.46-1
- Update to 0.11.46.

* Wed Dec  3 2003 Matthias Saou <http://freshrpms.net/> 0.11.45-1
- Update to 0.11.45.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.11.44-1
- Update to 0.11.44.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.11.43-1
- Update to 0.11.43.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.11.42-1
- Update to 0.11.42.
- Added icon suggested by Matthias Haase.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 0.11.41-1
- Update to 0.11.41.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.11.40-1
- Update to 0.11.40.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.11.39-2
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 0.11.39-1
- Update to 0.11.39.

* Mon Oct 27 2003 Matthias Saou <http://freshrpms.net/> 0.11.38-1
- Update to 0.11.38.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.37.

* Fri Oct  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.35.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Mon Sep  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.34.

* Mon Aug 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.32.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.31.

* Mon Jul 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.30.

* Fri Jul 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.29.

* Thu Jul 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.28.
- Added the lang stuff.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.27.

* Mon Jun 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.26.

* Wed Jun  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.25.

* Tue Apr  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.23.

* Thu Mar 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.22.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.21.

* Fri Feb 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.20.

* Mon Feb 11 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.19.

* Mon Oct 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.18.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.17.
- The sources are now much cleaner, so hacks were removed from the spec.

* Thu Jul  5 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.16.
- Spec file cleanup for Red Hat 7.1.

* Fri Sep 15 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.15-1]
- Definition of demonstration SelectRE-work-a-like button command
  changed, since it was broken. Also added glob check button.
- Lack of internal quoting caused Dir{To,From}Other to fail on
  paths containing spaces, as did the shortcuts. Fixed.
- Changed appearance of check buttons {Ix} input dialog codes.
- Having lurked among the giants of comp.lang.c for at least five
  years, I finally realized that identifiers whose names begin
  with an underscore immediately followed by an upper case letter
  are reserved for the implementation. Since I, for some historical
  reason, tend to use structure tags formed like that, gentoo was
  very much in violation of the holy scripture of ISO C. This has
  now been fixed, of course (except in widgets/). Feels good. :)
- Being urged on by a Brazilian gentoo user, Alceu Rodrigues de
  Freitas Junior, I caved in and went through the code, marking
  all strings suitable for translation using gettext. A translation
  to my own mother tongue, Swedish, is included in the locale/sv/
  directory. gentoo's I18N support is very early, and by default
  it will not build with it included. I need help with autoconfig
  before doing that.
- Capped the percentage number in the textviewer at 100%. :)
- Left-adjusted the filename in the progress window. :)
- Improved behavior when an operation (such as Copy or Move) is
  cancelled. Previously, it was not possible to correctly cancel
  if the files being copied were smaller than the copy buffer
  size, and the 'keep full-sized copy on error?' flag was on.
- A long operation can now be cancelled by simply closing the
  progress-reporting window.
- Made parsing of {Fup} (among other things, hopefully) work
  better when 'treat focus as selection?' flag is on. Sneaky.
- Test-compiled against glib and GTK+ version 1.2.8. Went fine.
- Fixed buglet that prevented modes (aka permissions) from being
  formatted correctly. Reported by Erik Johansson.
- Banged a bit on the page up/down response for the focus bar.
  Way less ugly implementation, and (I think) better behavior
  now. Still wish GTK+ permitted use of it's built-in focusing
  bar, though. :(
- Updated to the latest version (0.5) of Johan Hanson's
  odemilbutton widget.

* Wed Apr 19 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.14-3]
- Doh!. Was not setting default icon path in default gentoorc. Fixed.
  Thanks Udo K. Schuermann <walrus@ringlord.com>.

* Mon Apr 17 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.14-1]
- Added support for extracting tar.gz, tar.bz2, and zip files to
  the example config. Select archive, right click, then choose
  the "extract" item in the "File Action" submenu.
- Due to an internal quoting problem, MkDir would fail to enter
  the created directory if the name contained spaces. Fixed.
- The Makefile no longer attempts to create a backup of the config,
  and only installs the supplied example if no old config exists.
- The ChOwn command now uses combo boxes rather than menus to
  display the system data, and also allows you to type in a
  user and/or group number or name directly. Way nicer.
- Brought back the 'grab' button in the window pos/size config,
  but only for the main window. Should make a few users happy. :)
- Altered the huge parent buttons' relief style; they now look
  more like wide borders, which JH and I find less distracting.
- Added an option (hidden away in the Command Options page,
  DpFocus tab) that makes gentoo move the focus row to the last
  row selected using the mouse. Only works if focusing is on.
- The MenuPopup command can now be bound to a keyboard key, just
  like any other command. Previously, it could only be bound to
  a mouse button. Bound to Ctrl+Space in example config.
- Added Ctrl+A and Shift+Ctrl+A as keyboard shortcuts for the
  [Select] All and None commands, respectively. :)
- Improved ANSI compliance by removing use of "str" as a prefix
  in function names. :)
- A pane's contents can now be sorted on any content type, not
  just those that are displayed. There is currently no way of
  changing to a non-displayed type without opening the config
  window, though.
- Touched up the sorting code somewhat, and while doing that
  noted that user and group names could not actually be sorted
  on as text. They sure can now.
- Fixed horrible bug in the {}-code parsing and handling, that
  made gentoo segfault when certain sequences of commands were
  run. Reported by T. Tilton.

* Mon Mar 20 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.13-1]
- Fixed incredibly stupid bug (reported by plenty of people, it's
  nice to know people care :) which prevented the text viewer
  window from closing when it should. It's a two-line fix.
- If you enable the "System Default" Control key mode in the
  dirpane config, it will now work.
- There was some broken logic related to quitting and the dialog
  that asks about saving changed configs. Fixed that, and also
  cleaned up the code significantly, removing duplicate stuff.

* Mon Mar  6 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.12-1]
- I'm reasonably sure I fixed a bug which caused a crash if you
  hit enter after entering an *empty* directory using the key-
  board-controlled focusing mechanism.
- Added support for tall, thin, parent buttons along the outer
  edges in the panes. Enable through the "Huge Parent Button?"
  checkbox in the config. The position and action of these is
  currently not configurable; it's always outer edge & DirParent.
- Incorporated alternative implementation of the GtkLabel widget
  provided by Johan Hanson. This label implementation is only used
  for the status line in the top of the window, which reportedly
  had refresh-problems with some pixmap-based GTK+ themes.
- Redid the code for the textviewer, which was very old and some-
  what confused. This might make it support mouse wheel scrolling
  better. Since I don't have a wheelie mouse, I can't test it...
- Fixed tiny bug which caused GTK+ warnings if you hit TAB in the
  command selection dialog without having typed anything first.
- Implemented a Join command, to counter the (still incomplete)
  Split command. Pretty neat, with DnD reordering.
- gentoo can now optionally ignore the state of the NumLock key
  when parsing keyboard and mouse input. Enable the check button
  in the bottom of the Controls config page. Note that only the
  input event is filtered, not the definition (do not use NumLock
  in actual mappings with this flag on).
- New version of the odscrolledbox widget, provided by Johan
  Hanson as always. Should fix some smudgy redrawing problems.
- Brought the (c) in the About box into the 21th century, added
  acknowledgement (and mail address) of Johan Hanson's work.
- Added recognition and viewing of LHa compressed files to the
  example config. Requires the 'lha' external command.
- gentoo can now remember the position and size of the config and
  textviewer windows, in addition to the main window. See config
  page labeled "Windows" (was "Pos & Size" previously). Eh, also
  see the BUGS file, since this feature has a few problems still. :(
- Tweaked code that dealt with 64-bit stuff; gentoo should now
  compile better on Linux/Alpha platforms.
- Selected content in the right-hand list in the Dirpane config
  page can now be reordered directly, by dragging. You can still
  use the up/down buttons below the list, like always.
- Er, not a fix per se, but this version of gentoo has been
  compiled and executed using GTK+ 1.2.7. No extensive tests,
  though.

* Mon Nov 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.11-1]
- Tweaked the FileAction command slightly: now it will stop running
  the action if the selection is empty. This helps when you run a
  command containing e.g. a {Fu} code on more than one file, since
  it will then just run the command once, then stop since the {Fu}
  "consumed" the entire selection. Hopefully this is not a bad thing.
- The GetSize command no longer loses track of the pane's vertical
  position.
- The pane centering on startup was changed back to the pre-0.11.10
  behavior, since the "fix" didn't help the user who reported the
  problem. Weird.
- Rewrote core file copying routine, used by Copy, CopyAs, Move,
  and other commands. It now handles "magic" files whose length
  looks like zero (like most files in the /proc filesystem). It's
  also shorter, simpler, and possibly a tiny bit faster.
- Fixed semi-obscure bug in the Split command; it wouldn't close
  output files on failed writes. Oops.
- In an attack of POSIX panic, I removed all my symbols whose names
  ended in _MAX, leaving only standard ones. Touched ~130 places.
- The SelectRE command now lets you chose what column content you
  wish to match against. This is sometimes useful, for example you
  could use the following command to select all rows whose files
  have an odd size: 'SelectRE glob=0 full=0 content=size [13579]$'.
     See "docs/scratch/command_args.txt" for a brief table of
  content names.
- Removed all uses of stdlib's malloc() & free(), replacing them
  with glib's g_XXX work-alikes, making the code more consistent.
- Added tooltips to the pane control widgets (the parent button,
  the path entry field, and the cryptic 'H' hide button).
- RTFM:ed a bit, and fixed example config's "view_man" command to
  stop emitting control codes for bold and underline. This makes
  it work better with gentoo's viewer. Unsure about portability.
- Added type, style, and view support for AVI and MPEG video clips
  to the example config. Both use 'xanim' for view. Untested. Also
  added support for IFF-ILBM bitmap images, through 'xv' as always.
- Added a new command, DpFocusPath, which moves GTK+'s input focus
  to the current pane's path entry box. Bound to shift+Return in
  the example config. Call with select=1 to select contents, too.
- Fixed buglet which made it annoying to bind commands to Return,
  since the config window's default button ("OK") would trigger.

* Tue Nov  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.10-1]
- Got mail from Jesse Perry <jap@unx.dec.com>, reporting problems
  building gentoo on an Alpha, running Tru64. Luckily, the report
  (and followups) included lots of detail and helpful hints, so I
  went over the offending code. Hopefully it works now.
- I still got the expand/collapse tracking in the Styles config
  page wrong. <HOMER>Duh!</HOMER> Fixed again. This time, for sure!
- Wrote a new command, RenameRE. It provides two ways of doing search
  and replace over selected file names, and then renaming the files.
  Learn about in "docs/scratch/renamere.txt". Recommended reading!
- Fixed bug which prevented an error from the Rename command (and
  others, no doubt) from showing up.
- Did a long-overdue, minimal, change in the way the active pane gets
  hilighted, now uses Johan Hanson's code in "colorutil.c". Should
  work better if you're running a themed GTK+.
- Pressing return after entering a path name now causes that path
  to be entered, instead of (uselessly) popping up the combo menu
  showing directory history. Oops.
- When running a command bound to a key, the key press signal is
  no longer propagated to GTK+; gentoo consumes it. This makes things
  work better when you bind stuff to e.g. cursor keys, which are
  used by GTK+ to control focus. A neat one-line fix.
- The 'view_tar_bzip2' command in the example config has been made
  more portable (uses --use-compress-prog=bzip2 rather than -y).
- If you attempt to DirRescan a directory which no longer exists,
  you will get an informative message. Better than silence.
- Included a new icons package from Johan Hanson (<johan@tiq.com>).
  There are around 20 new icons, including a very cute Commodore
  logo for SID music files! Check them out in the icons/ subdir!
- Fixed a portability problem in dirpane.c; a reference to strncmp().
- Upgraded my home development machine to GTK+/glib 1.2.6, which
  went fairly smooth. It exposed a bug in the config GUI, though.
- The centering of the panes is now done later during startup,
  since one user reported problems with it. This is too bad, since
  it now looks kind of worse during startup. :(

