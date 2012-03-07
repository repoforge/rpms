# $Id$
# Authority: shuff
# Upstream: <unbound-bugs$nlnetlabs,nl>

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

%define unbounddir %{_localstatedir}/unbound
%define unbounduser unbound

Summary: Validating recursive caching DNS resolver
Name: unbound
Version: 1.4.16
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://unbound.net/

Source: http://unbound.net/downloads/unbound-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: expat-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: ldns-devel
BuildRequires: libevent-devel >= 1.3
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: swig
Requires: openssl

%description
Unbound is a validating, recursive, and caching DNS resolver.

The C implementation of Unbound is developed and maintained by NLnet Labs. It
is based on ideas and algorithms taken from a Java prototype developed by
Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also DNSSEC (secure
DNS) validation and stub-resolvers (that do not run as a server, but are linked
into an application) are easily possible.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-libunbound
Summary: Python support for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python(abi)

%description -n python-libunbound
This package contains Python support for %{name}.

%prep
%setup

%build
%configure \
    --with-libevent \
    --with-conf-file="%{unbounddir}/unbound.conf" \
    --with-pidfile="%{unbounddir}/run/unbound/unbound.pid" \
    --with-run-dir="%{unbounddir}" \
    --with-chroot-dir="%{unbounddir}" \
    --with-rootkey-file="%{unbounddir}/root.key" \
    --with-rootcert-file="%{unbounddir}/pki/tls/certs/ca-bundle.crt" \
    --with-pyunbound \
    --with-pythonmodule \
    --disable-gost

%{__make} %{?_smp_mflags}

%{__rm} -rf doc/man

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -m0700 -d %{buildroot}%{_localstatedir}/unbound
%{__install} -m0755 -d %{buildroot}%{_initrddir}
%{__install} -m0755 contrib/unbound.init %{buildroot}%{_initrddir}/unbound
%{__ln_s} %{_localstatedir}/unbound/unbound.conf %{buildroot}%{_sysconfdir}/unbound.conf

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%pre
getent group %{unbounduser} >/dev/null || groupadd -r %{unbounduser}
getent passwd %{unbounduser} >/dev/null || \
useradd -r -g %{unbounduser} -d %{unbounddir} -s /sbin/nologin \
    -c "unbound name daemon" %{unbounduser}
exit 0

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add unbound

%preun
if [ $1 -eq 0 ]; then
    /sbin/service unbound stop >/dev/null 2>&1
    /sbin/chkconfig --del unbound
    # remove root jail 
    rm -f %{unbounddir}/dev/log %{unbounddir}/dev/random %{unbounddir}/etc/localtime %{unbounddir}/etc/resolv.conf >/dev/null 2>&1
    rmdir %{unbounddir}/dev >/dev/null 2>&1 || :
    rmdir %{unbounddir}/etc >/dev/null 2>&1 || :
    rmdir %{unbounddir} >/dev/null 2>&1 || :
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service unbound condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, 0755)
%doc LICENSE README contrib/
%doc %{_mandir}/man[1,5,8]/*
%attr(0755,%{unbounduser},%{unbounduser}) %dir %{_initrddir}/unbound
%attr(0700,%{unbounduser},%{unbounduser}) %{unbounddir}
%attr(0644,%{unbounduser},%{unbounduser}) %config(noreplace) %{unbounddir}/unbound.conf
%attr(0644,%{unbounduser},%{unbounduser}) %config(noreplace) %{_sysconfdir}/unbound.conf
%{_sbindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man3/*
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files -n python-libunbound
%defattr(-, root, root, 0755)
%{python_sitearch}/*

%changelog
* Wed Mar 7 2012 Steve Huff <shuff@vecna.org> - 1.4.16-1
- Initial package (ported from unbound.spec in dist)
