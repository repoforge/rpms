# $Id$
# Authority: dries
# Upstream: Giuseppe Martino <denever$users,sourceforge,net>
# Upstream: <aldo-main$nongnu,org>

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Morse tutor
Name: aldo
Version: 0.7.0
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/aldo/

Source: http://savannah.nongnu.org/download/aldo/aldo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, automake, autoconf, readline-devel, libao-devel

%description
Aldo is a morse tutor released under GPL.
At this moment Aldo has four kinds of exercises:
* Classic exercise: With this exercise you must guess some random
strings of characters that Aldo plays in morse code.
* Koch method
* Read from file: with this exercise you can write something in a text
file and read this file with Aldo.
Callsign exercise: with this exercise you can training yourself reciving
random generated callsigns

%prep
%setup

%build
%{__aclocal} -I config
%{__autoheader}
%{__automake} --gnu --add-missing
%{__autoconf}
%configure
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_mandir}/man1/aldo*
%{_bindir}/aldo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-2.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.0-2
- Libao-devel added to buildrequirements.

* Sat Oct 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1
- Updated to release 0.6.8.

* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 0.6.5-1
- initial package
