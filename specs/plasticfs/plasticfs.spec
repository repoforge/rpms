# $Id$
# Authority: dag

Summary: The Plastic File System
Name: plasticfs
Version: 1.9
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://plasticfs.sourceforge.net/

Source: http://dl.sf.net/plasticfs/plasticfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: groff, gcc-c++, libtool

%description
The Plastic File System is an LD_PRELOAD module for manipulating what the
file system looks like for programs.  This allows virtual file systems
to exist in user space, without kernel hacks or modules.

%prep
%setup
%configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUILDING LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/*


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9-1.2
- Rebuild for Fedora Core 5.

* Wed Jul 07 2004 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Fri Mar 14 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
