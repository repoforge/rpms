# $Id$
# Authority: dag
# Upstream: Russell Coker <russell$coker,com,au>

%define real_version 1.03a

Summary: Benchmark suite for hard drive and file system performance
Name: bonnie++
Version: 1.03
Release: 1.a
License: GPL
Group: Applications/System
URL: http://www.coker.com.au/bonnie++/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.coker.com.au/bonnie++/bonnie++-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of
simple tests of hard drive and file system performance. Then you can
decide which test is important and decide how to compare different
systems after running it. I have no plans to ever have it produce a
single number, because I don't think that a single number can be useful
when comparing such things.

%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e '
		s|\$\(eprefix\)/sbin|\$(sbindir)|;
		s|\$\(eprefix\)/bin|\$(bindir)|;
		s|\@mandir\@|\$(mandir)|;
	' Makefile.in

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog.txt readme.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_sbindir}/*

%changelog
* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 1.03-1.a
- Initial package. (using DAR)
