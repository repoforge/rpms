# $Id$
# Authority: dag
# Upstream: Emmanuel Saracco <esaracco$noos,fr>

%define desktop_vendor rpmforge

Summary: Graphical link validity checker
Name: gurlchecker
Version: 0.7.15
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://labs.libre-entreprise.org/projects/gurlchecker/

Source: http://labs.libre-entreprise.org/download/gurlchecker/gurlchecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0, libglade2-devel >= 2.0, gnet2 >= 2.0
BuildRequires: gnet2-devel, gnutls-devel, gettext, desktop-file-utils

%description
gURLChecker is a graphical web link checker. It can work on a whole
site, a single local page or a browser bookmarks file.

%prep
%setup

%{__cat} <<EOF >gurlchecker.desktop
[Desktop Entry]
Name=Website URL Validator
Comment=Find broken links on websites
Icon=gnome-spider.png
Exec=gurlchecker
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Network;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gurlchecker.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_datadir}/gtk-doc/html/gurlchecker/
%{_bindir}/gurlchecker
%{_datadir}/applications/*gurlchecker.desktop
%{_datadir}/gurlchecker/

%changelog
* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 0.7.15-2
- Fixed the proper Source-tag, use real 0.7.15 tarball. (Jeff Moe)

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 0.7.15-1
- Updated to release 0.7.15.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 0.7.14-1
- Updated to release 0.7.14.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.7.13-1
- Updated to release 0.7.13.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 0.7.12-1
- Updated to release 0.7.12.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.7.11-1
- Updated to release 0.7.11.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.7.10-0
- Updated to release 0.7.10.

* Fri Mar 05 2004 Dag Wieers <dag@wieers.com> - 0.7.9-0
- Updated to release 0.7.9.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.7.8-0
- Updated to release 0.7.8.

* Mon Jan 12 2004 Dag Wieers <dag@wieers.com> - 0.7.6-0
- Updated to release 0.7.6.

* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 0.7.5-0
- Updated to release 0.7.5.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 0.7.4-0
- Updated to release 0.7.4.

* Mon Nov 03 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Updated to release 0.7.2.

* Thu Oct 02 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.5.5-0
- Updated to release 0.5.5.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Updated to release 0.5.4.

* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 0.5.3-0
- Updated to release 0.5.3.

* Tue Jun 17 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 0.4.1-0
- Updated to release 0.4.1.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.3.14-0
- Updated to release 0.3.14.

* Thu May 08 2003 Dag Wieers <dag@wieers.com> - 0.3.13-0
- Updated to release 0.3.13.

* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 0.3.12-0
- Updated to release 0.3.12.

* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 0.3.11-0
- Updated to release 0.3.11.

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.3.10-0
- Updated to release 0.3.10.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.3.9-0
- Updated to release 0.3.9.

* Sat Apr 19 2003 Dag Wieers <dag@wieers.com> - 0.3.8-0
- Updated to release 0.3.8.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.3.5.3-0
- Updated to release 0.3.5-3.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 0.3.5-2
- Updated to release 0.3-5b.

* Fri Mar 21 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Updated to release 0.3-4.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Updated to release 0.3-2.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Updated to release 0.3-0.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Updated to release 0.2-0.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.1.6-0
- Initial package. (using DAR)
