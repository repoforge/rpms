# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Good Plugins for the Elisa Media Center
Name: elisa-plugins-good
Version: 0.5.22
Release: 1%{?dist}
License: GPL and MIT
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/

Source: http://elisa.fluendo.com/static/download/elisa/elisa-plugins-good-%{version}.tar.gz
Patch0: elisa-plugins-good-0.5.2-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: elisa
BuildRequires: python-devel
Requires: elisa = %{version}

%description
This package contains the good set of plugins for the Elisa Media Center,
plugins which are considered stable and do not present any licensing issues.

%prep
%setup
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{python_sitelib}/elisa/plugins/base/
%{python_sitelib}/elisa/plugins/gnome/
%{python_sitelib}/elisa/plugins/hal/
%{python_sitelib}/elisa_plugin_*
### This plugin is not useful on non Windows platforms
%exclude %{python_sitelib}/elisa/plugins/winscreensaver/
%exclude %{python_sitelib}/elisa_plugin_winscreensaver-*

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 0.5.22-1
- Updated to release 0.5.22.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.5.21-1
- Updated to release 0.5.21.

* Mon Dec  1 2008 Matthias Saou <http://freshrpms.net/> 0.5.20-1
- Update to 0.5.20.

* Mon Nov 24 2008 Matthias Saou <http://freshrpms.net/> 0.5.19-1
- Update to 0.5.19.

* Mon Nov 17 2008 Matthias Saou <http://freshrpms.net/> 0.5.18-1
- Update to 0.5.18.
- Now list plugins individually in %%files to easily keep track of them.

* Tue Nov  4 2008 Matthias Saou <http://freshrpms.net/> 0.5.17-1
- Update to 0.5.17.

* Mon Oct 27 2008 Matthias Saou <http://freshrpms.net/> 0.5.16-1
- Update to 0.5.16.

* Tue Oct 21 2008 Matthias Saou <http://freshrpms.net/> 0.5.15-1
- Update to 0.5.15.
- Exclude new winscreensaver plugin, only useful on Windows.

* Mon Oct 13 2008 Matthias Saou <http://freshrpms.net/> 0.5.14-1
- Update to 0.5.14.

* Fri Oct 10 2008 Matthias Saou <http://freshrpms.net/> 0.5.13-2
- Build require elisa-base from now on.
- Update description to explain what "good" plugins are.

* Tue Oct  7 2008 Matthias Saou <http://freshrpms.net/> 0.5.13-1
- Update to 0.5.13.

* Tue Sep 30 2008 Matthias Saou <http://freshrpms.net/> 0.5.12-1
- Update to 0.5.12.

* Tue Sep 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.11-1
- Update to 0.5.11.

* Tue Sep 16 2008 Matthias Saou <http://freshrpms.net/> 0.5.10-1
- Update to 0.5.10.

* Tue Sep  9 2008 Matthias Saou <http://freshrpms.net/> 0.5.9-1
- Update to 0.5.9.

* Mon Sep  2 2008 Matthias Saou <http://freshrpms.net/> 0.5.8-1
- Update to 0.5.8.

* Tue Aug 26 2008 Matthias Saou <http://freshrpms.net/> 0.5.7-1
- Update to 0.5.7.

* Tue Aug 19 2008 Matthias Saou <http://freshrpms.net/> 0.5.6-1
- Update to 0.5.6.
- Require the exact same elisa version, as elisa and all plugins are always
  released all at once and should always match.

* Mon Aug 11 2008 Matthias Saou <http://freshrpms.net/> 0.5.5-1
- Update to 0.5.5.

* Fri Aug  8 2008 Matthias Saou <http://freshrpms.net/> 0.5.4-1
- Update to 0.5.4.

* Tue Jul 29 2008 Matthias Saou <http://freshrpms.net/> 0.5.3-1
- Update to 0.5.3.

* Wed Jul 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.2-2
- Update to 0.5.2.
- Update the build patch which is still required.
- Now build require the elisa-devel package.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-2
- Update to 0.5.1.
- Include install patch.

* Mon Jul 14 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-4
- Add xdg-user-dirs requirement, for xdg-user-dirs-update execution.

* Tue Jul  1 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-3
- Add libvisual-plugins requirement.

* Wed Apr 23 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-2
- Add pyxdg requirement (upstream bug #1206).

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Initial RPM release.

