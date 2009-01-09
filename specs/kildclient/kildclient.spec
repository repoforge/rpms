# $Id$
# Authority: dries
# Upstream:  Eduardo M Kalinowski <ekalin$bol,com,br>

Summary: MUD client
Name: kildclient
Version: 2.8.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kildclient.sourceforge.net/

Source: http://dl.sf.net/kildclient/kildclient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(XML::Parser), intltool, pkgconfig, gettext
BuildRequires: libglade2-devel, glib2-devel >= 2.6.0, gtk2-devel >= 2.10.0
BuildRequires: desktop-file-utils

%description
KildClient is a MUD client written with the GTK+ windowing toolkit. It
supports many common features of other clients, such as triggers, gags,
aliases, macros, timers, and much more. But its main feature is the
built-in Perl interpreter. At any moment, the user can execute Perl
statements and functions to do things much more powerful than simply
sending text the the MUD. Perl statements can also be run, for example,
as the action of a trigger, allowing you to do complex things. Some
built-in functions of KildClient allow interaction with the world,
such as sending commands to it. KildClient has extensive ANSI support,
it can display text in the standard 16 colors, and also text underlined,
in italics, strike-through, and in reverse video. It supports vt100's
line drawing characters for nice tables and xterm's sequences for a
256-color mode. KildClient supports MCCP (Mud Client Compression Protocol)
versions 1 and 2, and a direct chat system to other users of KildClient or
other clients compatible with the MudMaster or zChat protocols.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
%{__mv} %{buildroot}%{_datadir}/doc/kildclient rpmdocs

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL rpmdocs/*
%doc %{_mandir}/man1/kildclient.1*
%{_bindir}/kildclient
%{_datadir}/kildclient/
%{_datadir}/applications/*kildclient.desktop
%{_datadir}/pixmaps/kildclient.*

%changelog
* Fri Jan  9 2009 Dries Verachtert <dries@ulyssis.org> - 2.8.0-1
- Updated to release 2.8.0.

* Sun May  4 2008 Dries Verachtert <dries@ulyssis.org> - 2.7.0-1
- Updated to release 2.7.0.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.1-1
- Updated to release 2.5.1.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1
- Updated to release 2.5.0.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.1-1
- Updated to release 2.4.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1
- Updated to release 2.4.0.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 2.3.0-1
- Updated to release 2.3.0.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.2-1
- Updated to release 2.2.2.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.1-1
- Updated to release 2.2.1.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Initial package.
