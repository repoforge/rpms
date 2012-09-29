# $Id$
# Authority: dfateyev

Name: slowhttptest
Version: 1.5
Release: 1%{?dist}
Summary: SlowHTTPTest

Group: Applications/System
License: GPL
URL: http://code.google.com/p/slowhttptest/
Source0: http://slowhttptest.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel


%description
SlowHTTPTest is a highly configurable tool that simulates
some Application Layer Denial of Service attacks.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/slowhttptest
%{_mandir}/man1/slowhttptest.1.gz


%changelog
* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 1.5-1
- Rebuild for Repoforge

* Fri Sep 14 2012 Denis Fateyev <denis@fateyev.com> - 1.5-1.denf
- Update to 1.5

* Fri Feb 24 2012 Denis Fateyev <denis@fateyev.com> - 1.4-1.denf
- Initial build for 'denf' rhel/centos repository
