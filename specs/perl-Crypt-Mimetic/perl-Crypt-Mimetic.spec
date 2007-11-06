# $Id$
# Authority: dries
# Upstream: Erich Roncarolo <erich-roncarolo$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Mimetic

Summary: Crypt a file and mask it behind another file
Name: perl-Crypt-Mimetic
Version: 0.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Mimetic/

Source: http://search.cpan.org/CPAN/authors/id/E/ER/ERICH/Crypt-Mimetic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module allows you to hide a file by encrypting it and then attaching
it to another file of your choice.  This mimetic file then looks and
behaves like a normal file, and can be stored, used or emailed without
attracting attention.

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
%doc %{_mandir}/man?/*
%{_bindir}/mimetic
%{perl_vendorlib}/Crypt/Mimetic.pm
%{perl_vendorlib}/Crypt/Mimetic
%{perl_vendorlib}/Error/Mimetic.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
