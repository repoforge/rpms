# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

# ExclusiveDist: rh6 el2 rh7 rh8 rh9 el3 fc1

Summary: Library with GPG related error codes and descriptions
Name: libgpg-error
Version: 0.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/gpgme.html

Source: ftp://ftp.gnupg.org/gcrypt/alpha/libgpg-error/libgpg-error-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libgpg-error is a small library with error codes and descriptions
shared by most GnuPG related software.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
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
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING* ChangeLog INSTALL NEWS README
%{_bindir}/gpg-error
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/gpg-error-config
%{_includedir}/*.h
%{_libdir}/*.a
### Needed by dctc ?
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
