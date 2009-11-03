# $Id$
# Authority: dries
# Upstream: Karel Kubat <karel$kubat,nl>

Summary: Load balance and fail over utility for TCP based services
Name: crossroads
Version: 2.41
Release: 1%{?dist}
License: GPLv3
Group: Applications/Utilities
URL: http://crossroads.e-tunity.com/

Source: http://crossroads.e-tunity.com/downloads/versions/crossroads-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
Crossroads is an open source load balance and fail over utility for TCP based 
services. It is a daemon running in user space, and features extensive 
configurability, polling of back ends using 'wakeup calls', detailed status 
reporting, 'hooks' for special actions when backend calls fail, and much more. 
Crossroads is service-independent: it is usable for HTTP(S), SSH, SMTP, DNS, 
etc.. In the case of HTTP balancing, Crossroads can provide 'session 
stickiness' for back end processes that need sessions, but aren't session-aware 
of other back ends.

%prep
%setup
%{__perl} -pi -e 's|use PROMPT to|Use PROMPT to|g;' src/crossroads-mgr/*

%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix} BINDIR=%{_sbindir} local
#needs yo2man
#{__make} %{?_smp_mflags} PREFIX=%{_prefix} BINDIR=%{_sbindir} documentation

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man7
%{__make} install DESTDIR="%{buildroot}" BINDIR=%{buildroot}%{_sbindir} PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%doc %{_mandir}/man1/xr*.1*
%doc %{_mandir}/man1/xrctl.1*
%doc %{_mandir}/man5/xrctl.xml.5*
%{_sbindir}/xrctl
%{_sbindir}/xr

%changelog
* Fri Jan  9 2009 Dries Verachtert <dries@ulyssis.org> - 2.41-1
- Updated to release 2.41.

* Thu Nov 20 2008 Dries Verachtert <dries@ulyssis.org> - 2.36-1
- Updated to release 2.36.

* Fri Sep 12 2008 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Mon Aug 11 2008 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Updated to release 2.00.

* Tue May 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 1.63-1
- Initial package.
