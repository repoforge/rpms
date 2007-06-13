# $Id$
# Authority: dries
# Upstream: Matthew McGillis <mmcgillis$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-QIF

Summary: Parse and create Quicken Interchange Format files
Name: perl-Finance-QIF
Version: 2.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-QIF/

Source: http://search.cpan.org//CPAN/authors/id/M/MM/MMCGILLIS/Finance-QIF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Parse and create Quicken Interchange Format files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Finance::QIF*
%{perl_vendorlib}/Finance/QIF.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Initial package.
