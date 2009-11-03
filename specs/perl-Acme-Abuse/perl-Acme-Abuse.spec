# $Id$
# Authority: dag
# Upstream: Ben Morrow <ben$morrow,me,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Abuse

Summary: Perl module for setid modules
Name: perl-Acme-Abuse
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Abuse/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Abuse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-Abuse is a Perl module for setid modules.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Acme::Abuse.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/Abuse.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
