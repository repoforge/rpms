# $Id$
# Authority: dag

Summary: User-space file system to navigate, extract, create and modify ZIP archives
Name: fuse-zip
Version: 0.2.12
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Libraries
URL: http://code.google.com/p/fuse-zip/

Source: http://fuse-zip.googlecode.com/files/fuse-zip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel
BuildRequires: libzip-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
Requires: fuse

%description
fuse-zip is a FUSE file system to navigate, extract, create and modify
ZIP archives based in libzip implemented in C++.

With fuse-zip you really can work with ZIP archives as real directories.
Unlike KIO or Gnome VFS, it can be used in any application without
modifications.

Unlike other FUSE filesystems, only fuse-zip provides write support
to ZIP archives. Also, fuse-zip is faster that all known implementations
on large archives with many files.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALLPREFIX="%{buildroot}%{_prefix}"

%{__rm} -rf %{buildroot}%{_docdir}/fuse-zip/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog LICENSE README
%doc %{_mandir}/man1/fuse-zip.1*
%{_bindir}/fuse-zip

%changelog
* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 0.2.12-1
- Updated to release 0.2.12-1

* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 0.2.9-1
- Initial package. (using DAR)
