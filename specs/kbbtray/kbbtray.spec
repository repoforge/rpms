# $Id$
# Authority: dries

Summary: Display the status of a Big Brother page in the system tray
Name: kbbtray
Version: 0.03
Release: 2
License: GPL
Group: Applications/System
URL: http://coldstonelabs.org/index.jsp?projectIndex=4

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://coldstonelabs.org/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: PyKDE, python

# Screenshot: http://coldstonelabs.org/images/kbbtray/kbbtray-sh.png

%description
Kbbtray displays the status of a Big Brother page in the system tray. It's
written in Python and uses PyKDE.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
sed -i "s|/usr/local/|%{buildroot}%{_prefix}|g" install.sh
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
* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 0.03-2
- cleanup of spec file

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 0.03-1
- first packaging for Fedora Core 1

