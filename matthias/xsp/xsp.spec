# $Id$
# Authority: matthias

# ExclusiveDist: fc5

Summary: Web server that hosts the Mono System.Webto run ASP.NET
Name: xsp
Version: 1.1.13
Release: 1
License: BSD
Group: System
URL: http://www.mono-project.com/ASP.NET
Source: http://go-mono.com/sources/xsp/xsp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mono-web
BuildRequires: pkgconfig, mono-web

%description
The XSP server is a small web server that hosts the Mono System.Web classes
for running what is commonly known as ASP.NET.


%package devel
Summary: Development files for the XSP web server
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
The XSP server is a small web server that hosts the Mono System.Web classes
for running what is commonly known as ASP.NET.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


#%post
#if [ $1 -eq 1 ]; then
#    /sbin/chkconfig --add foobar
#fi
#
#%preun
#if [ $1 -eq 0 ]; then
#    /sbin/service foobar stop >/dev/null 2>&1 || :
#    /sbin/chkconfig --del foobar
#fi
#
#%postun
#if [ $1 -ge 1 ]; then
#    /sbin/service foobar condrestart >/dev/null 2>&1 || :
#fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_prefix}/lib/xsp/
%{_libdir}/xsp/
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 1.1.13-1
- Initial RPM release.
- Room for enhancements in the package (init script?), then again if it works
  as-is when used with mod_mono, it might be enough.
- Build requires /dev/random, so doesn't work with default current mach.

