# $Id$
# Authority: dries
# Upstream: Walery Studennikov <despairr$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-Raw

Summary: Get Whois information for domains
Name: perl-Net-Whois-Raw
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-Raw/

Source: http://search.cpan.org//CPAN/authors/id/D/DE/DESPAIR/Net-Whois-Raw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Get Whois information for domains.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

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
