# $Id$
# Authority: dag
# Upstream: <sablist@gingerall.cz>

%define real_name Sablot

Summary: XSLT, XPath and DOM processor
Name: sablotron
Version: 1.0.1
Release: 1
License: GPL
Group: Utilities/Text
URL: http://www.gingerall.com/charlie/ga/xml/p_sab.xml

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download-1.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
Patch: sablot-lib-1.0.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: expat-devel >= 1.95.2, ncurses-devel, libstdc++-devel
BuildRequires: js-devel >= 1.5, readline-devel
#Requires: expat >= 1.95.2, ncurses, libstdc++
#Requires: js >= 1.5, readline
Conflicts: expat = 1.95.6

%description
Sablotron is an XML (XSLT 1.0, XPath 1.0, DOM Level2) processor. 
It is written in C++ by Ginger Alliance.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}
%patch

%build
export CPLUS_INCLUDE_PATH="%{_includedir}/js"
export CXXFLAGS="%{optflags}"
export SABLOT_GPL="1"
%configure \
	--enable-javascript \
	--with-readline \
	--enable-debugger
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README RELEASE doc/misc/DEBUGGER doc/misc/NOTES
%doc %{_mandir}/man?/*
%{_bindir}/sabcmd
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,0755)
%doc doc/apidoc/jsdom-ref doc/apidoc/sablot doc/apidoc/sxp
%{_bindir}/sablot-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
