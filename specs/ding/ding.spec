# $Id$
# Authority: dries
# Upstream: Frank Richter <fri$hrz,tu,chemnitz,de>

Summary: Dictionary lookup program
Name: ding
Version: 1.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www-user.tu-chemnitz.de/~fri/ding/

Source: http://wftp.tu-chemnitz.de/pub/Local/urz/ding/ding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: tk

%description
Ding is a dictionary lookup program for the X Window system on Linux/Unix. It
comes with a German-English Dictionary with about 180,000 entries. It is
based on Tk version >= 8.3 and uses the agrep or egrep tools for searching.
In addition ding can also search in English dictionaries using dict(1) and
check spelling using ispell(1). It has many configuration options, such as
search preferences, interface language (English or German), and colors. It
has history and help functions and comes with useful key and mouse bindings
for quick and easy lookups.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 ding %{buildroot}%{_bindir}/ding
%{__install} -d %{buildroot}%{_datadir}/dict \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/pixmaps \
	%{buildroot}%{_mandir}/man1
%{__install} -m0644 *-*.txt %{buildroot}%{_datadir}/dict/
%{__install} -m0644 ding.desktop %{buildroot}%{_datadir}/applications/
%{__install} -m0644 ding.png %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 ding.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/ding
%{_datadir}/dict/de-en.txt
%{_datadir}/pixmaps/ding.png
%{_datadir}/applications/ding.desktop
%doc %{_mandir}/man1/ding.1*

%changelog
* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
