# $Id$
# Authority: dag
# Upstream: splint$splint,org

### EL5 ships with splint-3.1.1-16.el5
### EL4 ships with splint-3.1.1-4
### EL3 ships with splint-3.0.1.7-0.20030123
%{?el3:# Tag: rfx}
# ExcludeDist: el4 el5

Summary: Secure programming lint
Name: splint
Version: 3.1.1
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.splint.org/

Source: http://www.splint.org/downloads/splint-%{version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison
Provides: lclint = %{version}
Obsoletes: lclint

%description
Splint is a tool for statically checking C programs for security
vulnerabilities and coding mistakes. With minimal effort, Splint
can be used as a better lint. If additional effort is invested
adding annotations to programs, Splint can perform stronger
checking than can be done by any standard lint.

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/html/ doc/linux.html doc/manual*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/splint/

%changelog
* Mon Mar 08 2004 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Added --program-prefix to %%configure.

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 3.1.1-0
- Updated to release 3.1.1.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 3.0.1.6-0
- Initial package. (using DAR)
