# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-IMAPClient

Summary: IMAP4 client library
Name: perl-Mail-IMAPClient
Version: 3.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-IMAPClient/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-IMAPClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT Changes INSTALL MANIFEST META.yml README Todo test_template.txt examples/
%doc %{_mandir}/man3/Mail::IMAPClient.3pm*
%doc %{_mandir}/man3/Mail::IMAPClient::*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/IMAPClient/
%{perl_vendorlib}/Mail/IMAPClient.pm
%{perl_vendorlib}/Mail/IMAPClient.pod

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 3.07-1
- Updated to release 3.07.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 3.05-1
- Updated to release 3.05.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1
- Initial package.
