# $Id$
# Authority: dries
# Upstream: <roseg$apsis,ch>

Summary: Reverse HTTP proxy, load balancer and SSL wrapper
Name: pound
Version: 2.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.apsis.ch/pound/index.html

Source: http://www.apsis.ch/pound/Pound-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
Pound is a reverse HTTP proxy, load balancer, and SSL wrapper. It proxies 
client HTTPS requests to HTTP backend servers, distributes the requests 
among several servers while keeping sessions, supports HTTP/1.1 requests 
even if the backend server(s) are HTTP/1.0, and sanitizes requests.

%prep
%setup -n Pound-%{version}
%{__perl} -pi -e "s|-o \@I_OWNER\@ -g \@I_GRP\@| |g;" Makefile*
%{__perl} -pi -e "s| -s | |g;" Makefile*

%build
%configure --disable-super
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_sbindir} %{buildroot}%{_mandir}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG GPL.html FAQ README
%doc %{_mandir}/man8/pound*
%{_sbindir}/pound
%{_sbindir}/poundctl

%changelog
* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Updated to release 2.1.

* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
