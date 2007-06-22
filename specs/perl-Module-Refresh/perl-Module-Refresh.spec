# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Refresh

Summary: Refresh %INC files when updated on disk
Name: perl-Module-Refresh
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Refresh/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Module-Refresh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1, perl(ExtUtils::MakeMaker)

%description
With this module, you can refresh %INC when updated on disk.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/Module::Refresh.3pm*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Refresh.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
