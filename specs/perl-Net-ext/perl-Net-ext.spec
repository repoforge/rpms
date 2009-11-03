# $Id$
# Authority: dries
# Upstream: Spider Boardman <spidb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-ext

Summary: Generic sockets interface handling
Name: perl-Net-ext
Version: 1.011
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-ext/

Source: http://www.cpan.org/modules/by-module/Net/Net-ext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Modules Net::Gen, Net::Inet, Net::TCP, Net::UDP, Net::UNIX,
Net::TCP::Server, and Net::UNIX::Server.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Net/
%{perl_vendorarch}/auto/Net/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.011-1
- Initial package.
