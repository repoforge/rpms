# $Id: $

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: PyKDE, python

# Screenshot: http://coldstonelabs.org/images/kbbtray/kbbtray-sh.png

%description
Kbbtray displays the status of a Big Brother page in the system tray. It's
written in Python and uses PyKDE.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
# nothing to do

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
sed -i "s/\/usr\/local\//${RPM_BUILD_ROOT//\//\\/}\/usr\//" install.sh
sed -i "s/\/bin\/install/install/" install.sh
sed -i "s/\/usr\/local\//\/usr\//" kbbtray.py
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
./install.sh

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING INSTALL README REAL-BB-ICONS TODO
%{_bindir}/kbbtray.py
%{_datadir}/kbbtray/blue.png
%{_datadir}/kbbtray/clear.png
%{_datadir}/kbbtray/green.png
%{_datadir}/kbbtray/purple.mng
%{_datadir}/kbbtray/red.mng
%{_datadir}/kbbtray/yellow.mng


%changelog
* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 0.03-2
- cleanup of spec file

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 0.03-1
- first packaging for Fedora Core 1
