# $Id$
# Authority: dries

%define real_version	1.8d

Summary: foreign function call libraries
Name: ffcall
Version: 1.8
Release: 4.d
License: GPL
Group: Development/Libraries
URL: ftp://ftp.gnustep.org/

Source: ftp://ftp.gnustep.org/pub/gnustep/libs/ffcall-1.8d.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.
* avcall - calling C functions with variable arguments
* vacall - C functions accepting variable argument prototypes
* trampoline - closures as first-class C functions
* callback - closures with variable arguments as first-class C functions
             (a reentrant combination of vacall and trampoline)

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: ffcall = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n ffcall-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}
%{__install} -d -m0755 %{buildroot}%{_docdir}/ffcal-%{real_version}
%makeinstall

# todo
# rpmbuild removes the doc directory, so this mv has no effect..
mv -v $RPM_BUILD_ROOT/usr/share/html $RPM_BUILD_ROOT/usr/share/doc/ffcall-1.8d

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,0755)
%doc avcall/avcall.html
%doc callback/callback.html
%doc callback/trampoline_r/trampoline_r.html
%doc trampoline/trampoline.html
%doc vacall/vacall.html
%doc ChangeLog COPYING README NEWS
%{_libdir}/*.so.*
%{_datadir}/man/man3/avcall.3.gz
%{_datadir}/man/man3/callback.3.gz
%{_datadir}/man/man3/trampoline.3.gz
%{_datadir}/man/man3/trampoline_r.3.gz
%{_datadir}/man/man3/vacall.3.gz

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-4.dries
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-3.dries
- further spec file cleanup

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-2.dries
- added the html files
- cleanup
- fix the 'Requires:'

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-1.dries
- first packaging for Fedora Core 1
