# $Id$

# Authority: dag

%define rname XML-NamespaceSupport

Summary: XML-NamespaceSupport Perl module.
Name: perl-XML-NamespaceSupport
Version: 1.08
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-NamespaceSupport/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl

%description
XML-NamespaceSupport Perl module.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/%{_target_cpu}-linux-thread-multi/
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/*/%{_target_cpu}-linux-thread-multi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.08-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR) 
