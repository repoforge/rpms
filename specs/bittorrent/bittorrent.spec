# $Id$
# Authority: dag
# Upstream: Bram Cohen <bram$bitconjurer,org>

### Requires python >= 2.3, works on 2.2.1+ too (Pasi Pirhonen)

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name BitTorrent

%define desktop_vendor rpmforge

Summary: Network file transfer tool
Name: bittorrent
Version: 4.4.0
Release: 1%{?dist}
License: BitTorrent Open Source License
Group: Applications/Internet
URL: http://bittorrent.com/

Source: http://bittorrent.com/dl/BitTorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2.1, pygtk2-devel >= 2.6, gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: python >= 2.2.1, python-khashmir, python-crypto
Obsoletes: BitTorrent <= %{version}

%description
BitTorrent is a tool for copying files from one machine to
another. FTP punishes sites for being popular: Since all uploading is
done from one place, a popular site needs big iron and big
bandwidth. With BitTorrent, clients automatically mirror files they
download, making the publisher's burden almost nothing.

%package gui
Summary: GUI versions of the BitTorrent file transfer tool
Group: Applications/Internet
Requires: pygtk2 >= 2.6
Requires: %{name} = %{version}-%{release}

%description gui
This package contains the GUI versions of the BitTorrent file transfer tool.

%package -n python-khashmir
Summary: Distributed hash table library of the Kademlia flavor for python
Group: Development/Libraries

%description -n python-khashmir
Khashmir is a distributed hash table library of the Kademlia flavor
implemented in Python.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e "s|dp = os.path.join\('share', 'doc'    , appdir\)|dp = '%{_docdir}/%{name}-%{version}/'|" BitTorrent/__init__.py

%{__cat} <<EOF >bittorrent.desktop
[Desktop Entry]
Name=BitTorrent Transfer Tool
Comment=Download files from the Internet
Exec=bittorrent
Icon=bittorrent.png
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Network;
MimeType=application/x-bittorrent;
Encoding=UTF-8
EOF

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--skip-build \
	--root "%{buildroot}"
%find_lang %{name}
%{__perl} -pi -e 's|env python2|env python|' %{buildroot}%{_bindir}/*

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 bittorrent.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/bittorrent.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		bittorrent.desktop
%endif

%{__install} -Dp -m644 images/logo/bittorrent_96.png %{buildroot}%{_datadir}/pixmaps/bittorrent.png

%post gui
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun gui
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc *.html *.txt
%{_bindir}/*
%exclude %{_bindir}/bittorrent
%{python_sitelib}/BitTorrent/
%{_datadir}/pixmaps/BitTorrent-%{version}/
%exclude %{_docdir}/BitTorrent-%{version}/

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/bittorrent
%{_datadir}/pixmaps/bittorrent.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-bittorrent.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/bittorrent.desktop}

%files -n python-khashmir
%defattr(-, root, root, 0755)
%{python_sitelib}/khashmir/

%changelog
* Wed Feb 01 2006 Dag Wieers <dag@wieers.com> - 4.4.0-1
- Updated to release 4.4.0.

* Sun Dec 18 2005 Dag Wieers <dag@wieers.com> - 4.2.2-1
- Updated to release 4.2.2.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 4.2.1-1
- Updated to release 4.2.1.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 4.2.0-2
- Updated to release 4.2.0.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 4.1.4-2
- Added python-crypto dependency. (Jim Perrin, Petr Klíma)

* Sat Aug 27 2005 Dries Verachtert <dries@ulyssis.org> - 4.1.4-1
- Update to release 4.1.4.

* Thu Jun 23 2005 Dries Verachtert <dries@ulyssis.org> - 4.1.2-1
- Updated to release 4.1.2.

* Sun May 29 2005 Dag Wieers <dag@wieers.com> - 4.1.1-2
- Small fix for About to work.

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 4.1.1-1
- Updated to release 4.1.1.

* Fri May 20 2005 Dag Wieers <dag@wieers.com> - 4.1.0-1
- Updated to release 4.1.0.

* Sun Apr 10 2005 Dag Wieers <dag@wieers.com> - 4.0.1-1
- Updated to release 4.0.1.

* Wed Mar 09 2005 Dag Wieers <dag@wieers.com> - 4.0.0-1
- Updated to release 4.0.0.

* Wed Jan 12 2005 Dag Wieers <dag@wieers.com> - 3.9.0-3
- Replaced wxpython dependency by pgtk2. (Paul Howarth, Jorge Bartos)

* Fri Jan 07 2005 Dag Wieers <dag@wieers.com> - 3.9.0-2
- Fixed python dependency problem. (Igor Guarisma)

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 3.9.0-1
- Updated to release 3.9.0.

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 3.4.2-1
- Initial package. (using DAR)
