# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Mechanize

Summary: Perl module implements a testing-specific WWW::Mechanize subclass
Name: perl-Test-WWW-Mechanize
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Mechanize/

Source: http://www.cpan.org/modules/by-module/Test/Test-WWW-Mechanize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Test-WWW-Mechanize is a Perl module implements
a testing-specific WWW::Mechanize subclass.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::WWW::Mechanize.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
%{perl_vendorlib}/Test/WWW/Mechanize.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
