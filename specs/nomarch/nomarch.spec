# $Id$

# Authority: dag

# Archs: i386 i686

Name: nomarch
Summary: GPLed Arc de-archiver 
Version: 1.3
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://rus.members.beeb.net/nomarch.html

Source: ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
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
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
