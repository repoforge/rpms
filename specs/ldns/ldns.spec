# $Id$
# Authority: shuff
# Upstream: <ldns-users$open,nlnetlabs,nl>

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

Summary: DNS(SEC) library based on Net::DNS
Name: ldns
Version: 1.6.12
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.nlnetlabs.nl/projects/ldns/

Source: http://www.nlnetlabs.nl/downloads/ldns/ldns-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: swig

%description
ldns is a library with the aim to simplify DNS programing in C. All
lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-pyldns
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description -n python-pyldns
This package contains Python support for %{name}.
%prep
%setup

%build
%configure \
    --disable-rpath \
    --disable-static \
    --disable-gost \
    --with-pyldns \
    --with-pyldnsx \
    --with-drill \
    --with-examples \
    --with-ssl

%{__make} %{?_smp_mflags}
make %{?_smp_mflags} doc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install-doc DESTDIR="%{buildroot}"

%{__rm} -rf doc/man
%{__rm} -rf doc/doxyparse.pl

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog LICENSE README
%doc %{_mandir}/man1/*
%{_bindir}/drill
%{_bindir}/ldns-chaos
%{_bindir}/ldns-compare-zones
%{_bindir}/ldns-[d-z]*
%{_bindir}/ldnsd
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%doc %{_mandir}/man3/*
%{_bindir}/ldns-config
%{_includedir}/ldns/
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%files -n python-pyldns
%defattr(-, root, root, 0755)
%{python_sitearch}/*
%exclude %{python_sitearch}/*.la

%changelog
* Wed Mar 7 2012 Steve Huff <shuff@vecna.org> - 1.6.12-1
- Initial package (ported from spec in dist).
