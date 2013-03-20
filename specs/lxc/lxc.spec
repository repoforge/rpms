# $Id$
# Authority: dfateyev
# Upstream:  Daniel Lezcano <dlezcano$fr,ibm,com>

### LXC works only with kernel >= 2.6.27
# ExcludeDist: el3 el4 el5

%define real_version 0.8.0-rc2

Name:           lxc
Version:        0.8.0
Release:        1%{?dist}
Summary:        Linux Resource Containers

Group:          Applications/System
License:        LGPLv2+
URL:            http://lxc.sourceforge.net
Source0:        http://lxc.sourceforge.net/download/lxc/%{name}-%{real_version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  automake
BuildRequires:  docbook-utils-pdf
BuildRequires:  kernel-headers
BuildRequires:  libcap-devel
BuildRequires:  libtool

%description
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

%package        libs
Summary:        Runtime library files for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description    libs
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-libs package contains libraries for running %{name} applications.

%package        templates
Summary:        Templates for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       debootstrap

%description    templates
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-template package contains templates for creating containers.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
%setup -n %{name}-%{real_version}

%build
%configure F77=no
# Fix binary-or-shlib-defines-rpath error
%{__sed} -i '/AM_LDFLAGS = -Wl,-E -Wl,-rpath -Wl,$(libdir)/d' src/lxc/Makefile.in
%{__make} %{?_smp_mflags}

%check
%{__make} check

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
%{__mkdir} -p %{buildroot}%{_sharedstatedir}/%{name}
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{name}

%clean
%{__rm} -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/%{name}-*
%{_mandir}/man*/%{name}*
%{_sharedstatedir}/%{name}
%{_localstatedir}/lib/%{name}

%files libs
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%dir %{_libdir}/lxc
%dir %{_libdir}/lxc/templates
%{_libdir}/liblxc.so.*
%{_libdir}/lxc/rootfs
%{_libexecdir}/lxc/lxc-init

%files templates
%defattr(-,root,root,-)
%{_libdir}/lxc/templates/lxc-*

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc
%{_includedir}/*
%{_libdir}/liblxc.so

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}

%changelog
* Thu Aug  2 2012 IWAI, Masaharu <iwaim.sub@gmail.com> 0.8.0-1.rc2
- build for CentOS

* Wed Apr 25 2012 Daisuke SUZUKI <daisuke@linux.or.jp> 0.8.0-0.rc1
- new upstream release 

* Thu Jan 26 2012 Daisuke SUZUKI <daisuke@linux.or.jp> 0.7.5-1.20120105
- update to git current (20120105)

* Mon Jun 06 2011 Daisuke SUZUKI <daisuke@linux.or.jp> 0.7.4.2-1
- update to 0.7.4.2

* Thu Apr 28 2011 Daisuke SUZUKI <daisuke@linux.or.jp> 0.7.4.1-2
- include all templates

* Wed Apr 27 2011 Daisuke SUZUKI <daisuke@linux.or.jp> 0.7.4.1-1
- initial build for Vine Linux

* Fri Mar 25 2011 Silas Sewell <silas@sewell.ch> - 0.7.4.1-1
- Update to 0.7.4.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 Silas Sewell <silas@sewell.ch> - 0.7.2-1
- Update to 0.7.2
- Remove templates

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.7.1-1
- Update to 0.7.1

* Wed Feb 17 2010 Silas Sewell <silas@sewell.ch> - 0.6.5-1
- Update to latest release
- Add /var/lib/lxc directory
- Patch for sys/stat.h

* Fri Nov 27 2009 Silas Sewell <silas@sewell.ch> - 0.6.4-1
- Update to latest release
- Add documentation sub-package

* Mon Jul 27 2009 Silas Sewell <silas@sewell.ch> - 0.6.3-2
- Apply patch for rawhide kernel

* Sat Jul 25 2009 Silas Sewell <silas@sewell.ch> - 0.6.3-1
- Initial package
