# $Id$
# Authority: dries
# Upstream: Sean Dowd <pop3client$dowds,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-POP3Client

Summary: Talk to a POP3 (RFC1939) server
Name: perl-Mail-POP3Client
Version: 2.17
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-POP3Client/

Source: http://search.cpan.org/CPAN/authors/id/S/SD/SDOWD/Mail-POP3Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Mail::POP3Client.3pm*
%{perl_vendorlib}/Mail/POP3Client.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.17-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Initial package.
