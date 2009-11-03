# $Id$
# Authority: dag

Summary: The skarnet.org development library
Name: skalibs
Version: 0.45
Release: 1%{?dist}
License: BSD
Group: Development/Other
URL: http://www.skarnet.org/software/skalibs/

Source: http://www.skarnet.org/software/skalibs/skalibs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
skalibs is a package centralizing the public-domain C
development files used for building other skarnet.org software.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n prog/%{name}-%{version}

%build
package/compile

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_libdir}/skalibs/
%{__install} -d -m0755 %{buildroot}%{_includedir}/skalibs/

for inc in $(cat package/include); do
	%{__install} -Dp -m0755 include/$inc %{buildroot}%{_includedir}/skalibs/$inc
done

for lib in $(cat package/library); do
	%{__install} -Dp -m0755 library/$lib %{buildroot}%{_libdir}/skalibs/$lib
done

%clean
%{__rm} -rf %{buildroot}

%files devel
%defattr(-, root, root, 0755)
%doc package/CHANGES package/README package/THANKS doc/*.html
%{_includedir}/skalibs/
%{_libdir}/skalibs/

%changelog
* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Initial package. (using DAR)
