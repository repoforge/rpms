# $Id$
# Authority: cheusov
# Upstream: NetBSD

Summary: The NetBSD make(1) tool
Name: bmake
Version: 20111010
Release: 1%{?dist}
License: BSD with advertising
Group: Development/Tools
URL: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/

Source0: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/bmake-%{version}.tar.gz
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
%setup -n %{name}

%build
unset MAKEFLAGS
./boot-strap -o Linux \
    --prefix="%{_prefix}" \
    --sysconfdir="%{_sysconfdir}" \
    --with-default-sys-path="%{_datadir}/mk" \
    --mksrc none

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 bmake.1 %{buildroot}%{_mandir}/man1/bmake.1
%{__install} -Dp -m0755 Linux/bmake %{buildroot}%{_bindir}/bmake
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/mk/sys.mk

%files
%doc ChangeLog README
%doc %{_mandir}/man1/bmake.1*
%{_bindir}/bmake
%{_datadir}/mk/

%changelog
* Mon Jan 02 2012 Aleksey Cheusov <cheusov@NetBSD.org> 20111010-1
- Update to 20111010 and adapted to Repoforge.

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
