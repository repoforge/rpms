# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Moose

Summary: Perl module that implements a complete modern object system
Name: perl-Moose
Version: 0.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Moose/

Source: http://www.cpan.org/authors/id/S/ST/STEVAN/Moose-0.20.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Moose is a Perl module that implements a complete modern object system.

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
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Moose/
%{perl_vendorlib}/Moose.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
