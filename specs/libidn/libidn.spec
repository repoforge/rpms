# $Id: _template.spec 130 2004-03-17 10:51:35Z dude $

# Authority: dag
# Upstream: <bug-libidn@gnu.org>

Summary: Internationalized string processing library
Name: libidn
Version: 0.3.6
Release: 2
License: LGPL
Group: System Environment/Libraries
URL: http://josefsson.org/libidn/releases/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://josefsson.org/libidn/releases/libidn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: texinfo
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__make} -C examples distclean

### Clean up docs
%{__find} doc/ -name "Makefile*" | xargs rm -f

%post
/sbin/install-info %{_infodir}/libidn*.info.gz %{_infodir}/dir
/sbin/ldconfig 2>/dev/null

%preun
/sbin/install-info --delete %{_infodir}/libidn*.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ INSTALL NEWS README* THANKS TODO doc/libidn.html contrib
%doc %{_mandir}/man1/*
%doc %{_infodir}/libidn.info*
%{_bindir}/*
%{_datadir}/emacs/site-lisp/*.el
%{_libdir}/*.so.*
%exclude %{_datadir}/info/dir

%files devel
%defattr(-, root, root, 0755)
%doc examples/ doc/specifications/ TODO doc/*.pdf libc/example.c doc/reference
%doc %{_mandir}/man3/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.3.6-2
- Cosmetic rebuild for Group-tag.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Initial package. (using DAR)
