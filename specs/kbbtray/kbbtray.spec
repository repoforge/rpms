# $Id$
# Authority: dries
# Screenshot: http://coldstonelabs.org/images/kbbtray/kbbtray-sh.png

Summary: Display the status of a Big Brother page in the system tray
Name: kbbtray
Version: 0.07
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://coldstonelabs.org/index.jsp?projectIndex=4

Source: http://coldstonelabs.org/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: PyKDE, python

%description
Kbbtray displays the status of a Big Brother page in the system tray. It's
written in Python and uses PyKDE.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
sed -i "s|/usr/local|%{buildroot}%{_prefix}|g" install.sh
sed -i "s|/bin/install|%{__install}|g" install.sh
sed -i "s|/usr/local|%{_prefix}|g" kbbtray.py
%{__mkdir_p} %{buildroot}%{_bindir}
./install.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README REAL-BB-ICONS TODO
%{_bindir}/kbbtray.py
%{_datadir}/kbbtray/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> 0.07-1
- Update to version 0.07.

* Wed Dec 22 2004 Dries Verachtert <dries@ulyssis.org> 0.06-1
- Update to version 0.06.

* Mon Sep 13 2004 Dries Verachtert <dries@ulyssis.org> 0.05-1
- Update to version 0.05.

* Mon Sep 13 2004 Dries Verachtert <dries@ulyssis.org> 0.04-1
- Update to version 0.04.

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 0.03-1
- first packaging for Fedora Core 1
