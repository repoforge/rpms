# $Id: _template.spec 471 2004-05-03 19:42:19Z dag $
# Authority: dag
# Upstream: 

%define real_version 0.3beta1

Summary: SWF output library
Name: ming
Version: 0.3
Release: 0.beta1
License: LGPL
Group: System Environment/Libraries
URL: http://www.opaque.net/ming/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ming/ming-%{real_version}.tar.bz2
Patch: ming-listmp3.c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ming is a c library for generating SWF ("Flash") format movies. This
package only contains the basic c-based library - not yet extensions for
Python, Ruby, etc.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}
%patch0 -p1

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%{__make} %{_smp_mflags} -C util listswf listfdb listmp3 listjpeg makefdb swftophp \
	CFLAGS="%{optflags}"

mkdir temp
for util in listswf listfdb listmp3 listjpeg makefdb swftophp; do
	mv $util temp/ming-$util
done

%install
%{__rm} -rf %{buildroot}
%makeinstall
#make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 util/temp/ming* %{buildroot}%{_bindir}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Fri May 14 2004 Dag Wieers <dag@wieers.com> -
- Initial package. (using DAR) 
