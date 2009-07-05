# $Id$
# Authority: dag
# Upstream: Ingy döt Net <INGY$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline

Summary: Perl module to write Perl subroutines in other programming languages
Name: perl-Inline
Version: 0.45
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline/

Source: http://www.cpan.org/modules/by-module/Inline/Inline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Inline is a Perl module to write Perl subroutines
in other programming languages.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Inline-API.pod
%{perl_vendorlib}/Inline-FAQ.pod
%{perl_vendorlib}/Inline-Support.pod
%{perl_vendorlib}/Inline.pm
%{perl_vendorlib}/Inline.pod
%{perl_vendorlib}/Inline/
%{perl_vendorlib}/auto/Inline/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.45-1
- Updated to version 0.45.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.44-1
- Initial package. (using DAR)
