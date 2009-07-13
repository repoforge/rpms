# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IMAP-Simple

Summary: Perl extension for simple IMAP account handling
Name: perl-Net-IMAP-Simple
Version: 1.1900
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IMAP-Simple/

Source: http://www.cpan.org/modules/by-module/Net/Net-IMAP-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is a simple way to access IMAP accounts.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/IMAP/Simple.pm
%{perl_vendorlib}/Net/IMAP/Simple.pod

%changelog
* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 1.1900-1
- Updated to version 1.1900.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.1801-1
- Updated to version 1.1801.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.101-1
- Updated to release 0.101.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Initial package.
