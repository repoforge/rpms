# $Id$
# Authority: dag
# Upstream: Ask Solem <ASKSH$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Snowball-Norwegian

Summary: Porters stemming algorithm for norwegian
Name: perl-Snowball-Norwegian
Version: 1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Snowball-Norwegian/

Source: http://www.cpan.org/authors/id/A/AS/ASKSH/Snowball-Norwegian-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.42

%description
Porters stemming algorithm for norwegian.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Lingua::Stem::Snowball::No.3pm*
%{_bindir}/stemmer-no.pl
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Stem/
%dir %{perl_vendorlib}/Lingua/Stem/Snowball/
%{perl_vendorlib}/Lingua/Stem/Snowball/No.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
