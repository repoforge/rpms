# $Id$
# Authority: dag
# Upstream: Thierry Godefroy <xdialog$free,fr>

%define real_name Xdialog

Name: xdialog
Summary: X11 drop in replacement for cdialog
Version: 2.1.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://xdialog.dyns.net/

Source: http://thgodef.nerim.net/xdialog/Xdialog-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0
BuildRequires: autoconf, automake, gettext

Provides: Xdialog
Obsoletes: Xdialog < %{version}

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even
more functionalities (help button+box, treeview, editbox, file selector,
range box, and much more).

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__perl} -pi.orig -e '
		s|\@AR\@|%{_bindir}/ar|g;
		s|\@RANLIB\@|%{_bindir}/ranlib|g;
	' lib/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README
%doc doc/*.html doc/*.png samples/
%doc %{_mandir}/man1/Xdialog.1*
%{_bindir}/Xdialog
%exclude %{_docdir}/%{real_name}-%{version}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.2-1.2
- Rebuild for Fedora Core 5.

* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Initial package. (using DAR)
