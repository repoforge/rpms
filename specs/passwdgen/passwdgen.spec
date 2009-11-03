# $Id$
# Authority: dag


Summary: Random Password Generator
Name: passwdgen
Version: 2.2
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://directory.fsf.org/security/auth/pwdgen.html
#URL: http://www.securityfocus.com/tools/1649/scoreit
#URL: http://members-http-1.rwc1.sfba.home.net/denisl/passwdgen/

Source: http://www.securityfocus.com/data/tools/passwdgen-%{version}.tar.gz
#Source: http://members-http-1.rwc1.sfba.home.net/denisl/passwdgen/download/passwdgen-%{version}.tar.gz
Patch0: passwdgen-2.2-lafix.patch
Patch1: passwdgen-2.2-gcc3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, autoconf, automake

%description
passwdGen is a flexible but user-friendly random password generator. It should
be extremely useful for network administrators, or simply those who wish to
change their passwords often, and would rather not use dictionary words.

passwdGen is implemented in two pieces, a C++ class library, and one or more
user interfaces. This allows passwdGen to look consistant with whatever
environment you happen to use. It should also encourage people to write their
own front-ends based on their own needs.

passwdGen itself is released under the terms of the GNU GPL and is free
software. Recently however, I've developed passwdGen Pocket, a non-free though
inexpensive feature complete port for the Palm OS platform. If you use
passwdGen and have a Palm OS based PDA I would greatly appreciate your support.

%prep
%setup
%patch0 -p0
%patch1 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/passwdgen.1*
%{_bindir}/passwdgen
%{_includedir}/passwdgen/
%{_libdir}/libpasswdgen.so
%{_libdir}/libpasswdgen-2.2.so*
%exclude %{_libdir}/libpasswdgen.a
%exclude %{_libdir}/libpasswdgen.la

%changelog
* Mon May 07 2007 Dag Wieers <dag@wieers.com> - 2.2-2
- Added build patched from PLD.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 2.2-1
- Cosmetic changes.

* Mon Dec 30 2002 Dag Wieers <dag@wieers.com> - 2.2-0
- Initial package. (using DAR)
