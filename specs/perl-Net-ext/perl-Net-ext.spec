# $Id$
# Authority: dries
# Upstream: Spider Boardman <spidb$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-ext

Summary: Generic sockets interface handling
Name: perl-Net-ext
Version: 1.011
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-ext/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPIDB/Net-ext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Modules Net::Gen, Net::Inet, Net::TCP, Net::UDP, Net::UNIX,
Net::TCP::Server, and Net::UNIX::Server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.011-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.011-1
- Initial package.
