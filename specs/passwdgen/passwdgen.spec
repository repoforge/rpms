# $Id$

# Authority: dag

# Distcc: 0
# Soapbox: 0

Summary: Random Password Generator
Name: passwdgen
Version: 2.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://members-http-1.rwc1.sfba.home.net/denisl/passwdgen/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://members-http-1.rwc1.sfba.home.net/denisl/passwdgen/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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

%build
%configure
### FIXME: Workaround in strange build-problem
%{__mkdir} -p class/.libs/.libs
%{__ln_s} -f ../libpasswdgen.so class/.libs/.libs/libpasswdgen.so

### FIXME: Fix headerfiles
%{__perl} -pi.orig -e 's|<string>|<string.h>|' class/*.h
%{__make} %{?_smp_mflags} %{?rh80:CXX="g++296"}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/passwdgen/

%changelog
* Mon Dec 30 2002 Dag Wieers <dag@wieers.com> - 2.2-0
- Initial package. (using DAR)
