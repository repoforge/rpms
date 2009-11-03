# $Id$
# Authority: dag
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Statgrab

Summary: Perl module for collecting information about the machine
Name: perl-Unix-Statgrab
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Statgrab/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Statgrab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libstatgrab-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Unix-Statgrab is a Perl module for collecting information
about the machine.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/Unix::Statgrab.3pm*
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Statgrab.pm
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Statgrab/

%changelog
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
