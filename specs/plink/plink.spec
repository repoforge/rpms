# $Id$
# Authority: shuff
# Upstream: Shaun Purcell <plink$chgr,mgh,harvard,edu>
# ExcludeDist: el3 el4

Summary: Whole genome data analysis toolset
Name: plink
Version: 1.07
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://pngu.mgh.harvard.edu/~purcell/plink/

Source: http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-%{version}-src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++ >= 4.1
BuildRequires: gcc-gfortran >= 4.1
BuildRequires: lapack-devel >= 3
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge

%description
PLINK is a free, open-source whole genome association analysis toolset,
designed to perform a range of basic, large-scale analyses in a computationally
efficient manner.

The focus of PLINK is purely on analysis of genotype/phenotype data, so there
is no support for steps prior to this (e.g. study design and planning,
generating genotype or CNV calls from raw data). Through integration with
gPLINK and Haploview, there is some support for the subsequent visualization,
annotation and storage of results. 

%package -n gplink
Summary: Java GUI for PLINK
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
Requires: jre >= 1.5

%description -n gplink
gPLINK is a freely-available, Java-based software package that:

* is a GUI that allows construction of many common PLINK operations
* provides a simple project management tool and analysis log
* allows for data and computation to be on a separate server (via SSH)
* facilitates integration with Haploview 

%prep
%setup -n %{name}-%{version}-src

%build
# set build options
perl -pi -e 's|^WITH_WEBCHECK = 1*$|WITH_WEBCHECK = |;' Makefile
perl -pi -e 's|^WITH_ZLIB = *$|WITH_ZLIB = 1|;' Makefile
perl -pi -e 's|^WITH_LAPACK = *$|WITH_LAPACK = 1|;' Makefile
perl -pi -e 's|^FORCE_DYNAMIC = *$|FORCE_DYNAMIC = 1|;' Makefile
perl -pi -e 's|^LIB_LAPACK = /usr/lib/liblapack.so.3$|LIB_LAPACK = %{_libdir}/liblapack.so.3|;' Makefile
%{__make} %{?_smp_mflags}

# make a gplink install script
%{__cat} <<GPLINK > gplink
#!/bin/sh
%{_bindir}/java -jar %{_datadir}/gplink/gPLINK.jar >/dev/null 2>&1 &
GPLINK

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 plink %{buildroot}%{_bindir}
%{__install} -m0755 gplink %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/gplink
%{__install} -m0644 gPLINK.jar %{buildroot}%{_datadir}/gplink

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.txt README.txt
%{_bindir}/plink

%files -n gplink
%{_bindir}/gplink
%{_datadir}/gplink

%changelog
* Tue Oct 26 2010 Steve Huff <shuff@vecna.org> - 1.07-1
- Initial package.
