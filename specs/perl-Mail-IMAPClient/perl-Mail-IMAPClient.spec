# $Id$
# Authority: dries
# Upstream: David J. Kernen <DJKERNEN__NO_SOLICITING__$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-IMAPClient

Summary: IMAP Client API
Name: perl-Mail-IMAPClient
Version: 2.2.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-IMAPClient/

Source: http://search.cpan.org/CPAN/authors/id/D/DJ/DJKERNEN/Mail-IMAPClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides perl routines that simplify a sockets connection 
to and an IMAP conversation with an IMAP server.

%prep
%setup -n %{real_name}-%{version}

%build
echo n | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Mail/IMAPClient.p*
%{perl_vendorlib}/Mail/IMAPClient/*

%changelog
* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1
- Initial package.
