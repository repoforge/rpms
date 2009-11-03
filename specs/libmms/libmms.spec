# $Id$
# Authority: matthias

Summary: MMS stream protocol library
Name: libmms
Version: 0.3
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libmms
Source: http://downloads.sf.net/libmms/libmms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel

%description
Library implementing the MMS streaming protocol.


%package devel
Summary: Development files for libmms
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
Files required for developing applications that will use the MMS streaming
protocol using libmms.


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


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING.LIB ChangeLog README* TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmms/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmms.pc


%changelog
* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 0.3-1
- Update to 0.3.
- Remove HTTP_PROXY support patch which is now included.

* Tue Mar 28 2006 Matthias Saou <http://freshrpms.net/> 0.2-2
- Add HTTP_PROXY support patch from Daniel S. Rogers.

* Thu Mar 23 2006 Matthias Saou <http://freshrpms.net/> 0.2-1
- Initial RPM release.

