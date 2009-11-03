# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Bad Plugins for the Elisa Media Center
Name: elisa-plugins-bad
Version: 0.5.22
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/

Source: http://elisa.fluendo.com/static/download/elisa/elisa-plugins-bad-%{version}.tar.gz
Patch0: elisa-plugins-bad-0.5.2-install.patch
Patch1: elisa-plugins-bad-0.5.21-thumbnail.patch
Patch2: elisa-plugins-bad-0.5.21-dbus.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: elisa
BuildRequires: python-devel
Requires: dbus-python
Requires: elisa = %{version}
Requires: libvisual-plugins
Requires: gstreamer-plugins-good
Requires: gstreamer-python
Requires: pygtk2
Requires: python-coherence
Requires: python-cssutils
#Requires: python-gpod
Requires: python-pigment >= 0.3.4
Requires: python-twisted-core
Requires: python-twisted-web2
Requires: python-xdg
Requires: xdg-user-dirs

%description
This package contains the bad set of plugins for the Elisa Media Center.

%prep
%setup
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed \

### Clean up buildroot
### Remove Windows only plugins
%{__rm} -rf %{buildroot}%{python_sitelib}/elisa/plugins/elisa_updater/ \
            %{buildroot}%{python_sitelib}/elisa_plugin_elisa_updater* \
            %{buildroot}%{python_sitelib}/elisa/plugins/smbwin32/ \
            %{buildroot}%{python_sitelib}/elisa_plugin_smb_win32* \
            %{buildroot}%{python_sitelib}/elisa/plugins/winremote/ \
            %{buildroot}%{python_sitelib}/elisa_plugin_winremote* \
            %{buildroot}%{python_sitelib}/elisa/plugins/wmd/ \
            %{buildroot}%{python_sitelib}/elisa_plugin_wmd*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{python_sitelib}/elisa/plugins/amazon/
%{python_sitelib}/elisa/plugins/amp/
%{python_sitelib}/elisa/plugins/avahi/
%{python_sitelib}/elisa/plugins/coherence/
%{python_sitelib}/elisa/plugins/daap/
%{python_sitelib}/elisa/plugins/database/
%{python_sitelib}/elisa/plugins/discogs/
%{python_sitelib}/elisa/plugins/dvd/
%{python_sitelib}/elisa/plugins/favorites/
%{python_sitelib}/elisa/plugins/filtered_shares/
%{python_sitelib}/elisa/plugins/gstreamer/
%{python_sitelib}/elisa/plugins/http_client/
%{python_sitelib}/elisa/plugins/ipod/
%{python_sitelib}/elisa/plugins/osso/
%{python_sitelib}/elisa/plugins/pigment/
%{python_sitelib}/elisa/plugins/poblesec/
%{python_sitelib}/elisa/plugins/rss/
%{python_sitelib}/elisa/plugins/search/
%{python_sitelib}/elisa/plugins/shelf/
%{python_sitelib}/elisa/plugins/yesfm/
%{python_sitelib}/elisa_plugin_*

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 0.5.22-1
- Updated to release 0.5.22.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.5.21-2
- Added patches to disable dbus and fix CentOS specific items.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.5.21-1
- Updated to release 0.5.21.

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
- Exclude wmd plugin, the dependency problem should be fixed.
- Disable all %%lang translations, they're gone...

* Wed Jul 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.2-2
- Update to 0.5.2.
- List translations as %%lang.
- Update the build patch which is still required.
- Now build require the elisa-devel package.
- Update requirements.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-6
- Update to 0.5.1.
- Add python-cssutils requirement for the pigment theme plugin.
- Include install patch.
- Remove winremote plugin, it seems to be Windows specific (win32api req).
- Remove smbwin32 plugin, it seems to be Windows specific (win32net req).
- Remove wmd plugin, it seems to be Windows specific (win32api req)... NOT! As
  the poblesec plugin requires it anyway (ugly, should go away).
- Remove elisa_updater plugin, as we only want to update elisa with rpms.

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Initial RPM release.
