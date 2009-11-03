# $Id$
# Authority: dries
# Upstream: Jan Krynicky <Jenda$Krynicky,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Sender
%define real_version 0.008016

Summary: Module for sending mails with attachments
Name: perl-Mail-Sender
Version: 0.8.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Sender/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Sender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Mail::Sender is a module for sending mails with attachments through an SMTP
server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
echo "N" | %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_vendorlib}/Mail/Sender/CType/Win32.pm

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Mail::Sender.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/Sender/
%{perl_vendorlib}/Mail/Sender.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.8.16-1
- Updated to release 0.8.16.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.13-1
- Updated to release 0.8.13.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1
- Initial package.
