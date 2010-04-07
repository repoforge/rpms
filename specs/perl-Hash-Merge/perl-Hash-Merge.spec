# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Hash-Merge

Summary: Perl module to merge arbitrarily deep hashes into a single hash
Name: perl-Hash-Merge
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Hash-Merge/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/Hash-Merge-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Hash/Hash-Merge-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Hash-Merge is a Perl module to merge arbitrarily deep hashes
into a single hash.

This package contains the following Perl module:

    Hash::Merge

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Hash::Merge.3pm*
%dir %{perl_vendorlib}/Hash/
#%{perl_vendorlib}/Hash/Merge/
%{perl_vendorlib}/Hash/Merge.pm

%changelog
* Mon Mar 22 2010 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Update version 0.11.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
