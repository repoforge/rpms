# $Id$
# Authority: dries
# Upstream: Mark Frost <mfrost@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GnuPG

Summary: Interface to the GNU Privacy Guard
Name: perl-GnuPG
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GnuPG/

Source: http://search.cpan.org/CPAN/authors/id/M/MF/MFROST/GnuPG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gnupg
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
GnuPG is a perl module that interface with the Gnu Privacy Guard using
the coprocess hooks provided by gpg. The communication mechanism uses
is shared memory and a status file descriptor.

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
%doc ChangeLog README
%doc %{_mandir}/man?/*
%{_bindir}/gpgmailtunl
%{perl_vendorlib}/GnuPG.pm
%{perl_vendorlib}/GnuPG

%changelog
* Tue Apr 05 2011 Denis Fateyev <denis@fateyev.com> - 0.17-1
- Updated to version 0.17.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
