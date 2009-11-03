# $Id$
# Authority: dag

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%{?dtag: %{expand: %%define %dtag 1}}
%{?el5:%define _with_nspr 1}
%{?el4:%define _with_seamonkey_nspr 1}
%{?el3:%define _with_seamonkey_nspr 1}
%{?rh9:%define _with_mozilla_nspr 1}
%{?rh7:%define _with_mozilla_nspr 1}
%{?el2:%define _with_seamonkey_nspr 1}

Summary: JavaScript interpreter
Name: js
Version: 1.60
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://www.mozilla.org/js/
Source: http://ftp.mozilla.org/pub/mozilla.org/js/js-%{version}.tar.gz
Patch0: js-make.patch
Patch1: js-shlib.patch
Patch2: js-1.5-va_copy.patch
Patch3: js-ldflags.patch
Patch4: js-1.5-threadsafe.patch
Patch5: js-1.60-ncurses.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.1, readline-devel, ncurses-devel
Buildrequires: pkgconfig
%{?_with_nspr:BuildRequires: nspr-devel}
%{?_with_seamonkey_nspr:BuildRequires: seamonkey-nspr}
%{?_with_mozilla_nspr:BuildRequires: mozilla-nspr}
Provides: libjs = %{version}-%{release}

%description
JavaScript is the Netscape-developed object scripting languages.
This package has been created for purposes of Sablotron and is suitable
for embedding in applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libjs-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
%patch0 -p0 -b .make
%patch1 -p0 -b .shlib
%patch2 -p1 -b .vacopy
%patch3 -p0 -b .ldflags
%patch4 -p1 -b .threadsafe
%patch5 -p1 -b .ncurses

%{__cat} <<'EOF' >libjs.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libjs
Description: JS library
Requires:
Version: %{version}
Libs: -L${libdir} -ljs
Cflags: -I${includedir}
EOF

%build
export BUILD_OPT="1"
%{__make} -C src -f Makefile.ref \
	JS_THREADSAFE="1" \
	XCFLAGS="%{optflags} -fPIC" \
	BUILD_OPT="1"
	JS_READLINE="1" \
	JS_PERLCONNECT="1"

cd src/perlconnect
MAKEFLAGS="-s" %{__perl} Makefile.PL INSTALLDIRS="vendor"
cd -
%{__make} %{?_smp_mflags} -C src/perlconnect OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/js %{buildroot}%{_bindir}/js
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/jscpucfg %{buildroot}%{_bindir}/jscpucfg
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/libjs.a %{buildroot}%{_libdir}/libjs.a
%{__install} -Dp -m0755 src/Linux_All_OPT.OBJ/libjs.so %{buildroot}%{_libdir}/libjs.so.1
%{__ln_s} -nf libjs.so.1 %{buildroot}%{_libdir}/libjs.so

%{__install} -d -m0755 %{buildroot}%{_includedir}/js/
%{__install} -p -m0644 src/js*.h %{buildroot}%{_includedir}/
%{__install} -p -m0644 src/Linux_All_OPT.OBJ/jsautocfg.h %{buildroot}%{_includedir}/

%{__install} -Dp -m0644 libjs.pc %{buildroot}%{_libdir}/pkgconfig/libjs.pc

%{__make} -C src/perlconnect pure_install PERL_INSTALL_ROOT="%{buildroot}"

### Remove unwanted perl related files
find %{buildroot} -type f -name .packlist -o -name jsperlbuild.pl | xargs -r rm
find %{buildroot} -type f -name '*.bs' -a -size 0 | xargs -r rm
### For some reason, the pure_install above doesn't set u+w :-(
find %{buildroot}%{perl_vendorarch} -type f -exec %{__chmod} u+w {} \;

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc src/README*.html src/perlconnect/bg.jpg
%{_bindir}/js
%{_libdir}/libjs.so.*
%{perl_vendorarch}/auto/JS/
%{perl_vendorarch}/*.pm

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/jscpucfg
%{_libdir}/libjs.so
%{_libdir}/libjs.a
%{_libdir}/pkgconfig/libjs.pc
%{_includedir}/js*.h

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.60-1
- Updated to release 1.60.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to final release of 1.5.

* Sat Mar 26 2005 Dag Wieers <dag@wieers.com> - 1.5-0.rc6a
- Added x86_64 VA_COPY patch. (Stef Van Dessel)

* Tue Jun 15 2004 Matthias Saou <http://freshrpms.net> 1.5-0.rc6a
- Update to 1.5rc6a.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 1.5-0.rc6
- Initial package. (using DAR)

