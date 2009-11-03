# $Id$
# Authority: dag
# Upstream: <bug-libidn$gnu,org>

### RHEL4 and newer ship with libidn
# ExclusiveDist: el2 rh7 rh9 el3

Summary: Internationalized string processing library
Name: libidn
Version: 0.5.6
Release: 0.1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://josefsson.org/libidn/releases/

Source: ftp://alpha.gnu.org/pub/gnu/libidn/libidn-%{version}.tar.gz
#Source: http://josefsson.org/libidn/releases/libidn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: texinfo, gcc-c++
Prereq: info

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__make} -C examples distclean

### Clean up docs
%{__find} doc/ -name "Makefile*" | xargs rm -f

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/info/dir

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/libidn*.info.gz %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/libidn*.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog contrib COPYING* doc/libidn.html FAQ INSTALL NEWS README* THANKS TODO
%doc %{_mandir}/man1/idn.1*
%{_bindir}/idn
%{_datadir}/emacs/site-lisp/idna.el
%{_datadir}/emacs/site-lisp/punycode.el
%{_libdir}/libidn.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.pdf doc/reference doc/specifications/ examples/ libc/example.c TODO
%doc %{_mandir}/man3/*.3*
%doc %{_infodir}/*.info*
#%{_libdir}/libidn.a
%{_includedir}/*.h
%{_libdir}/libidn.so
%{_libdir}/pkgconfig/libidn.pc
%exclude %{_libdir}/libidn.la

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.5.6-0.1
- Updated to release 0.5.6.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Updated to release 0.4.6.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Thu May 20 2004 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.3.6-2
- Cosmetic rebuild for Group-tag.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Initial package. (using DAR)
