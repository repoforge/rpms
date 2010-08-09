# $Id$
# Authority: shuff
# Upstream: Al Chu <achu$llnl,gov>

%define real_name genders
%define real_release 1

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)


Summary: Static cluster configuration database
Name: libgenders
Version: 1.14
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://computing.llnl.gov/linux/genders.html

Source: http://downloads.sourceforge.net/project/genders/genders/%{version}-%{real_release}/genders-%{version}.tar.gz
Patch0: libgenders-1.14_perlpath.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge

%description
Genders is a static cluster configuration database used for cluster
configuration management. It is used by a variety of tools and scripts for
management of large clusters. The Genders database is accessed by every node in
a cluster, either through a networked file system or by replicating the
database on every node of the cluster. The database describes the layout and
configuration of the cluster so that tools and scripts can sense the variations
of cluster nodes. By abstracting this information into a plain text file, it
becomes possible to change the configuration of a cluster by modifying only one
file.

%package compat
Summary: Compatibility API for earlier releases of %{name}
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description compat
This package provides backwards compatibility for executables built against
older versions of libgenders.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package perl
Summary: Perl API for %{name}
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl

%description perl
This package provides the Perl API for libgenders.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%configure \
    --disable-dependency-tracking \
    --enable-static=no \
    --with-perl-extensions \
    --with-perl-destdir="%{buildroot}"
%{__make} %{?_smp_mflags} INSTALLDIRS="vendor"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALLDIRS="vendor"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DISCLAIMER DISCLAIMER.UC INSTALL 
%doc META NEWS README TODO TUTORIAL genders.sample contrib/php/
%doc %{_mandir}/man?/*
%exclude %{_mandir}/man?/gendlib*
%exclude %{_mandir}/man?/Genders*
%exclude %{_mandir}/man?/Libgenders*
%{_bindir}/*
%{_libdir}/*.so.*

%files compat
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/gendlib*
%{_prefix}/lib/genders/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%files perl
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/Genders*
%doc %{_mandir}/man?/Libgenders*
%{perl_vendorarch}/*

%changelog
* Mon Aug 09 2010 Steve Huff <shuff@vecna.org> - 1.14-1
- Initial package.
