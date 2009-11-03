# $Id$
# Authority: dag
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-ISA

Summary: Perl module to report the search path for a class's ISA tree
Name: perl-Class-ISA
Version: 0.33
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-ISA/

Source: http://www.cpan.org/modules/by-module/Class/Class-ISA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Class-ISA is a Perl module to report the search path for
a class's ISA tree.

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
%doc %{_mandir}/man3/Class::ISA.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/ISA.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Initial package. (using DAR)
