# $Id$
# Authority: matthias

Summary: AMR NarrowBand speech codec
Name: amrnb
Version: 0.0.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.3gpp.org/
Source: ftp://ftp.freebsd.org/pub/FreeBSD/ports/local-distfiles/kwm/amrnb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
AMR-NB is a narrowband speech codec used in mobile phones.


%package devel
Summary: AMR NarrowBand speech codec development files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
AMR-NB is a narrowband speech codec used in mobile phones development files.


%prep
%setup


%build
%configure --enable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,0755)
%doc COPYING
%{_libdir}/libamrnb.so.*

%files devel
%defattr(-,root,root,0755)
%{_includedir}/amrnb/
%{_libdir}/libamrnb.a
%exclude %{_libdir}/libamrnb.la
%{_libdir}/libamrnb.so


%changelog
* Fri Dec 16 2005 Matthias Saou <http://freshrpms.net/> 0.0.1-1
- Spec file inclusion in rpmforge.

* Wed Sep 07 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.0.1-0.lvn.1: initial package

