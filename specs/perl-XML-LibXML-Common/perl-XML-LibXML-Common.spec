# $Id$

# Authority: dag

%define rname XML-LibXML-Common

Summary: XML-LibXML-Common Perl module.
Name: perl-XML-LibXML-Common
Version: 0.13
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML-Common/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
XML-LibXML-Common Perl module.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.13-1
- Fixed site -> vendor. (Matthew Mastracci)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.13-0
- Updated to release 0.13.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR) 
