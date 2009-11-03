# $Id$
# Authority: dries
# Upstream: Jan Behrens <jan,behrens$flexidesk,de>

Summary: Library for processing UTF-8 encoded unicode strings
Name: utf8proc
Version: 1.1.4
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.flexiguided.de/publications.utf8proc.en.html

Source: http://www.public-software-group.org/pub/projects/utf8proc/v%{version}/utf8proc-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
utf8proc is a library for processing UTF-8 encoded Unicode strings. Some 
features are Unicode normalization, stripping of default ignorable 
characters, case folding and detection of grapheme cluster boundaries.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n utf8proc-v%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir} %{buildroot}%{_includedir}
%{__install} libutf8proc.so %{buildroot}%{_libdir}/libutf8proc.so
%{__install} utf8proc.h %{buildroot}%{_includedir}/utf8proc.h

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog lump.txt LICENSE README
%{_libdir}/libutf8proc.so

%files devel
%{_includedir}/utf8proc.h

%changelog
* Sat Aug 29 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.4-1
- Updated to release 1.1.4.

* Sun Jul 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Initial package.
