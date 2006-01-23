# $Id$
# Authority: matthias

# ExclusiveDist: fc5

%define httpd_mmn_version %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo badbuild)

Summary: Apache module providing ASP.NET functionality
Name: mod_mono
Version: 1.1.13
Release: 1
License: Apache Software License
Group: System
URL: http://www.mono-project.com/ASP.NET
Source: http://go-mono.com/sources/mod_mono/mod_mono-%{version}.tar.gz
Patch0: mod_mono-1.1.13-apr1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: httpd-mmn = %{httpd_mmn_version}, xsp
BuildRequires: httpd-devel, pkgconfig

%description
Apache module providing ASP.NET functionality using Mono.


%prep
%setup
%patch0 -p1 -b .apr1


%build
# We need to force apr-config, since only "apr-config" is checked, and it's
# required to add the proper apr include path to CFLAGS
%configure --with-apr-config=%{_bindir}/apr-1-config
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# Move the configuration file from main "conf" to proper "conf.d"
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__mv} -f   %{buildroot}%{_sysconfdir}/httpd/conf/mod_mono.conf \
             %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_mono.conf

# Rename the library to be non-versionned like all the others
%{__mv} -f %{buildroot}%{_libdir}/httpd/modules/mod_mono.so.?.?.? \
           %{buildroot}%{_libdir}/httpd/modules/mod_mono.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_mono.conf
%{_libdir}/httpd/modules/mod_mono.so*
%{_mandir}/man8/mod_mono.8*


%changelog
* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 1.1.13-1
- Initial RPM release.

