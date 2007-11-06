# $Id$
# Authority: dries
# Upstream: David J. Kernen <DJKERNEN__NO_SOLICITING__$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-IMAPClient

Summary: IMAP Client API
Name: perl-Mail-IMAPClient
Version: 2.2.9
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-IMAPClient/

Source: http://search.cpan.org/CPAN/authors/id/D/DJ/DJKERNEN/Mail-IMAPClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Mail::IMAPClient*
%{perl_vendorlib}/Mail/IMAPClient.p*
%{perl_vendorlib}/Mail/IMAPClient/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1.2
- Rebuild for Fedora Core 5.

* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1
- Initial package.
