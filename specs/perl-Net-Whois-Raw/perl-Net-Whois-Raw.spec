# $Id$
# Authority: dries
# Upstream: Walery Studennikov <despairr$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-Raw

Summary: Get Whois information for domains
Name: perl-Net-Whois-Raw
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-Raw/

Source: http://www.cpan.org/modules/by-module/Net/Net-Whois-Raw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Get Whois information for domains.

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
%doc Changes README
%doc %{_mandir}/man3/Net::Whois::Raw*
%doc %{_mandir}/man1/pwhois*
%{_bindir}/pwhois
%{perl_vendorlib}/Net/Whois/Raw.pm
%{perl_vendorlib}/Net/Whois/Raw/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
