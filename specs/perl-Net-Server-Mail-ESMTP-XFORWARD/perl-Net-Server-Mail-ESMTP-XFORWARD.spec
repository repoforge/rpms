# $Id$
# Authority: dries
# Upstream: Xavier Guimard <perl$astola,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Server-Mail-ESMTP-XFORWARD

Summary: Adds support for XFORWARD to Net::Server::Mail::ESMTP
Name: perl-Net-Server-Mail-ESMTP-XFORWARD
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server-Mail-ESMTP-XFORWARD/

Source: http://search.cpan.org//CPAN/authors/id/G/GU/GUIMARD/Net-Server-Mail-ESMTP-XFORWARD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module adds support for XFORWARD to Net::Server::Mail::ESMTP.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Server/Mail/ESMTP/XFORWARD.pm
%dir %{perl_vendorlib}/Net/Server/Mail/ESMTP/
%dir %{perl_vendorlib}/Net/Server/Mail/
%dir %{perl_vendorlib}/Net/Server/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
