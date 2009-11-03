# $Id: js.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag

Summary: JavaScript interpreter
Name: js
Version: 1.5
Release: 1.2%{?dist}
License: MPL
Group: Development/Languages
URL: http://www.mozilla.org/js/
Source: http://ftp.mozilla.org/pub/mozilla.org/js/js-%{version}.tar.gz
Patch0: js-make.patch
Patch1: js-shlib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
JavaScript is the Netscape-developed object scripting languages.
This package has been created for purposes of Sablotron and is suitable
for embedding in applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
%patch0 -b .make
%patch1 -b .shlib

%{__perl} -pi.orig -e 's|\bVA_COPY\(|va_copy\(|g' src/jsprf.c

%build
BUILD_OPT="1" %{__make} -C src -f Makefile.ref \
    XCFLAGS="%{optflags} -fPIC" \
    BUILD_OPT="1"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/js %{buildroot}%{_bindir}/js
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/jscpucfg %{buildroot}%{_bindir}/jscpucfg
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/libjs.a %{buildroot}%{_libdir}/libjs.a
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/libjs.so %{buildroot}%{_libdir}/libjs.so.1
%{__ln_s} -nf libjs.so.1 %{buildroot}%{_libdir}/libjs.so

%{__install} -d -m0755 %{buildroot}%{_includedir}/js/
%{__install} -p -m0644 src/*.h %{buildroot}%{_includedir}/js/
%{__install} -p -m0644 src/Linux_All_OPT.OBJ/jsautocfg.h %{buildroot}%{_includedir}/js/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc src/README.html
%{_bindir}/js
%{_libdir}/libjs.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/jscpucfg
%{_libdir}/libjs.so
%{_libdir}/libjs.a
%{_includedir}/js/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1.
- Updated to final release of 1.5.

* Sat Mar 26 2005 Dag Wieers <dag@wieers.com> - 1.5-0.rc6a
- Added x86_64 VA_COPY patch. (Stef Van Dessel)

* Tue Jun 15 2004 Matthias Saou <http://freshrpms.net> 1.5-0.rc6a
- Update to 1.5rc6a.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 1.5-0.rc6
- Initial package. (using DAR)

