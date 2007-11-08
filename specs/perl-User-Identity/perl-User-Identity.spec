# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name User-Identity

Summary: Maintains info about a physical person
Name: perl-User-Identity
Version: 0.91
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User-Identity/

Source: http://search.cpan.org//CPAN/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Maintains info about a physical person.

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
%doc Changes
%doc %{_mandir}/man3/User::Identity*
%doc %{_mandir}/man3/Mail::Identity*
%{perl_vendorlib}/User/Identity.p*
%{perl_vendorlib}/Mail/Identity.p*
%{perl_vendorlib}/User/Identity/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.91-1
- Initial package.
