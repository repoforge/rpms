# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Media Center
Name: elisa
Version: 0.5.22
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/

Source: http://elisa.fluendo.com/static/download/elisa/elisa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-twisted-core
#Requires: avahi-tools
Requires: elisa-plugins-good = %{version}
Requires: elisa-plugins-bad = %{version}
Requires: gnome-python2-extras
Requires: mgopen-fonts
#Requires: pycairo
Requires: python-ctypes
#Requires: python-daap
Requires: python-imaging
#Requires: python-lirc
#Requires: python-metar
Requires: python-setuptools
#Requires: python-sqlite2
#Requires: python-tag
Requires: python-twisted-core
Requires: python-twisted-web
Requires: python-twisted-web2

Obsoletes: elisa-core <= %{version}-%{release}
Provides: elisa-core = %{version}-%{release}

%description
Media center solution using the GStreamer multimedia framework.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed

### Create empty plugins directory
%{__install} -d -m0755 %{buildroot}%{python_sitelib}/elisa/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ FIRST_RUN LICENSE* NEWS README TRANSLATORS docs/*.txt
%doc %{_mandir}/man1/elisa.1*
%{_bindir}/elisa
%{_datadir}/applications/elisa.desktop
%{_datadir}/pixmaps/elisa.png
%{_datadir}/dbus-1/services/com.fluendo.elisa.service
%{python_sitelib}/elisa/
%{python_sitelib}/elisa-*.egg-info/
%{python_sitelib}/elisa-*-nspkg.pth
%exclude %{_datadir}/applications/elisa-mobile.desktop
%exclude %{_datadir}/icons/elisa.png

%changelog
* Mon Dec 15 2008 Dag Wieers <dag@wieers.com> - 0.5.22-1
- Updated to release 0.5.22.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.5.21-2
- Added python-ctypes as a requirement.

* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.5.21-1
- Updated to release 0.5.21.

* Wed May 16 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-4
- Patch desktop file to remove useless bits (Version and extra Categories).

* Tue May  8 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-3
- Change Coherence requirement to python-Coherence to match package name change.

* Mon May  7 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-2
- Change coherence requirement to Coherence to match package name change.

* Fri May  4 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-1
- Update to 0.1.6.

* Mon Apr 16 2007 Matthias Saou <http://freshrpms.net/> 0.1.5-1
- Update to 0.1.5.
- Disable gst requirements which aren't part of Fedora (oops!).
- Patch out the hash-bang python from scripts not meant to be executed.
- Rip out the root user test condition to installing the desktop entry.

* Fri Mar 23 2007 Matthias Saou <http://freshrpms.net/> 0.1.4.2-1
- Update to 0.1.4.2.

* Wed Feb 21 2007 Matthias Saou <http://freshrpms.net/> 0.1.4.1-1
- Update to 0.1.4.1.

* Thu Feb  8 2007 Matthias Saou <http://freshrpms.net/> 0.1.3-1
- Initial RPM release.

