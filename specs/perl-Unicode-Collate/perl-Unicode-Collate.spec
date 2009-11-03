# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Collate

Summary: Perl module that implements Unicode Collation Algorithm
Name: perl-Unicode-Collate
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Collate/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Collate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-Collate is a Perl module that implements Unicode Collation
Algorithm.

This package contains the following Perl module:

    Unicode::Collate

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
%doc Changes MANIFEST MANIFEST.X META.yml README
%doc %{_mandir}/man3/Unicode::Collate.3pm*
%dir %{perl_vendorlib}/Unicode/
%{perl_vendorlib}/Unicode/Collate/
%{perl_vendorlib}/Unicode/Collate.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.52-1
- Initial package. (using DAR)
