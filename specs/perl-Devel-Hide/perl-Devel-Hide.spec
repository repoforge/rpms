# $Id$
# Authority: cmr
# Upstream: A, R, Ferreira <ferreira$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Hide

Summary: Forces the unavailability of specified Perl modules (for testing)
Name: perl-Devel-Hide
Version: 0.0008
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Hide/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Hide-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(Test::More)
# From yaml recommends
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)


%description
Forces the unavailability of specified Perl modules (for testing).

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
%doc %{_mandir}/man3/Devel::Hide.3pm*
%dir %{perl_vendorlib}/Devel/
#%{perl_vendorlib}/Devel/Hide/
%{perl_vendorlib}/Devel/Hide.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.0008-1
- Initial package. (using DAR)
