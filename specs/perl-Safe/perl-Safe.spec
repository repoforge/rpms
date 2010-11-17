# $Id$
# Authority: dag

# Tag: rft

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Safe

Summary: Compile and execute code in restricted compartments
Name: perl-Safe
Version: 2.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Safe/

#Source: http://www.cpan.org/modules/by-module/Safe/Safe-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Safe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Compile and execute code in restricted compartments.

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
%doc %{_mandir}/man3/Safe.3pm*
#%{perl_vendorlib}/Safe/
%{perl_vendorarch}/Safe.pm

%changelog
* Sun Aug 22 2010 Dag Wieers <dag@wieers.com> - 2.27-1
- Initial package. (using DAR)
