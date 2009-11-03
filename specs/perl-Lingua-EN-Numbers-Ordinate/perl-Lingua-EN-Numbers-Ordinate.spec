# $Id$
# Authority: dag
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Numbers-Ordinate

Summary: Perl module to go from cardinal number (3) to ordinal ("3rd")
Name: perl-Lingua-EN-Numbers-Ordinate
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Numbers-Ordinate/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-Numbers-Ordinate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Lingua-EN-Numbers-Ordinate is a Perl module to go from cardinal
number (3) to ordinal ("3rd").

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Lingua::EN::Numbers::Ordinate.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/EN/
%dir %{perl_vendorlib}/Lingua/EN/Numbers/
%{perl_vendorlib}/Lingua/EN/Numbers/Ordinate.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
