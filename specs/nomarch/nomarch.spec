# $Id$
# Authority: dag

##Archs: i386 i686

Name: nomarch
Summary: GPLed Arc de-archiver
Version: 1.4
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://rus.members.beeb.net/nomarch.html

Source: ftp://ftp.ibiblio.org/pub/Linux/utils/compress/nomarch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
nomarch lists/extracts/tests `.arc' archives. (It also handles `.ark'
files, they're exactly the same.) This is a *very* outdated file
format which should never be used for anything new, but unfortunately,
you can still run into it every so often.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS README TODO
%doc %{_mandir}/man1/nomarch.1*
%{_bindir}/nomarch

%changelog
* Tue Jul 25 2006 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
