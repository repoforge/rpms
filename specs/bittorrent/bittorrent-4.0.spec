# $Id$
# Authority: dag
# Upstream: Bram Cohen <bram$bitconjurer,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define desktop_vendor rpmforge

%define real_name BitTorrent

Summary: Network file transfer tool
Name: bittorrent
Version: 4.0.4
Release: 1%{?dist}
License: MIT
Group: Applications/Internet
URL: http://bittorrent.com/

Source: http://bittorrent.com/dl/BitTorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2.1, gtk2-devel >= 2.2, pygtk2 >= 2.4.0
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: python >= 2.3
Obsoletes: BitTorrent

%description
BitTorrent is a tool for copying files from one machine to
another. FTP punishes sites for being popular: Since all uploading is
done from one place, a popular site needs big iron and big
bandwidth. With BitTorrent, clients automatically mirror files they
download, making the publisher's burden almost nothing.

%package gui
Summary: GUI versions of the BitTorrent file transfer tool
Group: Applications/Internet
Requires: pygtk2 >= 2.4.0
Requires: %{name} = %{version}-%{release}

%description gui
This package contains the GUI versions of the BitTorrent file transfer tool.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >bittorrent.desktop
[Desktop Entry]
Name=BitTorrent Transfer Tool
Comment=Download files from the Internet
Exec=btdownloadgui.py
Icon=bittorrent.png
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Network;
MimeType=application/x-bittorrent;
Encoding=UTF-8
EOF

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 \
	--skip-build \
	--root %{buildroot}
%{__perl} -pi -e 's|env python2|env python|' %{buildroot}%{_bindir}/*.py

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 bittorrent.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/bittorrent.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		bittorrent.desktop
%endif

#convert bittorrent.ico bittorrent.png
%{__install} -D -m644 images/logo/bittorrent_96.png %{buildroot}%{_datadir}/pixmaps/bittorrent.png

%post gui
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun gui
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html *.txt
%{_bindir}/*.py
%exclude %{_bindir}/btdownloadgui.py
%dir %{python_sitelib}/BitTorrent/
%{python_sitelib}/BitTorrent/*.py
%{python_sitelib}/BitTorrent/*.pyc
%ghost %{python_sitelib}/BitTorrent/*.pyo
%{_datadir}/pixmaps/BitTorrent-%{version}/
%exclude %{_docdir}/BitTorrent-%{version}/

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/btdownloadgui.py
%{_datadir}/pixmaps/bittorrent.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-bittorrent.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/bittorrent.desktop}

%changelog
* Sat Aug 27 2005 Dag Wieers <dag@wieers.com> - 4.0.4-1
- Updated to release 4.0.4.

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
