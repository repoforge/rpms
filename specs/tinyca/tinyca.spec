# $Id$
# Authority: dag
# Upstream: <sm$sm-zone,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical Tool for Managing a Certification Authority
Name: tinyca
Version: 0.7.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tinyca.sm-zone.net/

Source:	http://tinyca.sm-zone.net/tinyca-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: openssl, Gtk-Perl

Obsoletes: TinyCA < %{version}

%description
TinyCA is a graphical tool written in Perl/Gtk to manage a small
Certification Authority (CA) using openssl.

TinyCA supports - creation and revocation of x509 - S/MIME
certificates.

%prep
%setup

%{__perl} -pi.orig -e '
		s|./lib|%{_datadir}/tinyca|g;
		s|./locale|%{_datadir}/locale|g;
		s|./templates|%{_sysconfdir}/tinyca|g;
	' tinyca

%{__cat} <<EOF >tinyca.desktop
[Desktop Entry]
Name=TinyCA Certification Authority
Comment=Work with various certificates
Exec=tinyca
Type=Application
Encoding=UTF-8
Icon=redhat-accessories.png
Categories=GNOME;Application;Utility;
EOF

%build
%{__make} -C po

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 templates/openssl.cnf %{buildroot}%{_sysconfdir}/tinyca/openssl.cnf
%{__install} -Dp -m0755 tinyca %{buildroot}%{_bindir}/tinyca

%{__install} -d -m0755 %{buildroot}%{_datadir}/locale/
%{__cp} -apv locale/* %{buildroot}%{_datadir}/locale/

%{__install} -d -m0755 %{buildroot}%{_datadir}/tinyca/
%{__cp} -apv lib/* %{buildroot}%{_datadir}/tinyca/

%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 tinyca.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/tinyca.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		tinyca.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL
%config %{_sysconfdir}/tinyca/
%{_bindir}/tinyca
%{_datadir}/tinyca/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/tinyca.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-tinyca.desktop}

%changelog
* Fri Jun 30 2006 Dag Wieers <dag@wieers.com> - 0.7.4-1
- Updated to release 0.7.4.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Updated to release 0.6.8.

* Tue Dec 07 2004 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Updated to release 0.6.7.

* Sat Aug 14 2004 Dag Wieers <dag@wieers.com> - 0.6.6-1
- Updated to release 0.6.6.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Wed Jun 16 2004 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Initial package. (using DAR)
