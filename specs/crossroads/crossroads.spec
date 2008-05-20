# $Id$
# Authority: dries
# Upstream: Karel Kubat <karel$kubat,nl>

Summary: Load balance and fail over utility for TCP based services
Name: crossroads
Version: 1.80
Release: 1
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
%{__make} %{?_smp_mflags} PREFIX=%{_prefix} local
#needs yo2man
#{__make} %{?_smp_mflags} PREFIX=%{_prefix} documentation

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man7
%{__make} install DESTDIR="%{buildroot}" PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%doc %{_mandir}/man1/crossroads*.1*
%doc %{_mandir}/man7/crossroads.conf.7*
%{_bindir}/crossroads
%{_bindir}/crossroads-daemon
%{_bindir}/crossroads-mgr

%changelog
* Tue May 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 1.63-1
- Initial package.
