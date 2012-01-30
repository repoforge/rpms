# $Id$
# Authority: cheusov
# Upstream: NetBSD

Name: bmake
Version: 20111010
Release: 1%{?dist}

Summary: The NetBSD make(1) tool

License: BSD with advertising
Group: Development/Tools
Url: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/

Packager: Aleksey Cheusov <vle@gmx.net>

Source0: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/%{name}-%{version}.tar.gz
Source1: Linux.sys.mk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Requires: pkgsrc-mk-files

%description
bmake, the NetBSD make(1) tool, is a program designed to simplify the
maintenance of other programs.  The input of bmake is a list of specifications
indicating the files upon which the targets (programs and other files) depend.
bmake then detects which targets are out of date based on their dependencies
and triggers the necessary commands to bring them up to date when that happens.

bmake is similar to GNU make, even though the syntax for the advanced features
supported in Makefiles is very different.

%prep
%setup -q -n %name

%build
unset MAKEFLAGS
./boot-strap -q -o Linux --prefix=%{_prefix} \
  --with-default-sys-path=%{_prefix}/share/mk --mksrc none \
  --sysconfdir=/etc

%install
%{__install} -D -m 0644 bmake.1 %{buildroot}%{_mandir}/man1/bmake.1
%{__install} -D -m 0755 Linux/bmake %{buildroot}%{_bindir}/bmake
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/mk/sys.mk

%files
%doc ChangeLog README
%{_bindir}/bmake
%{_mandir}/man1/*
%{_datadir}/mk/sys.mk

%changelog
* Mon Jan 02 2012 Aleksey Cheusov <cheusov@NetBSD.org> 20111010-1
- update to 20111010 and adapted to repoforge

* Tue Dec 08 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt4
- add pkgsrc-mk-files require

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt3
- create dir for bmake macros

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 20081111-alt2
- Now bmake doesn't depend on mk-files

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 2 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20080515-1
- Initial release for Fedora.
