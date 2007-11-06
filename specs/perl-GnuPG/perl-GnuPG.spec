# $Id$
# Authority: dries
# Upstream: Francis J. Lacoste <frajulac$contre,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GnuPG

Summary: Interface to the GNU Privacy Guard
Name: perl-GnuPG
Version: 0.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GnuPG/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRAJULAC/GnuPG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

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
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
