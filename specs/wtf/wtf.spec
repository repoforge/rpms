# Authority: dag

# Upstream: Thomas Sutton <thsutton@utas.edu.au>

Summary: Finds acronyms and filename suffixes information.
Name: wtf
Version: 0.0.4
Release: 1
License: GPL
Group: System Environment/Base
URL: http://cronus.comp.utas.edu.au/~thsutton/computing/wtf.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://cronus.comp.utas.edu.au/~thsutton/downloads/computing/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
The wtf program looks-up the definition of a term. It supports a number
of definition sources. In this version they are the acronyms database and
the filename suffixes database.

%prep
%setup

### FIXME: Makefile doesn't support the default autotools macros
%{__perl} -pi.orig -e '
		s|^DESTDIR\s+=.*$|DESTDIR =|;
		s|^prefix\s+=.*$|prefix = %{_prefix}|;
		s|^bindir\s+=.*$|bindir = %{_bindir}|;
		s|^datadir\s+=.*$|datadir = %{_datadir}/wtf|;
		s|^mandir\s+=.*$|mandir = %{_mandir}/man6|;
	' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS LICENSE NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/wtf/

%changelog
* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.0.4-0
- Updated to release 0.0.4.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 0.0.1-0
- Initial package. (using DAR)
