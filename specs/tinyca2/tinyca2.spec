# $Id$
# Authority: dag
# Upstream: <sm$sm-zone,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical Tool for Managing a Certification Authority
Name: tinyca2
Version: 0.7.5
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tinyca.sm-zone.net/

Source:	http://tinyca.sm-zone.net/tinyca2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, perl-Gtk2
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: perl, perl-Gtk2, perl-MIME-tools

Obsoletes: TinyCA <= %{version}

%description
TinyCA is a graphical tool written in Perl/Gtk to manage a small
Certification Authority (CA) using openssl.

TinyCA supports - creation and revocation of x509 - S/MIME
certificates.

%prep
%setup

%{__perl} -pi.orig -e '
		s|./lib|%{_datadir}/TinyCA2/lib|g;
		s|./locale|%{_datadir}/TinyCA2/locale|g;
		s|./templates|%{_datadir}/TinyCA2/templates|g;
	' tinyca2

%build
%{__make} -C po

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 templates/openssl.cnf %{buildroot}%{_datadir}/TinyCA2/templates/openssl.cnf
%{__install} -Dp -m0755 tinyca2 %{buildroot}%{_bindir}/tinyca2

%{__install} -d -m0755 %{buildroot}%{_datadir}/TinyCA2/locale/
%{__cp} -apv locale/* %{buildroot}%{_datadir}/TinyCA2/locale/

%{__install} -d -m0755 %{buildroot}%{_datadir}/TinyCA2/lib/
%{__cp} -apv lib/* %{buildroot}%{_datadir}/TinyCA2/lib/

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 tinyca2.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/tinyca.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		tinyca2.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL
%{_bindir}/tinyca2
%{_datadir}/TinyCA2/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/tinyca2.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-tinyca2.desktop}

%changelog
* Mon Jul 31 2006 Dag Wieers <dag@wieers.com> - 0.7.5-2
- Use desktop file from upstream. (David Hrbac)

* Thu Jul 27 2006 Dag Wieers <dag@wieers.com> - 0.7.5-1
- Updated to release 0.7.5.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

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
