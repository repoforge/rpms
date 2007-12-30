# $Id$
# Authority: dag
# Upstream: Brandon L. Black, <blblack@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MRO-Compat

Summary: mro::* interface compatibility for Perls < 5.9.5
Name: perl-MRO-Compat
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MRO-Compat/

Source: http://www.cpan.org/authors/id/B/BL/BLBLACK/MRO-Compat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::C3)
BuildRequires: perl(Class::C3::XS)
BuildRequires: perl(Test::More) >= 0.47

%description
mro::* interface compatibility for Perls < 5.9.5.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/MRO::Compat.3pm*
%dir %{perl_vendorlib}/MRO/
#%{perl_vendorlib}/MRO/Compat/
%{perl_vendorlib}/MRO/Compat.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
