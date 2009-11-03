# $Id$
# Authority: dag
# Upstream:

%define real_version 2.6a

Summary: NIST SPeech HEader REsources (SPHERE) Package
Name: sphere
Version: 2.6
Release: 1.a.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: ftp://jaguar.ncsl.nist.gov/pub/sphere_2.6a.README

Source: ftp://jaguar.ncsl.nist.gov/pub/sphere_%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
The NIST SPeech HEader REsources (SPHERE) Package

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n nist

#%{__perl} -pi.orig -e 's|extern char *sys_errlist\[\];|extern __const char *__const _sys_errlist[];|' src/lib/sp/exit.c
%{__perl} -pi.orig -e '
		s|^(# include <sp/shorten/shorten.h>)$|$1\n# include <sys/errno.h>|;
		s|^(extern) (char) \*(sys_errlist\[\];)$|$1 __const $2 *__const $3|;
	' src/lib/sp/exit.c

%build
%{__cat} <<EOF | sh src/scripts/install.sh
10
gcc
yes
%{optflags} -fPIC
yes
%{__install} -p -m0755
yes
ranlib
yes
ar ru
yes
%{_arch}
yes
EOF
#%{__make} -C src
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -p -m0755 bin/* %{buildroot}%{_bindir}

%{__install} -Dp -m0755 lib/libsp.a %{buildroot}%{_libdir}/sp/libsp.a
%{__install} -Dp -m0755 lib/libutil.a %{buildroot}%{_libdir}/sp/libutil.a
%{__ln_s} -f sp/libsp.a %{buildroot}%{_libdir}/libsp.a

%{__install} -d -m0755 %{buildroot}%{_includedir}/sp/
#{__install} -m0644 include/sp/* %{buildroot}%{_includedir}/sp/
%{__cp} -apv include/sp/* %{buildroot}%{_includedir}/sp/

%{__install} -d -m0755 %{buildroot}%{_includedir}/util/
%{__cp} -apv include/util/* %{buildroot}%{_includedir}/util/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/man/man1/* %{buildroot}%{_mandir}/man1/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man3/
%{__install} -p -m0644 doc/man/man3/* %{buildroot}%{_mandir}/man3/

### Clean up buildroot (conflict with shorten package)
%{__rm} -f %{buildroot}%{_mandir}/man1/shorten*

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.doc
#%doc scripts/
%doc %{_mandir}/man1/*
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/sphere.*
%doc %{_mandir}/man3/*
%{_includedir}/sp/
%{_includedir}/util/
%{_libdir}/*.a
%{_libdir}/sp/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-1.a.2
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 2.6-1.a
- Fixed Group tag.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 2.6-0.a
- Initial package. (using DAR)
