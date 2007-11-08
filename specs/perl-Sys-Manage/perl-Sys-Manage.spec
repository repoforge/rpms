# $Id$
# Authority: dries
# Upstream: Andrew V. Makarow <makarow$mail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Manage

Summary: Systems management command volley
Name: perl-Sys-Manage
Version: 0.56
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Manage/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MAKAROW/Sys-Manage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Systems management command volley.

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
%doc readme
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Sys/Manage.p*
%{perl_vendorlib}/Sys/Manage/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
