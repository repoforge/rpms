# $Id$
# Authority: dries
# Upstream: Sean Dowd <pop3client$dowds,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-POP3Client

Summary: Talk to a POP3 (RFC1939) server
Name: perl-Mail-POP3Client
Version: 2.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-POP3Client/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-POP3Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

Obsoletes: perl-POP3Client <= %{version}-%{release}
Provides: perl-POP3Client = %{version}-%{release}
Obsoletes: perl(POP3Client) < %{version}
Provides: perl(POP3Client) = %{version}

%description
This is a POP3 client module for perl5.  It provides an
object-oriented interface to a POP3 server.  It can be used to write
perl-based biff clients, mail readers, or whatever.

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
%doc Changes FAQ MANIFEST META.yml README
%doc %{_mandir}/man3/Mail::POP3Client.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/POP3Client.pm

%changelog
* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Mon Oct 15 2007 Dag Wieers <dag@wieers.com> - 2.17-2
- Added Provides and Obsoletes for perl-POP3Client.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Initial package.
