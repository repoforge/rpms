# $Id$

# Authority: dries

# NeedsCleanup

%define _name		ffcall
%define _version	1.8d
%define	_release	4.dries

Summary: foreign function call libraries
Summary(nl): foreign function call libraries
Name:		%{_name}
License:	GPL
Version:	%{_version}
Release:	%{_release}
URL: ftp://ftp.gnustep.org/
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Source0: ftp://ftp.gnustep.org/pub/gnustep/libs/ffcall-1.8d.tar.gz
BuildRequires: gcc diffutils make 


%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.
* avcall - calling C functions with variable arguments
* vacall - C functions accepting variable argument prototypes
* trampoline - closures as first-class C functions
* callback - closures with variable arguments as first-class C functions
             (a reentrant combination of vacall and trampoline)


%description -l nl
Dit is een verzameling van vier libraries die gebruikt kunnen worden in
embedded interpreters voor 'foreign function call interfaces'.
* avcall - calling C functions with variable arguments
* vacall - C functions accepting variable argument prototypes
* trampoline - closures as first-class C functions
* callback - closures with variable arguments as first-class C functions
             (a reentrant combination of vacall and trampoline)



%prep
rm -rf $RPM_BUILD_ROOT
%setup

%build
%configure
make 

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/man
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/ffcall-1.8d

%makeinstall

# todo
# rpmbuild removes the doc directory, so this mv has no effect..
mv -v $RPM_BUILD_ROOT/usr/share/html $RPM_BUILD_ROOT/usr/share/doc/ffcall-1.8d

%clean
rm -rf $RPM_BUILD_ROOT


%package devel
Summary: ffcall devel
Group: Development/Libraries
Requires: ffcall = %{version}-%{release}

%description devel
Development headers of ffcall: foreign function call libraries

%description -l nl devel
Development headers van ffcall: foreign function call libraries


%files
%defattr(-,root,root,0755)
%doc avcall/avcall.html
%doc callback/callback.html
%doc callback/trampoline_r/trampoline_r.html
%doc trampoline/trampoline.html
%doc vacall/vacall.html
%doc ChangeLog COPYING README NEWS
/usr/lib/libavcall.a
/usr/lib/libavcall.la
/usr/lib/libcallback.a
/usr/lib/libcallback.la
/usr/lib/libtrampoline.a
/usr/lib/libvacall.a
/usr/share/man/man3/avcall.3.gz
/usr/share/man/man3/callback.3.gz
/usr/share/man/man3/trampoline.3.gz
/usr/share/man/man3/trampoline_r.3.gz
/usr/share/man/man3/vacall.3.gz

%files devel
/usr/include/avcall.h
/usr/include/callback.h
/usr/include/trampoline.h
/usr/include/trampoline_r.h
/usr/include/vacall.h
/usr/include/vacall_r.h

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
