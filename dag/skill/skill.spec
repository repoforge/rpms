# Authority: dag

# Tag: test

Summary: An advanced set of utilities to send signals and prioritise processes.
Name: skill
Version: 4.1.1
Release: 0
License: BSD
Group: System Environment/Base
URL: http://www.cs.utah.edu/~forys/software.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.flux.utah.edu/pub/skill/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
skill is a program which sends signals to processes given any
combination of user names, ttys, commands, and pids. snice is a
program which changes the priority of processes (given the same).

It is similar to kill(1) and renice(8), however the command line is
completely order independent. There are also verbose, search, and
interactive modes of operation.

%prep
%setup

### FIXME: Let Makefile use standard autotools variables
%{__perl} -pi.orig -e '
		s|\${DESTDIR}|\$(DESTDIR)|;
		s|\${BINDIR}|\$(bindir)|;
		s|\${MANDIR}|\$(mandir)/man1|;
	' Makefile

%build
%{__make} %{?_smp_mflags} \
	OSTYPE="linux-1" \
	COPTS="%{optflags}" \
	LIBS="-s -N"

%install
%{__rm} -rf %{buildroot}

### FIXME: make install does not create target directories
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
### FIXME: Soapbox makes it work with the link, report upstream
%makeinstall
%{__ln_s} -f %{_bindir}/skill %{buildroot}%{_bindir}/snice

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%defattr(-, root, wheel, 0755)
%{_bindir}/*

%changelog
* Wed Aug 20 2003 Dag Wieers <dag@wieers.com> - 4.1.1-0
- Initial package. (using DAR)
