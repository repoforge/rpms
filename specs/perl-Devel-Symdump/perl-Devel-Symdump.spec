# $Id$
# Authority: dries
# Upstream: Andreas J. König <andreas,koenig$anima,de>

### EL6 ships with perl-Devel-Symdump-2.08-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Symdump

Summary: Dump symbol names or the symbol table
Name: perl-Devel-Symdump
Version: 2.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Symdump/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Symdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Dump symbol names or the symbol table.

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
%doc ChangeLog ChangeLog.svn MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Devel::Symdump.3pm*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/Symdump/
%{perl_vendorlib}/Devel/Symdump.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.08-1
- Updated to release 2.08.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Updated to release 2.07.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
