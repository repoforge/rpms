# Authority: dag
# Distcc: 0

%define rversion 1.5-rc6

Summary: JavaScript interpreter.
Name: js
Version: 1.5
Release: 0.rc6
License: MPL
Group: Development/Languages
URL: http://www.mozilla.org/js/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.mozilla.org/pub/mozilla.org/js/js-%{rversion}.tar.gz
Patch0: js-make.patch
Patch1: js-shlib.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
JavaScript is the Netscape-developed object scripting languages.
This package has been created for purposes of Sablotron and is suitable
for embedding in applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
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

%build
BUILD_OPT="1" %{__make} -C src -f Makefile.ref \
	XCFLAGS="%{optflags} -fPIC" \
	BUILD_OPT="1"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}/js/
%{__install} -m0755 src/Linux_All_OPT.OBJ/js %{buildroot}%{_bindir}
%{__install} -m0755 src/Linux_All_OPT.OBJ/jscpucfg %{buildroot}%{_bindir}
%{__install} -m0755 src/Linux_All_OPT.OBJ/libjs.so %{buildroot}%{_libdir}/libjs.so.1
%{__ln_s} -nf libjs.so.1 %{buildroot}%{_libdir}/libjs.so
%{__install} -m0755 src/Linux_All_OPT.OBJ/libjs.a %{buildroot}%{_libdir}
%{__install} -m0644 src/*.h %{buildroot}%{_includedir}/js/
%{__install} -m0644 src/Linux_All_OPT.OBJ/jsautocfg.h %{buildroot}%{_includedir}/js/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc src/README.html README
%{_bindir}/js
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/jscpucfg
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/js/

%changelog
* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 1.5-0.rc6
- Initial package. (using DAR)
