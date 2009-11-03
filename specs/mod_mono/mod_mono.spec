# $Id$

# Authority: dag

Summary: Run ASP.NET pages on Unix with Apache and Mono!
Name: mod_mono
Version: 0.7
Release: 0%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.apacheworld.org/modmono/

Source: http://www.go-mono.org/archive/mod_mono-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mono-devel, xsp, pkgconfig, httpd-devel
Requires: mono, xsp, httpd

%description
mod_mono is a module that interfaces Apache with Mono and allows running
ASP.NET pages on Unix and Unix-like systems.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|\$\(LIBEXECDIR\)|\$(libdir)/httpd/modules|g;' Makefile.in */Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc ChangeLog COPYING INSTALL README
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/httpd/modules/mod_mono.so

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.7-0
- Initial package. (using DAR)
