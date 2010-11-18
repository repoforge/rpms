# $Id$
# Authority: dag

Summary: AMR WideBand speech codec
Name: amrwb
Version: 7.0.0.3
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.penguin.cz/~utx/amr

#Source: ftp://ftp.freebsd.org/pub/FreeBSD/ports/local-distfiles/kwm/amrwb-%{version}.tar.gz
#Source: http://distfiles.opendarwin.org/amrwb-%{version}.tar.gz
Source0: http://ftp.penguin.cz/pub/users/utx/amr/amrwb-%{version}.tar.bz2
Source1: http://www.3gpp.org/ftp/Specs/archive/26_series/26.204/26204-700.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
AMR-WB is a wideband speech codec used in mobile phones.

%package devel
Summary: AMR WideBand speech codec development files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
AMR-WB is a wideband speech codec used in mobile phones development files.

%prep
%setup
%{__cp} -v %{SOURCE1} .

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/amrwb-decoder
%{_bindir}/amrwb-decoder-if2
%{_bindir}/amrwb-encoder
%{_bindir}/amrwb-encoder-if2
%{_libdir}/libamrwb.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/amrwb/
%{_libdir}/libamrwb.so
%exclude %{_libdir}/libamrwb.la

%changelog
* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 7.0.0.3-1
- Initial package. (using DAR)
