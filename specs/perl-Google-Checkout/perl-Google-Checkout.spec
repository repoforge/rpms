# $Id$
# Authority: dries
# Upstream: David Shao Lin Zhuo <dzhuo$google,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Google-Checkout

Summary: Interface to Google Checkout
Name: perl-Google-Checkout
Version: 1.0.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Google-Checkout/

Source: http://search.cpan.org//CPAN/authors/id/D/DZ/DZHUO/Google-Checkout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Interface to Google Checkout.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Google::Checkout::*
%{perl_vendorlib}/Google/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Initial package.
