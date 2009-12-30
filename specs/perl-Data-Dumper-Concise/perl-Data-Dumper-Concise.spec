# $Id$
# Authority: cmr
# Upstream: mst - Matt S, Trout <mst$shadowcat,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Dumper-Concise

Summary: Less indentation and newlines plus sub deparsing
Name: perl-Data-Dumper-Concise
Version: 1.100
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Dumper-Concise/

Source: http://www.cpan.org/authors/id/M/MS/MSTROUT/Data-Dumper-Concise-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
Requires: perl >= 0:5.6.0

%description
Less indentation and newlines plus sub deparsing.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Data::Dumper::Concise.3pm*
%doc %{_mandir}/man3/Data::Dumper::Concise::Sugar.3pm*
%doc %{_mandir}/man3/Devel::Dwarn.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Dumper/
%{perl_vendorlib}/Data/Dumper/Concise/Sugar.pm
%{perl_vendorlib}/Data/Dumper/Concise.pm
%{perl_vendorlib}/Devel/Dwarn.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.100-1
- Initial package. (using DAR)

