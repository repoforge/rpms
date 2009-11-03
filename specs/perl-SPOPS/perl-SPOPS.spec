# $Id$
# Authority: dries
# Upstream: Chris Winters <chris$cwinters,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SPOPS

Summary: Simple Perl Object Persistence with Security
Name: perl-SPOPS
Version: 0.87
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SPOPS/

Source: http://www.cpan.org/authors/id/C/CW/CWINTERS/SPOPS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
SPOPS is a robust and powerful module that allows you to serialize
objects. It is unique in that it also allows you to apply security to
these objects using a fairly simple but powerful scheme of users and
groups. (You can, of course, turn off security if you want.)

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
%{perl_vendorlib}/SPOPS.pm
%{perl_vendorlib}/SPOPS

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.87-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.87-1
- Initial package.
