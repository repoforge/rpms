# $Id$
# Authority: dag
# Upstream: <sablist$gingerall,cz>

%define real_name Sablot

Summary: XSLT, XPath and DOM processor
Name: sablotron
Version: 1.0.3
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.gingerall.org/sablotron.html

Source: http://download-1.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: expat-devel >= 1.95.2, ncurses-devel, libstdc++-devel
BuildRequires: js-devel >= 1.5, readline-devel
# Building the documentation requires this
BuildRequires: perl(XML::Parser), intltool, gcc-c++
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

%build
export CPLUS_INCLUDE_PATH="%{_includedir}/js"
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
%doc README* RELEASE doc/misc/DEBUGGER doc/misc/NOTES src/TODO
%doc %{_mandir}/man1/sabcmd.1*
%{_bindir}/sabcmd
%{_libdir}/libsablot.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/apidoc/jsdom-ref doc/apidoc/sablot doc/apidoc/sxp
%{_bindir}/sablot-config
%{_libdir}/libsablot.a
%exclude %{_libdir}/libsablot.la
%{_libdir}/libsablot.so
%{_includedir}/*.h

%changelog
* Wed Jul 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.
- Fixed the urls.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Mar 26 2005 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
